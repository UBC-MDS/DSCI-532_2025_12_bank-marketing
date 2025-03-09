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



## **Deviations from Proposal**

We stayed close to our original proposal; however, we made one key change:

-   Replaced the ***Campaign Contact and Subscription Status*** **density plot** with a **strip plot** with size encoding.

-   **Reason for the change:**

    -   The number of contacts is a **discrete variable**, and a density plot assumes continuity, which may misrepresent the data.



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


## **Dashboard Limitations & Future Improvements**

**Visual Improvements:** Interpretability of the Strip Plot

-   While it correctly shows discrete contact counts, the distribution is right-skewed and it makes the patterns for points in the right harder to interpret.

**Usability Improvements:** No Filter Reset Button

-   Currently, users have to manually reset filters to return to the default selection. This can be inconvenient, especially when multiple filters are adjusted.

-   A filter reset button would enhance usability, allowing users to quickly revert to default selections and efficiently explore different filter combinations.


## Challenging

Our dashboard seems to be well optimized and we didn't want to change something significantly. But as a group we were discussing how to make the Info of the dashboard better. Daniel suggested several options that could potentially work, but the final decision was inspired from [Group 3](https://dsci-532-2025-3-quantatrack.onrender.com/) usage of tabs. We found it efficient to use a different tab for a section that is partially or completely independent of the current view. We decided to implement an INFO tab alongside the FILTERS tab. This allows users to switch between viewing dashboard information and adjusting filters without cluttering the main interface.