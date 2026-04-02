📊 Business Sales Tracker (Advanced Web Dashboard)
One-Line Explanation: This application transforms raw business sales data into interactive dashboards using Python, enabling users to analyze performance, trends, and product insights efficiently.
🧾 1. Project Overview
📌 Title: Business Sales Tracker
🎯 Objective: To build an interactive web-based analytics dashboard that:
Accepts sales data (CSV)
Processes and cleans data
Provides real-time insights
Displays interactive visualizations
🧠 2. Core Concept
Data Input ➔ Data Cleaning ➔ Data Analysis ➔ Visualization ➔ Business Insights
⚙️ 3. Technology Stack
Component
Technology
Role
UI + Backend
Streamlit
Web app interface
Data Processing
Pandas
Data cleaning & analysis
Visualization
Plotly Express
Interactive charts
Language
Python
Core logic

🏗️ 4. Application Structure
The application is organized into the following logical sections:
Page Configuration: Setting up the browser environment.
Sidebar Controls: Managing file uploads and date filters.
Data Processing: Cleaning and calculating financial metrics.
KPI Metrics: Displaying high-level business health.
Visualizations: Interactive charts for deep dives.
Data Table: Raw record access for verification.
💻 5. Code Explanation (Step-by-Step)
🔹 1. Imports
We use pandas for data math, plotly.express for charts, and streamlit for the website.
🔹 2. Page Configuration
st.set_page_config sets the title, icon, and forces a wide-screen layout.
🔹 3. Main Logic
The def main(): function encapsulates the app logic.
🔹 4. Sidebar (Control Panel)
Allows users to upload their CSV files and select date ranges dynamically.
🔄 5. Data Processing
Read File: pd.read_csv(uploaded_file)
Clean Names: df.columns = [c.strip().capitalize() for c in df.columns]
Convert Types: Dates and numeric values are standardized using pd.to_datetime and pd.to_numeric.
Revenue Calculation: df['Revenue'] = df['Quantity'] * df['Price']
📊 6. KPI Metrics
Using st.metric() to display:
Total Revenue: Overall earnings.
Total Items Sold: Total quantity moved.
Avg Sale Value: Revenue per transaction.
📈 7. Visualizations
Pie Chart: px.pie(df, values='Revenue', names='Category') for category share.
Line Chart: df.groupby('Date')['Revenue'].sum() to track trends over time.
Bar Chart: df.groupby('Product')['Revenue'].sum().nlargest(5) for top product insights.
🎯 6. Key Features
Interactive dashboard with real-time updates.
Sidebar controls for easy navigation.
Date range filtering for specific period analysis.
KPI metrics with local currency (₹) support.
Comprehensive trend and category analysis.
Sample file feature for immediate testing.
🚀 7. Advantages
Real-world application: Ready for use by small businesses.
Interactive: Users can hover, zoom, and filter data instantly.
Professional UI: Clean, modern design optimized for mobile and desktop.
Scalable: Can handle thousands of rows of data efficiently.
🛠️ 8. How to Run
Install requirements: pip install streamlit pandas plotly
Run the app: streamlit run app.py
Developed as part of the Python Programming Mini Project.
