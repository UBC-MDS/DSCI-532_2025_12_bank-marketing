# Milestone 3 - Reflection

## Implementation Progress

Since Milestone 2, we have implemented the feedback made by our professor, Daniel Chen. More specifically we changed the following:

### **Implemented Features**

-   Hid away *Info* as a tab for better use of the app real estate
-   Removed the plots' legends and added them to *Subscribed* card instead for conciseness
-   **Changes in Summary Statistics Cards:**
    -   Align the cards with the figures for a nicer presentation
    -   Changed *Proportion Subscribed* to percentage for better readability
    -   Changed proportions to percentages 
    -   *Average Contacts* have their separate line for easier visualization
    -   Added colors in the upper cards for better visualization 
    -   Removed parenthesis from *Average Contacts*

------------------------------------------------------------------------

## **Deviations from Proposal**

We stayed close to our original proposal; however, we made one key change:

-   Replaced the ***Campaign Contact and Subscription Status*** **density plot** with a **strip plot** with size encoding.

-   **Reason for the change:**

    -   The number of contacts is a **discrete variable**, and a density plot assumes continuity, which may misrepresent the data.

    -   A strip plot allows us to **visualize individual data points and their frequency** more explicitly.

-   **Challenges with the strip plot:**

    -   Due to overlapping points and the dense distribution at lower contact values, interpretation may be difficult at a glance.

-   **Future considerations for Milestone 4:**

    -   We may explore alternative visualizations to improve readability while preserving the discreteness of the number of contacts (See **Dashboard Limitations & Future Improvements** for more details)

------------------------------------------------------------------------

## **What Dashboard Does Well**

**Clear and Organized Layout:**

-   The dashboard is neatly structured, with filters on the left and key insights in the main section.

-   The top summary cards are clearly labeled, and proportions are displayed as percentages for better readability.

**Effective Use of Filters:**

-   Users can filter by **Year**, **Age**, **Marital** **Status**, and **Job** **Type,** which helps in segmenting customer behavior.

**Key Business Metrics Are Highlighted:**

-   Important campaign statistics (e.g. *Average Contacts CURRENT Campaign, Average Last Contact Duration*) help in assessing outreach effectiveness

**Diverse Visualizations:**

-   *Proportion of Subscribed Users by Education Level* (Stacked Bar Chart)
-   *Balance Distribution by Subscription Status* (Density Plot)
-   *Campaign Contact and Subscription Status* (Strip Plot)
-   *Distribution of Personal Loan by Subscription Status* (Grouped Bar Chart)

**Subscription Status Breakdown:**

-   The *Subscribed* card effectively captures the goal of the dashboard (subscription status) with a color-coded breakdown (green for yes, red for no)

    ------------------------------------------------------------------------

    ## **Dashboard Limitations & Future Improvements**

    **Visual Improvements:** Interpretability of the Strip Plot

-   While it correctly shows discrete contact counts, overlapping points make it harder to interpret patterns.

-   Alternative representations to improve readability could be:

    -   **Violin plot** – Shows distribution while maintaining the distinction between discrete values.

    -   **Binned scatterplot** – Reduces clutter and provides a clearer view of data concentration.

    **Usability Improvements:** No Filter Reset Button

-   Currently, users have to manually reset filters to return to the default selection. This can be inconvenient, especially when multiple filters are adjusted.

-   A filter reset button would enhance usability, allowing users to quickly revert to default selections and efficiently explore different filter combinations.
