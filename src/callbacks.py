import pandas as pd
from dash import Input, Output, html
from src.app import dash_app
import altair as alt
alt.data_transformers.enable('default', max_rows=50000)

df = pd.read_csv("data/processed/prep_bank_marketing.csv")

plot_width = 380
plot_height = 190

def create_balance_plot(data):
    chart = alt.Chart(data, width='container').transform_density(
        'balance', as_=['balance', 'density'], groupby=['y']
    ).mark_area(opacity=0.75).encode(
        x=alt.X('balance:Q', title='Balance', axis=alt.Axis(titleFontSize=16)),
        y=alt.Y('density:Q', title='Density', axis=alt.Axis(titleFontSize=16)),
        color=alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), title='Subscribed?')
    ).properties(
        width=plot_width,  
        height=plot_height
    ).interactive()

    return chart.to_dict()

def create_contact_plot(data):
    chart = alt.Chart(data).mark_square().encode(
         x=alt.X('campaign:Q', title='Number of Contacts During this Campaign', axis=alt.Axis(titleFontSize=16)),
         y=alt.Y('y:N', title='Subscribed?', axis=alt.Axis(titleFontSize=16)),
         color=alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), title='Subscribed?'),
         size='count()',
         tooltip=['campaign:Q', 'y:N', 'count():Q']
    ).properties(
        width=plot_width,
        height=plot_height
    ).interactive()

    return chart.to_dict()

def create_loan_plot(data):
    chart = alt.Chart(data).mark_bar(size=40).encode(
        alt.X('loan:N', title='Has Personal Loan?', axis=alt.Axis(labelAngle=360, titleFontSize=16)),
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

def return_empty(balance_plot, contact_plot, loan_plot, education_plot):
    subscribed_summary = [
                html.P(f"Yes: {0}", style={'margin': '0px'}),
                html.P(f"No: {0}", style={'margin': '0px'})
            ]
    return (
        0,
        0,
        0,
        0,
        subscribed_summary,
        balance_plot,
        contact_plot,
        loan_plot,
        education_plot
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
    min_age, max_age = selected_age

    filtered_df = df[
        (df["year"].isin([int(y) for y in selected_years])) &
        (df["age"] >= min_age) & (df["age"] <= max_age) &
        (df["marital"].isin(selected_marital)) &
        (df["job_prep"] == selected_job.lower() if selected_job else False)
    ]

    balance_plot = create_balance_plot(filtered_df)
    contact_plot = create_contact_plot(filtered_df)
    loan_plot = create_loan_plot(filtered_df)
    education_plot = create_education_plot(filtered_df)

    if filtered_df.empty:
        return return_empty(balance_plot, contact_plot, loan_plot, education_plot)

    prop_subscribed = filtered_df["y_numeric"].mean()
    avg_contacts_campaign = filtered_df["campaign"].mean()
    avg_contacts_before = filtered_df["previous"].mean()
    avg_last_contact = filtered_df["duration"].mean()

    yes_count = sum(filtered_df['y_numeric'])
    no_count = len(filtered_df) - yes_count

    subscribed_summary = [
        html.P(f"Yes: {yes_count}", style={'margin': '0px'}),
        html.P(f"No: {no_count}", style={'margin': '0px'})
    ]

    return (
        f"{prop_subscribed:.2f}",
        f"{avg_contacts_campaign:.2f}",
        f"{avg_contacts_before:.2f}",
        f"{avg_last_contact:.1f}",
        subscribed_summary,
        balance_plot,
        contact_plot,
        loan_plot,
        education_plot
    )
