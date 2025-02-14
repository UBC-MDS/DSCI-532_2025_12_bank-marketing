# Milestone 1 - Dashboard Proposal

Group Members: Hrayr Muradyan, Jia Quan Lim, Mason Zhang, Merari Santana

## I. Motivation and Purpose

Our Role: Data scientist at a financial institution

Target Audience: Marketing managers at a financial institution

As data scientists at a financial institution, our goal is to support marketing managers and supervisors in refining their telemarketing strategies for term deposits. The bank's current marketing campaigns rely on phone calls, but not all outreach efforts result in successful conversions. The challenge lies in identifying which client characteristics most strongly influence a customer’s decision to subscribe to a term deposit, allowing for more effective targeting and campaign optimization.

This problem is important to solve because inefficient targeting leads to wasted resources, unnecessary customer outreach, and lower overall success rates. Without data-driven decision-making, marketing managers may struggle to identify high-potential clients, leading to poor engagement strategies and reduced return on investment.

Our Bank Marketing Dashboard aims to address this problem by providing an interactive visualization tool that enables marketing managers to analyze the key factors influencing client decisions. Users will be able to explore variables such as age, job type, education level, and account balance to determine which customer segments are most likely to subscribe to a term deposit. With this information, marketing managers can refine their targeting strategy to segment clients based on conversion potential and tailor their outreach efforts to maximize campaign efficiency.

By leveraging this dashboard, marketing managers can identify trends, optimize call strategies, and ultimately improve subscription rates for term deposits. This will help the bank make data-driven decisions and enhance its overall marketing effectiveness.

## II. Description of the data

For this project, we are using the **Bank Marketing Dataset** from the UCI Machine Learning Repository. The dataset contains information about clients who were contacted as part of a **telemarketing campaign** conducted by a financial institution to promote term deposits. Our goal is to analyze key client characteristics that influence their decision to subscribe, allowing marketing managers to optimize their targeting strategies.

#### Dataset Overview

-   **Total Rows:** 45,211

-   **Total Columns:** 17

-   **Data Source:** [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)

#### Key Variables for Visualization

We will focus on the following key variables, which we hypothesize will help identify high-potential clients for term deposits:

1.  **Client Demographics:**

    -   `age`: Age of the client

    -   `job`: Occupation of the client (originally 12 categories; we plan to engineer into broader categories: *Employed, Unemployed, Unknown, Student, Retired*)

    -   `marital`: Marital status (*single, married, divorced*)

    -   `education`: Education level (*primary, secondary, tertiary, unknown*)

2.  **Financial Status:**

    -   `balance`: Client’s bank account balance

    -   `default`: Whether the client has credit in default (*yes/no*)

    -   `housing`: Whether the client has a housing loan (*yes/no*)

    -   `loan`: Whether the client has a personal loan (*yes/no*)

3.  **Marketing Campaign Information:**

    -   `contact`: Type of communication used (*cellular, telephone, unknown*)

    -   `month`: Last contact month

    -   `day`: Last contact day

    -   `duration`: Last call duration (seconds)

    -   `campaign`: Number of contacts performed during this campaign

    -   `pdays`: Days since the client was last contacted (if applicable)

    -   `previous`: Number of contacts performed before this campaign

    -   `poutcome`: Outcome of the previous campaign (*success, failure, nonexistent*)

4.  **Target Variable:**

    -   `y`: Whether the client subscribed to a term deposit (*yes/no*)

#### Data Engineering and New Variables

To enhance the analysis, we plan to derive the following new variables:

-   **Job Category (engineered from `job`)**: Reducing the original 12 job categories into 5 broader groups for easier visualization and interpretation.

-   **Age Groups (engineered from `age`)**: Grouping ages into categories (e.g., *18-25, 26-40, 41-60, 60+*) to understand how different age segments respond to marketing campaigns.

-   **Year Grouping for filtering**: Grouping data into their corresponding year (e.g., "2008-2010"). This will allow marketing managers to analyze trends over different periods and assess the impact of campaigns across years.

#### Justification for Dataset Choice

This dataset is well-suited for our project because it provides rich client-level information, enabling us to uncover patterns in successful marketing outreach. By leveraging interactive visualizations, marketing managers can:

-   Identify **which demographics are most likely to subscribe**.

-   Determine **optimal communication strategies** based on past interactions.

-   Refine **targeting strategies** to improve overall campaign efficiency and conversion rates.

#### Reference:

Moro, S., Laureano, R. M., & Cortez, P. (2014). UCI Bank Marketing Dataset [Data set]. UCI Machine Learning Repository. Retrieved from <https://archive.ics.uci.edu/dataset/222/bank+marketing>.

## III. Research questions and usage scenarios

Celeste, a marketing manager at a prestigious bank in Portugal, wants to determine which factors influence a client's decision to accept a term deposit offer. By identifying key indicators, she aims to refine the bank’s telemarketing strategy and target high-potential customers effectively.

When Celeste visits our “Bank Marketing Dashboard”, she will see an overview of her dataset and the 16 features related to client characteristics. She filters key variables such as “marital status”, "age", and "job type", to explore their impact on term deposit acceptance. For instance, she inspects the “loan” feature—whether the client has a personal loan or not—and notices a pattern: clients with personal loans are less likely to subscribe.

Using these insights, Celeste segments customers into high-, medium-, and low- potential groups and tailors telemarketing scripts accordingly. She then exports a refined list of high-potential clients to optimize her outreach strategy, increasing campaign efficiency and conversion rates.

## IV. App sketch & brief description

...
