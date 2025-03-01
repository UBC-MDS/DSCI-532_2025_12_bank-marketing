import dash_bootstrap_components as dbc
from dash import html

def create_stat_card(title, value_id):
    """
    Creates a single statistic card component.
    :param title: Title of the metric
    :param value_id: ID for the value to be updated dynamically
    """
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="card-title"),
            html.H2(id=value_id, children="...", className="card-value")
        ]),
        className="mb-3 p-3 shadow-sm",
    )

# Define all the required cards
cards = dbc.Row([
    dbc.Col(create_stat_card("Proportion Subscribed", "prop_subscribed"), width=2),
    dbc.Col(create_stat_card("Avg Contacts (Campaign)", "avg_contacts_campaign"), width=2),
    dbc.Col(create_stat_card("Avg Contacts (Before)", "avg_contacts_before"), width=2),
    dbc.Col(create_stat_card("Avg Last Contact Duration", "avg_last_contact"), width=2),
    dbc.Col(create_stat_card("Subscribed? (Yes/No)", "subscribed_summary"), width=2),
])
