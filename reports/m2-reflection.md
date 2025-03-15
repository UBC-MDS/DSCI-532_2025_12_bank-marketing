# Milestone 2 - Reflection

## Implementation Progress

We have successfully implemented most of the core functionality outlined in our proposal. Below is a breakdown of what has been completed and what remains:

### **Implemented Features**

-   **Filters**: Users can filter by year, age, marital status, and job type using the sidebar. The filtering logic updates the displayed visualizations accordingly.
-   **Job Category Reduction**: The original 12 job categories have been grouped into 5 broader groups (`Employed`, `Unemployed`, `Student`, `Retired`, and `Unknown`) as planned in the preprocessing stage.
-   **Summary Statistics Cards**: The top row displays key marketing campaign metrics such as:
    -   Proportion of customers who subscribed
    -   Average number of contacts per campaign
    -   Average previous contacts before the campaign
    -   Average last contact duration in minutes
    -   Total count of subscribed and non-subscribed customers
-   **Visualizations**:
    -   Education vs. Subscription Rate (Stacked Bar Chart)
    -   Number of Contacts vs. Subscription Rate (Square plot)
    -   Balance vs. Subscription Rate (Density Plot)
    -   Loan Status vs. Subscription Rate (Grouped Bar Chart)
-   **App Layout & Styling**:
    -   The app follows the two-column layout as proposed.
    -   Sidebar is consistent in design with appropriately labeled filters.
    -   The color scheme aligns with effective contrast and readability.
-   **Deployments**:
    -   The app has been successfully deployed on Render.
    -   PR deploy previews have been set up and tested.

### **Features Yet to Be Implemented**

-   Export Feature for High-Potential Clients: We originally planned to allow users to download a list of high-probability subscribers based on the selected filters. This has not been implemented yet but remains a priority for future milestones.
-   More Interactivity: Currently, all filters update the charts dynamically, but we plan to incorporate hover tooltips and clickable elements for deeper insights.
-   Additional Visualizations: While our dashboard includes a 2x2 grid of visualizations, we may explore alternative visual encodings (e.g., scatter plots, violin plots) to further enhance the insights.

------------------------------------------------------------------------

## **Deviations from Proposal**

Overall, we have stayed very close to our original proposal. However, some deviations were made due to practicality and usability improvements:

1.  Adjusted Job Type Filtering: Initially, we planned to reduce job categories on the front-end, but we instead preprocessed them into broader categories before filtering to optimize performance.
2.  Slider Tooltip Addition: The age slider now displays real-time values with a tooltip, which was not explicitly planned but was added to improve usability.
3.  Enhanced Styling: Some UI tweaks were made to improve readability, including dropdown font size, better contrast, and card spacing.

------------------------------------------------------------------------

## **Current Limitations & Future Improvements**

### **Limitations**

-   No Filter Reset Button: Currently, users have to manually reset filters to return to the default selection. This can be inconvenient, especially when multiple filters are adjusted.
-   UI Adjustments for Responsiveness: The app works well on full-screen desktop mode, but mobile optimization is still needed.
-   Performance with Large Data: Filtering large subsets takes a moment to update. We may need to optimize callbacks.

### **Future Enhancements**

-   Adding a Filter Reset Button: We plan to implement a reset button that allows users to quickly revert all filters to their default state. This will improve usability by making it easier to explore different filter combinations without manually resetting each one.
-   User Guide Section: Adding a brief guide within the app to help users understand the insights.
-   Drill-Down Interaction: Allow users to click on visual elements to refine selections dynamically.
-   Export Functionality: Generate CSVs of high-potential clients based on filtering criteria.


### Challenging Portion

-   As mentioned above, we managed to develop almost everything we had in our sketch.
-   If you now look at the sketch and the app, they are almost identical!
-   We have in total 4 plots, 4 filters, 5 summary statistics cards. 



## **Final Thoughts**

We are happy with the current progress of our Bank Marketing Analytics Dashboard. The app successfully allows marketing managers to analyze customer behaviors and campaign efficiency. The interactive filters and dynamic visualizations make it a practical tool for decision-making.

Moving forward, we will address minor issues, incorporate additional insights, and ensure that the final deployment meets our original goals while keeping the app fast, readable, and insightful.

------------------------------------------------------------------------
