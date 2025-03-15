from dash import Input, Output, State, ctx, dcc
import io
import pandas as pd
from dash import Input, Output, html, State
from src.app import dash_app
import altair as alt
from functools import lru_cache
alt.data_transformers.enable('default', max_rows=50000)

df = pd.read_csv("data/processed/prep_bank_marketing.csv")

plot_width = 380
plot_height = 190

@lru_cache(maxsize=128)
def filter_by_checklists(years_tuple, marital_tuple, job):
    years = list(years_tuple)
    marital = list(marital_tuple)
    return df[
        (df["year"].isin([int(y) for y in years])) &
        (df["marital"].isin(marital)) &
        (df["job_prep"] == job.lower() if job else False)
    ]

def create_balance_plot(data):
    chart = alt.Chart(data, width='container').transform_density(
        'balance', as_=['balance', 'density'], groupby=['y']
    ).mark_area(opacity=0.75).encode(

        x=alt.X('balance:Q', title='Balance (EUR)', axis=alt.Axis(titleFontSize=16)),
        y=alt.Y('density:Q', title='Density', axis=alt.Axis(titleFontSize=16)).stack(False),
        color=alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), title='Subscribed', legend=None)
    ).properties(
        width=plot_width,  
        height=plot_height
    ).interactive()

    return chart.to_dict()

def create_contact_plot(data):
    chart = alt.Chart(data).mark_square().encode(
         x=alt.X('campaign:Q', title='Number of Contacts During this Campaign', axis=alt.Axis(titleFontSize=16)),
         y=alt.Y('y:N', title='Subscribed', axis=alt.Axis(titleFontSize=16)),
         color=alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), title='Subscribed?', legend=None),
         size=alt.Size('count()', legend=alt.Legend(title="Count of Records", orient="right")),
         tooltip=['campaign:Q', 'y:N', 'count():Q']
    ).properties(
        width=plot_width,
        height=plot_height
    ).interactive()

    return chart.to_dict()

def create_loan_plot(data):
    chart = alt.Chart(data).mark_bar(size=40).encode(
        alt.X('loan:N', title='Has Personal Loan', axis=alt.Axis(labelAngle=360, titleFontSize=16)),
        alt.Y('count()', title='Counts', axis=alt.Axis(titleFontSize=16)),
        alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), title='Subscribed?'),
        alt.XOffset('y:N'),
        alt.Tooltip(['count():Q'])
    ).properties(
        width=plot_width,  
        height=plot_height
    ).interactive()

    return chart.to_dict()

def create_education_plot(data):
    data_aggregated = data.groupby(['education', 'y']).size().reset_index(name='count')
    data_aggregated['total'] = data_aggregated.groupby('education')['count'].transform('sum')
    data_aggregated['proportion'] = data_aggregated['count'] / data_aggregated['total']
    
    chart = alt.Chart(data_aggregated).mark_bar().encode(
        alt.X('education:N', title='Education', axis=alt.Axis(labelAngle=360, titleFontSize=16)),  
        alt.Y('proportion:Q', title='Proportion', stack='zero', axis=alt.Axis(titleFontSize=16)),
        alt.Color(
            'y:N',
            scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']),
            title='Subscribed?', 
            sort=['yes', 'no'], 
            legend=alt.Legend(orient='right')),
        alt.Tooltip(['proportion:Q'])
        ).properties(
            width=plot_width,  
            height=plot_height
            ).interactive()
    
    return chart.to_dict()

@lru_cache(maxsize=128)
def calculate_stats(df_key):
    filtered_df = df.loc[list(df_key)]
    
    stats = {
        'prop_subscribed': filtered_df["y_numeric"].mean(),
        'avg_contacts_campaign': filtered_df["campaign"].mean(),
        'avg_contacts_before': filtered_df["previous"].mean(),
        'avg_last_contact': filtered_df["duration"].mean(),
        'yes_count': sum(filtered_df['y_numeric']),
        'no_count': len(filtered_df) - sum(filtered_df['y_numeric'])
    }
    
    return stats

def return_empty(balance_plot, contact_plot, loan_plot, education_plot):
    subscribed_summary = [
        html.P("Yes: 0", style={
            'margin': '0px',
            'color': '#60ac5a',
            'fontSize': '1.2rem',
            'fontWeight': 'bold'
        }),
        html.P("No: 0", style={
            'margin': '0px',
            'color': '#d16f6f',
            'fontSize': '1.2rem',
            'fontWeight': 'bold'
        })
    ]
    return (
        "0%",
        0,
        0,
        0,
        subscribed_summary,
        balance_plot,
        contact_plot,
        loan_plot,
        education_plot
    )

DEFAULT_YEARS = ['2008', '2009', '2010']
DEFAULT_AGE_RANGE = [25, 60]
DEFAULT_MARITAL = ['married', 'divorced', 'single']
DEFAULT_JOB = 'employed'

default_filtered_df = filter_by_checklists(tuple(DEFAULT_YEARS), tuple(DEFAULT_MARITAL), DEFAULT_JOB)
age_mask = (df["age"] >= DEFAULT_AGE_RANGE[0]) & (df["age"] <= DEFAULT_AGE_RANGE[1])
default_filtered_df = default_filtered_df[age_mask]

DEFAULT_BALANCE_PLOT = create_balance_plot(default_filtered_df)
DEFAULT_CONTACT_PLOT = create_contact_plot(default_filtered_df)
DEFAULT_LOAN_PLOT = create_loan_plot(default_filtered_df)
DEFAULT_EDUCATION_PLOT = create_education_plot(default_filtered_df)

default_stats = calculate_stats(tuple(default_filtered_df.index))
DEFAULT_PROP_SUBSCRIBED = default_stats['prop_subscribed']
DEFAULT_AVG_CONTACTS_CAMPAIGN = default_stats['avg_contacts_campaign']
DEFAULT_AVG_CONTACTS_BEFORE = default_stats['avg_contacts_before']
DEFAULT_AVG_LAST_CONTACT = default_stats['avg_last_contact']
DEFAULT_YES_COUNT = default_stats['yes_count']
DEFAULT_NO_COUNT = default_stats['no_count']

DEFAULT_SUBSCRIBED_SUMMARY = [
    html.P(f"Yes: {DEFAULT_YES_COUNT}", style={
        'margin': '0px',
        'color': '#60ac5a',
        'fontSize': '1.2rem',
        'fontWeight': 'bold'
    }),
    html.P(f"No: {DEFAULT_NO_COUNT}", style={
        'margin': '0px',
        'color': '#d16f6f',
        'fontSize': '1.2rem',
        'fontWeight': 'bold'
    })
]

@lru_cache(maxsize=128)
def get_card_updates(years_tuple, age_min, age_max, marital_tuple, job):
    """Cached version of card updates calculation"""
    is_default = (
        set(years_tuple) == set(DEFAULT_YEARS) and
        age_min == DEFAULT_AGE_RANGE[0] and
        age_max == DEFAULT_AGE_RANGE[1] and
        set(marital_tuple) == set(DEFAULT_MARITAL) and
        job.lower() == DEFAULT_JOB
    )

    if is_default:
        return (
            f"{DEFAULT_PROP_SUBSCRIBED:.1%}",
            f"{DEFAULT_AVG_CONTACTS_CAMPAIGN:.2f}",
            f"{DEFAULT_AVG_CONTACTS_BEFORE:.2f}",
            f"{DEFAULT_AVG_LAST_CONTACT:.1f}",
            DEFAULT_SUBSCRIBED_SUMMARY,
            DEFAULT_BALANCE_PLOT,
            DEFAULT_CONTACT_PLOT,
            DEFAULT_LOAN_PLOT,
            DEFAULT_EDUCATION_PLOT
        )

    filtered_df = filter_by_checklists(years_tuple, marital_tuple, job)
    age_mask = (df["age"] >= age_min) & (df["age"] <= age_max)
    filtered_df = filtered_df[age_mask]

    if filtered_df.empty:
        return return_empty(
            create_balance_plot(filtered_df),
            create_contact_plot(filtered_df),
            create_loan_plot(filtered_df),
            create_education_plot(filtered_df)
        )

    stats = calculate_stats(tuple(filtered_df.index))
    
    subscribed_summary = [
        html.P(f"Yes: {stats['yes_count']}", style={
            'margin': '0px',
            'color': '#60ac5a',
            'fontSize': '1.2rem',
            'fontWeight': 'bold'
        }),
        html.P(f"No: {stats['no_count']}", style={
            'margin': '0px',
            'color': '#d16f6f',
            'fontSize': '1.2rem',
            'fontWeight': 'bold'
        })
    ]

    return (
        f"{stats['prop_subscribed']:.1%}",
        f"{stats['avg_contacts_campaign']:.2f}",
        f"{stats['avg_contacts_before']:.2f}",
        f"{stats['avg_last_contact']:.1f}",
        subscribed_summary,
        create_balance_plot(filtered_df),
        create_contact_plot(filtered_df),
        create_loan_plot(filtered_df),
        create_education_plot(filtered_df)
    )

@dash_app.callback(
    [Output("prop_subscribed", "children"),
     Output("avg_contacts_campaign", "children"),
     Output("avg_contacts_before", "children"),
     Output("avg_last_contact", "children"),
     Output("subscribed_summary", "children")],
     Output('balance_plot', 'spec'),
     Output('contact_plot', 'spec'),
     Output('loan_plot', 'spec'),
     Output('education_plot', 'spec'),
    [Input("year_filter", "value"),
     Input("age_filter", "value"),
     Input("marital_filter", "value"),
     Input("job_filter", "value")],
)
def update_cards(selected_years, selected_age, selected_marital, selected_job):
    """Main callback function that uses the cached get_card_updates"""
    min_age, max_age = selected_age
    return get_card_updates(
        tuple(selected_years),
        min_age,
        max_age,
        tuple(selected_marital),
        selected_job
    )

@dash_app.callback(
    [Output("year_filter", "value"),
     Output("age_filter", "value"),
     Output("marital_filter", "value"),
     Output("job_filter", "value")],
    Input("reset-button", "n_clicks"),
    prevent_initial_call=True
)
def reset_filters(n_clicks):
    return DEFAULT_YEARS, DEFAULT_AGE_RANGE, DEFAULT_MARITAL, DEFAULT_JOB

@dash_app.callback(
    Output("download_data", "data"),
    Input("download_button", "n_clicks"),
    State("year_filter", "value"),
    State("age_filter", "value"),
    State("marital_filter", "value"),
    State("job_filter", "value"),
    prevent_initial_call=True
)
def download_filtered_data(n_clicks, selected_years, selected_age, selected_marital, selected_job):
    # Ensure there's a click trigger
    if n_clicks is None:
        return None
    
    # Reuse the same filtering logic as in `update_cards`
    min_age, max_age = selected_age
    filtered_df = df[
        (df["year"].isin([int(y) for y in selected_years])) &
        (df["age"] >= min_age) & (df["age"] <= max_age) &
        (df["marital"].isin(selected_marital)) &
        (df["job_prep"] == selected_job.lower() if selected_job else False)
    ]

    # Convert filtered_df to CSV
    if filtered_df.empty:
        return None

    return dcc.send_data_frame(filtered_df.to_csv, filename="filtered_bank_marketing_data.csv", index=False)

