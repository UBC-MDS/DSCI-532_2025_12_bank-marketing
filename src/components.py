import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import html

def create_stat_card(title, value_id):
    """
    Creates a single statistic card component.
    :param title: Title of the metric
    :param value_id: ID for the value to be updated dynamically
    """
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="card-title", style={'textAlign': 'center'}),
            html.H4(id=value_id, children="...", className="card-value", style={'textAlign': 'center'})
        ],
        style={
            'padding': '3px',
            'fontSize': '20px',
            'textAlign': 'center'
        }),
        className="mb-3 p-3 shadow-sm",
        style={'width': '100%', 'height': '100%', 'textAlign': 'center'}  
    )


def create_plot_card(plot_id):
    return dbc.Container([
        html.Div(
            dvc.Vega(id=plot_id, style={'width': '100%', 'height': '100%'}),
            style={'backgroundColor': 'white'}
        )
    ], className="mb-6 shadow-sm p-3", fluid=True, style={'height': '100%', 'backgroundColor': 'white'})


# Define all the required cards
cards = dbc.Row([
    dbc.Col(create_stat_card("Proportion Subscribed", "prop_subscribed"), style={'height': '100%'}),
    dbc.Col(create_stat_card("Avg Contacts (Campaign)", "avg_contacts_campaign"), style={'height': '100%'}),
    dbc.Col(create_stat_card("Avg Contacts (Before)", "avg_contacts_before"), style={'height': '100%'}),
    dbc.Col(create_stat_card("Avg Last Contact Duration", "avg_last_contact"), style={'height': '100%'}),
    dbc.Col(create_stat_card("Subscribed?", "subscribed_summary"), style={'height': '100%'}),
], style={'height': '95%'})

balance_plot = create_plot_card("balance_plot")

contact_plot = create_plot_card("contact_plot")

loan_plot = create_plot_card("loan_plot")

education_plot = create_plot_card("education_plot")

