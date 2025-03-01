import pandas as pd
from dash import Input, Output
from app import app

df = pd.read_csv("data/processed/prep_bank_marketing.csv")

# Convert 'y' column to numeric values
df['y_numeric'] = df['y'].map({'yes': 1, 'no': 0})

# Standardize job categories
df['job_prep'] = df['job_prep'].str.lower().str.strip()

@app.callback(
    [Output("prop_subscribed", "children"),
     Output("avg_contacts_campaign", "children"),
     Output("avg_contacts_before", "children"),
     Output("avg_last_contact", "children"),
     Output("subscribed_summary", "children")],
    [Input("year_filter", "value"),
     Input("age_filter", "value"),
     Input("marital_filter", "value"),
     Input("job_filter", "value")],
)
def update_cards(selected_years, selected_age, selected_marital, selected_job):
    if not selected_years or not selected_marital or selected_job is None:
        return ["N/A"] * 5

    min_age, max_age = selected_age

    filtered_df = df[
        (df["year"].isin([int(y) for y in selected_years])) &
        (df["age"] >= min_age) & (df["age"] <= max_age) &
        (df["marital"].isin(selected_marital)) &
        (df["job_prep"] == selected_job.lower() if selected_job else False)
    ]

    if filtered_df.empty:
        return ["N/A"] * 5

    prop_subscribed = filtered_df["y_numeric"].mean()
    avg_contacts_campaign = filtered_df["campaign"].mean()
    avg_contacts_before = filtered_df["previous"].mean()
    avg_last_contact = filtered_df["duration"].mean()

    subscribed_summary = f"Yes: {sum(filtered_df['y_numeric'])} / No: {len(filtered_df) - sum(filtered_df['y_numeric'])}"

    return (
        f"{prop_subscribed:.2f}",
        f"{avg_contacts_campaign:.2f}",
        f"{avg_contacts_before:.2f}",
        f"{avg_last_contact:.1f} mins",
        subscribed_summary
    )
