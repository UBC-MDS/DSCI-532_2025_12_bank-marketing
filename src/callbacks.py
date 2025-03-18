from dash import Input, Output, State, ctx, dcc
import pandas as pd
from dash import Input, Output, html, State
from app import dash_app
import altair as alt
from functools import lru_cache
alt.data_transformers.enable('default', max_rows=50000)

# Reading the parquet file containing the processed bank marketing data into a pandas DataFrame
df = pd.read_parquet("data/processed/prep_bank_marketing.parquet")

# Setting the width for plots to be created later
plot_width = 380  # Width in pixels for the plot

# Setting the height for plots to be created later
plot_height = 190  # Height in pixels for the plot

@lru_cache(maxsize=128)
def filter_by_checklists(years_tuple, marital_tuple, job):
    """
    Filters the DataFrame based on the provided years, marital status, and job.

    Parameters
    ----------
    years_tuple : tuple of int or str
        Tuple containing the years to filter by.
    marital_tuple : tuple of str
        Tuple containing the marital statuses to filter by.
    job : str, optional
        Job type to filter by. If None, no filtering is applied to the job column.

    Returns
    -------
    pandas.DataFrame
        A filtered DataFrame containing only rows that match the specified years, marital status, and job.
    """
    
    # Convert the years_tuple to a list of integers
    years = list(years_tuple)
    
    # Convert the marital_tuple to a list
    marital = list(marital_tuple)
    
    # Filter the DataFrame based on the conditions
    return df[
        (df["year"].isin([int(y) for y in years])) &  # Filter rows by years
        (df["marital"].isin(marital)) &  # Filter rows by marital status
        (df["job_prep"] == job.lower() if job else False)  # Filter rows by job, case insensitive
    ]



def create_balance_plot(data):
    """
    Creates a density plot of balance distribution for different subscription statuses.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data with at least the 'balance' and 'y' columns, where 'balance' represents
        the account balance and 'y' indicates subscription status (e.g., 'yes' or 'no').

    Returns
    -------
    dict
        A dictionary representation of the Altair chart object.
    """
    
    # Create the density chart based on 'balance' grouped by subscription status ('y')
    chart = alt.Chart(data, width='container').transform_density(
        'balance', as_=['balance', 'density'], groupby=['y']
    ).mark_area(opacity=0.75).encode(
        # X-axis representing the balance values (quantitative)
        x=alt.X('balance:Q', title='Balance (EUR)', axis=alt.Axis(titleFontSize=16)),
        
        # Y-axis representing the density values (quantitative), with stacking disabled
        y=alt.Y('density:Q', title='Density', axis=alt.Axis(titleFontSize=16)).stack(False),
        
        # Color encoding based on subscription status, with custom colors
        color=alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), legend=None)
    ).properties(
        width=plot_width,  # Set the width of the chart
        height=plot_height  # Set the height of the chart
    ).interactive()  # Enable chart interactivity

    # Return the Altair chart as a dictionary
    return chart.to_dict()



def create_contact_plot(data):
    """
    Creates a scatter plot displaying the number of contacts made during a campaign, 
    with different colors and sizes representing the subscription status and 
    the count of records.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data with at least the 'campaign' and 'y' columns, where 'campaign' represents 
        the number of contacts during the campaign, and 'y' represents subscription status (e.g., 'yes' or 'no').

    Returns
    -------
    dict
        A dictionary representation of the Altair chart object.
    """
    
    # Create a scatter plot (with squares) using the 'campaign' and 'y' columns
    chart = alt.Chart(data).mark_square().encode(
        # X-axis represents the number of contacts during the campaign (quantitative)
        x=alt.X('campaign:Q', title='Number of Contacts During this Campaign', axis=alt.Axis(titleFontSize=16)),
        
        # Y-axis represents the subscription status (categorical)
        y=alt.Y('y:N', title='Subscribed', axis=alt.Axis(titleFontSize=16)),
        
        # Color encoding for subscription status, with custom colors for 'yes' and 'no'
        color=alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), legend=None),
        
        # Size encoding based on the count of records for each combination of 'campaign' and 'y'
        size=alt.Size('count()', legend=alt.Legend(title="Count of Records", orient="right")),
        
        # Tooltip to display the campaign number, subscription status, and count for each point
        tooltip=['campaign:Q', 'y:N', 'count():Q']
    ).properties(
        width=plot_width,  # Set the width of the chart
        height=plot_height  # Set the height of the chart
    ).interactive()  # Enable chart interactivity

    # Return the Altair chart as a dictionary
    return chart.to_dict()



def create_loan_plot(data):
    """
    Creates a bar chart displaying the count of records based on whether a customer has a personal loan,
    with different colors representing the subscription status (e.g., 'yes' or 'no').

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data with at least the 'loan' and 'y' columns. The 'loan' column represents 
        whether a customer has a personal loan ('yes' or 'no'), and 'y' represents subscription status.

    Returns
    -------
    dict
        A dictionary representation of the Altair chart object.
    """
    
    # Create a bar chart with the 'loan' and 'y' columns
    chart = alt.Chart(data).mark_bar(size=40).encode(
        # X-axis represents whether the customer has a personal loan (categorical)
        alt.X('loan:N', title='Has Personal Loan', axis=alt.Axis(labelAngle=360, titleFontSize=16)),
        
        # Y-axis represents the count of records for each loan status
        alt.Y('count()', title='Counts', axis=alt.Axis(titleFontSize=16)),
        
        # Color encoding for subscription status, with custom colors for 'yes' and 'no'
        alt.Color('y:N', scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']), legend=None),
        
        # X-offset for the bars based on the subscription status
        alt.XOffset('y:N'),
        
        # Tooltip to display the count of records for each combination of 'loan' and 'y'
        alt.Tooltip(['count():Q'])
    ).properties(
        width=plot_width,  # Set the width of the chart
        height=plot_height  # Set the height of the chart
    ).interactive()  # Enable chart interactivity

    # Return the Altair chart as a dictionary
    return chart.to_dict()



def create_education_plot(data):
    """
    Creates a bar chart displaying the proportion of customers with a certain level of education 
    who are subscribed, with different colors representing subscription status ('yes' or 'no').

    The data is aggregated by 'education' and 'y' (subscription status), and the proportions are 
    calculated for each education level.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data with at least the 'education' and 'y' columns. The 'education' 
        column represents the level of education, and 'y' represents subscription status ('yes' or 'no').

    Returns
    -------
    dict
        A dictionary representation of the Altair chart object.
    """
    
    # Aggregate the data by education level and subscription status, and calculate counts
    data_aggregated = data.groupby(['education', 'y']).size().reset_index(name='count')
    
    # Calculate the total number of records for each education level
    data_aggregated['total'] = data_aggregated.groupby('education')['count'].transform('sum')
    
    # Calculate the proportion of each group (count / total) for each education level
    data_aggregated['proportion'] = data_aggregated['count'] / data_aggregated['total']
    
    # Create a bar chart with the aggregated data
    chart = alt.Chart(data_aggregated).mark_bar().encode(
        # X-axis represents the education level (categorical)
        alt.X('education:N', title='Education', axis=alt.Axis(labelAngle=360, titleFontSize=16)),  
        
        # Y-axis represents the proportion of subscribers in each education level
        alt.Y('proportion:Q', title='Proportion', stack='zero', axis=alt.Axis(titleFontSize=16)),
        
        # Color encoding for subscription status, with custom colors for 'yes' and 'no'
        alt.Color(
            'y:N',
            scale=alt.Scale(domain=['yes', 'no'], range=['#60ac5a', '#d16f6f']),
            sort=['yes', 'no'], 
            legend=None),
        
        # Tooltip to display the proportion of subscribers for each education level
        alt.Tooltip(['proportion:Q'])
    ).properties(
        width=plot_width,  # Set the width of the chart
        height=plot_height  # Set the height of the chart
    ).interactive()  # Enable chart interactivity
    
    # Return the Altair chart as a dictionary
    return chart.to_dict()



@lru_cache(maxsize=128)
def calculate_stats(df_key):
    """
    Calculate statistics for a subset of the DataFrame based on the provided key.

    This function filters the DataFrame by the given key, computes several statistics for 
    the filtered subset, and returns a dictionary containing these statistics. The statistics 
    include the proportion of subscribers, average contacts in the current and previous campaigns, 
    average contact duration, and counts of subscribers and non-subscribers.

    Parameters
    ----------
    df_key : tuple
        A tuple of keys used to filter the DataFrame `df`. Each key corresponds to a row 
        in the DataFrame and is expected to be part of the index or columns.

    Returns
    -------
    dict
        A dictionary containing the following statistics:
        - 'prop_subscribed': Proportion of subscribers (mean of 'y_numeric' column).
        - 'avg_contacts_campaign': Average number of contacts during the current campaign.
        - 'avg_contacts_before': Average number of contacts in previous campaigns.
        - 'avg_last_contact': Average contact duration.
        - 'yes_count': Number of subscribers (sum of 'y_numeric').
        - 'no_count': Number of non-subscribers (total rows minus 'yes_count').
    """
    
    # Filter the DataFrame based on the provided keys (df_key)
    filtered_df = df.loc[list(df_key)]
    
    # Calculate the statistics for the filtered data
    stats = {
        'prop_subscribed': filtered_df["y_numeric"].mean(),  # Proportion of subscribers
        'avg_contacts_campaign': filtered_df["campaign"].mean(),  # Average number of contacts in the current campaign
        'avg_contacts_before': filtered_df["previous"].mean(),  # Average number of contacts in previous campaigns
        'avg_last_contact': filtered_df["duration"].mean(),  # Average contact duration
        'yes_count': sum(filtered_df['y_numeric']),  # Number of subscribers
        'no_count': len(filtered_df) - sum(filtered_df['y_numeric'])  # Number of non-subscribers
    }
    
    return stats



def return_empty(balance_plot, contact_plot, loan_plot, education_plot):
    """
    Return empty statistics and plots for display when no data is available.

    This function returns default values representing a scenario where no data is available. 
    It provides zero values for statistics, an empty subscription summary, and the provided 
    plot objects unchanged.

    Parameters
    ----------
    balance_plot : Plot object
        A plot object for the balance plot (e.g., a chart).
        
    contact_plot : Plot object
        A plot object for the contact plot (e.g., a chart).
        
    loan_plot : Plot object
        A plot object for the loan plot (e.g., a chart).
        
    education_plot : Plot object
        A plot object for the education plot (e.g., a chart).

    Returns
    -------
    tuple
        A tuple containing the following values:
        - "0%" (str): Represents 0% as a string for the subscription proportion.
        - 0 (int): Placeholder for the "yes" count (set to 0).
        - 0 (int): Placeholder for the "no" count (set to 0).
        - 0 (int): Placeholder for the average contacts (set to 0).
        - subscribed_summary (list): A list of HTML elements showing "Yes: 0" and "No: 0" with 
          specific styles for subscription counts.
        - balance_plot (Plot object): The unchanged balance plot object passed to the function.
        - contact_plot (Plot object): The unchanged contact plot object passed to the function.
        - loan_plot (Plot object): The unchanged loan plot object passed to the function.
        - education_plot (Plot object): The unchanged education plot object passed to the function.
    """
    
    # Subscription summary with zero values for both "Yes" and "No"
    subscribed_summary = [
        html.P("Yes: 0", style={
            'margin': '0px',
            'color': '#60ac5a',
            'fontSize': '1.6rem',
            'fontWeight': 'bold'
        }),
        html.P("No: 0", style={
            'margin': '0px',
            'color': '#d16f6f',
            'fontSize': '1.6rem',
            'fontWeight': 'bold'
        })
    ]
    
    # Return the tuple with all default values and provided plot objects
    return (
        "0%",  # Proportion of subscribers (0% as a string)
        0,  # "Yes" count
        0,  # "No" count
        0,  # Average number of contacts
        subscribed_summary,  # Subscription summary
        balance_plot,  # Unchanged balance plot
        contact_plot,  # Unchanged contact plot
        loan_plot,  # Unchanged loan plot
        education_plot  # Unchanged education plot
    )


# Default filter values

DEFAULT_YEARS = ['2008', '2009', '2010']
DEFAULT_AGE_RANGE = [25, 60]
DEFAULT_MARITAL = ['married', 'divorced', 'single']
DEFAULT_JOB = 'employed'

# Default filtered df

default_filtered_df = filter_by_checklists(tuple(DEFAULT_YEARS), tuple(DEFAULT_MARITAL), DEFAULT_JOB)
age_mask = (df["age"] >= DEFAULT_AGE_RANGE[0]) & (df["age"] <= DEFAULT_AGE_RANGE[1])
default_filtered_df = default_filtered_df[age_mask]

# Create default plots

DEFAULT_BALANCE_PLOT = create_balance_plot(default_filtered_df)
DEFAULT_CONTACT_PLOT = create_contact_plot(default_filtered_df)
DEFAULT_LOAN_PLOT = create_loan_plot(default_filtered_df)
DEFAULT_EDUCATION_PLOT = create_education_plot(default_filtered_df)

# Create default summary stats

default_stats = calculate_stats(tuple(default_filtered_df.index))
DEFAULT_PROP_SUBSCRIBED = default_stats['prop_subscribed']
DEFAULT_AVG_CONTACTS_CAMPAIGN = default_stats['avg_contacts_campaign']
DEFAULT_AVG_CONTACTS_BEFORE = default_stats['avg_contacts_before']
DEFAULT_AVG_LAST_CONTACT = default_stats['avg_last_contact']
DEFAULT_YES_COUNT = default_stats['yes_count']
DEFAULT_NO_COUNT = default_stats['no_count']

# The default subscribed summary

DEFAULT_SUBSCRIBED_SUMMARY = [
    html.P(f"Yes: {DEFAULT_YES_COUNT}", style={
        'margin': '0px',
        'color': '#60ac5a',
        'fontSize': '1.6rem',
        'fontWeight': 'bold'
    }),
    html.P(f"No: {DEFAULT_NO_COUNT}", style={
        'margin': '0px',
        'color': '#d16f6f',
        'fontSize': '1.6rem',
        'fontWeight': 'bold'
    })
]




@lru_cache(maxsize=128)
def get_card_updates(years_tuple, age_min, age_max, marital_tuple, job):
    """
    Cached version of card updates calculation.

    This function filters the dataset based on the provided criteria (years, age range, marital status, and job).
    It calculates and returns key statistics (such as subscription proportion, average number of contacts, etc.)
    and visualizations (such as plots for balance, contact, loan, and education) for the filtered dataset. 
    If the default criteria is used, it returns pre-calculated default values and plots.

    Parameters
    ----------
    years_tuple : tuple of int
        A tuple containing the years to filter the data by.
        
    age_min : int
        The minimum age to filter the data by.
        
    age_max : int
        The maximum age to filter the data by.
        
    marital_tuple : tuple of str
        A tuple containing the marital statuses to filter the data by.
        
    job : str, optional
        The job title to filter the data by. If None, no filtering by job is applied.

    Returns
    -------
    tuple
        A tuple containing the following values:
        - Proportion of subscribers as a formatted string (e.g., "75.0%").
        - Average number of contacts during the campaign as a formatted string.
        - Average number of contacts before the campaign as a formatted string.
        - Average duration of the last contact as a formatted string.
        - Subscription summary as a list of HTML elements showing counts for "Yes" and "No".
        - Balance plot (Altair chart) for the filtered data.
        - Contact plot (Altair chart) for the filtered data.
        - Loan plot (Altair chart) for the filtered data.
        - Education plot (Altair chart) for the filtered data.
    """
    
    # If job is provided, convert to lowercase
    if job is not None:
        job = job.lower()

    # Check if the parameters are set to default values
    is_default = (
        set(years_tuple) == set(DEFAULT_YEARS) and
        age_min == DEFAULT_AGE_RANGE[0] and
        age_max == DEFAULT_AGE_RANGE[1] and
        set(marital_tuple) == set(DEFAULT_MARITAL) and
        job == DEFAULT_JOB
    )

    # Return default values if parameters are set to the defaults
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

    # Filter the dataframe based on the provided criteria
    filtered_df = filter_by_checklists(years_tuple, marital_tuple, job)
    
    # Apply age range filter
    age_mask = (df["age"] >= age_min) & (df["age"] <= age_max)
    filtered_df = filtered_df[age_mask]

    # If the filtered dataframe is empty, return default empty values
    if filtered_df.empty:
        return return_empty(
            create_balance_plot(filtered_df),
            create_contact_plot(filtered_df),
            create_loan_plot(filtered_df),
            create_education_plot(filtered_df)
        )

    # Calculate statistics on the filtered dataframe
    stats = calculate_stats(tuple(filtered_df.index))
    
    # Prepare the subscription summary with counts for "Yes" and "No"
    subscribed_summary = [
        html.P(f"Yes: {stats['yes_count']}", style={
            'margin': '0px',
            'color': '#60ac5a',
            'fontSize': '1.6rem',
            'fontWeight': 'bold'
        }),
        html.P(f"No: {stats['no_count']}", style={
            'margin': '0px',
            'color': '#d16f6f',
            'fontSize': '1.6rem',
            'fontWeight': 'bold'
        })
    ]

    # Return the calculated statistics and visualizations
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
    """
    Main callback function that updates the dashboard elements based on the selected filters.
    This function uses the `get_card_updates` method to retrieve statistics and visualizations,
    which are then updated on the dashboard.

    The function handles:
    - Years filter (`selected_years`)
    - Age range filter (`selected_age`)
    - Marital status filter (`selected_marital`)
    - Job filter (`selected_job`)

    Parameters
    ----------
    selected_years : list of int
        The selected years for filtering the data.

    selected_age : list of int
        A tuple representing the minimum and maximum ages to filter the data.

    selected_marital : list of str
        A list of selected marital statuses to filter the data by.

    selected_job : str
        The selected job to filter the data by.

    Returns
    -------
    tuple
        A tuple with the following values:
        - Proportion of subscribed users as a string (e.g., "75.0%").
        - Average number of contacts during the campaign as a string.
        - Average number of contacts before the campaign as a string.
        - Average duration of the last contact as a string.
        - Subscription summary as a list of HTML paragraphs with counts for "Yes" and "No".
        - Balance plot specification (Altair chart).
        - Contact plot specification (Altair chart).
        - Loan plot specification (Altair chart).
        - Education plot specification (Altair chart).
    """
    # Extract minimum and maximum age from the selected age filter
    min_age, max_age = selected_age

    # Call the cached function to get updated statistics and plots
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
    """
    Resets the filters to their default values when called. This function is typically
    triggered by a button click to reset the selected filters on the dashboard.

    Parameters
    ----------
    n_clicks : int
        The number of times the reset button has been clicked. This input is used to 
        trigger the reset action.

    Returns
    -------
    tuple
        A tuple containing the default filter values:
        - Default years range (list of years).
        - Default age range (tuple with min and max age).
        - Default marital status (tuple with marital categories).
        - Default job filter (string).
    """
    # Return default values for each filter
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
    """
    This callback function handles the download of filtered data as a CSV file. 
    The data is filtered based on the selected years, age range, marital status, 
    and job filter. The download is triggered by the user clicking the download button.

    Parameters
    ----------
    n_clicks : int
        The number of times the download button has been clicked. It is used to 
        trigger the download action.
    selected_years : list
        A list of selected years used to filter the data.
    selected_age : tuple
        A tuple with the minimum and maximum age for filtering.
    selected_marital : list
        A list of selected marital statuses used to filter the data.
    selected_job : str
        The job selected by the user used to filter the data.

    Returns
    -------
    dict or None
        If the data is not empty, a dictionary with the CSV file for download is returned.
        If the filtered data is empty, None is returned, and no download occurs.
    """
    
    # Ensure the download action is triggered by a button click
    if n_clicks is None:
        return None

    # Unpack the age range into min and max
    min_age, max_age = selected_age

    # Apply the filtering conditions to the DataFrame
    filtered_df = df[
        (df["year"].isin([int(y) for y in selected_years])) &
        (df["age"] >= min_age) & (df["age"] <= max_age) &
        (df["marital"].isin(selected_marital)) &
        (df["job_prep"] == selected_job.lower() if selected_job else False)
    ]

    # If the filtered DataFrame is empty, return None
    if filtered_df.empty:
        return None

    # Convert the filtered DataFrame to CSV and prepare it for download
    return dcc.send_data_frame(filtered_df.to_csv, filename="filtered_bank_marketing_data.csv", index=False)

