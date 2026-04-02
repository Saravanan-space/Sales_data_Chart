---

# 📊 Business Sales Tracker (Advanced Web Dashboard)

**One-Line Explanation:**
This application transforms raw business sales data into interactive dashboards using Python, enabling users to analyze performance, trends, and product insights efficiently.

---

## 🧾 1. Project Overview

### 📌 Title

**Business Sales Tracker**

### 🎯 Objective

To build an interactive web-based analytics dashboard that:

* Accepts sales data (CSV)
* Processes and cleans data
* Provides real-time insights
* Displays interactive visualizations

---

## 🧠 2. Core Concept

```
Data Input ➔ Data Cleaning ➔ Data Analysis ➔ Visualization ➔ Business Insights
```

---

## ⚙️ 3. Technology Stack

| Component       | Technology     | Role                     |
| --------------- | -------------- | ------------------------ |
| UI + Backend    | Streamlit      | Web app interface        |
| Data Processing | Pandas         | Data cleaning & analysis |
| Visualization   | Plotly Express | Interactive charts       |
| Language        | Python         | Core logic               |

---

## 🏗️ 4. Application Structure

The application is organized into the following logical sections:

* **Page Configuration** → Setting up the browser environment
* **Sidebar Controls** → Managing file uploads and date filters
* **Data Processing** → Cleaning and calculating financial metrics
* **KPI Metrics** → Displaying high-level business health
* **Visualizations** → Interactive charts for deep dives
* **Data Table** → Raw record access for verification

---

## 💻 5. Code Explanation (Step-by-Step)

### 🔹 1. Imports

We use:

* `pandas` for data processing
* `plotly.express` for visualization
* `streamlit` for the web interface

---

### 🔹 2. Page Configuration

`st.set_page_config()` sets the title, icon, and wide layout.

---

### 🔹 3. Main Logic

The `def main():` function encapsulates the entire application logic.

---

### 🔹 4. Sidebar (Control Panel)

Allows users to:

* Upload CSV files
* Select date ranges dynamically

---

### 🔄 5. Data Processing

* **Read File:**

  ```python
  pd.read_csv(uploaded_file)
  ```

* **Clean Column Names:**

  ```python
  df.columns = [c.strip().capitalize() for c in df.columns]
  ```

* **Convert Data Types:**

  * Dates → `pd.to_datetime()`
  * Numbers → `pd.to_numeric()`

* **Revenue Calculation:**

  ```python
  df['Revenue'] = df['Quantity'] * df['Price']
  ```

---

## 📊 6. KPI Metrics

Using `st.metric()` to display:

* **Total Revenue** → Overall earnings
* **Total Items Sold** → Total quantity sold
* **Average Sale Value** → Revenue per transaction

---

## 📈 7. Visualizations

* **Pie Chart**

  ```python
  px.pie(df, values='Revenue', names='Category')
  ```

  → Shows category-wise distribution

* **Line Chart**

  ```python
  df.groupby('Date')['Revenue'].sum()
  ```

  → Shows revenue trend over time

* **Bar Chart**

  ```python
  df.groupby('Product')['Revenue'].sum().nlargest(5)
  ```

  → Shows top-performing products

---

## 🎯 8. Key Features

* Interactive dashboard with real-time updates
* Sidebar controls for easy navigation
* Date range filtering for specific analysis
* KPI metrics with ₹ currency support
* Category and trend-based insights
* Sample dataset for testing

---

## 🚀 9. Advantages

* Real-world application (useful for businesses)
* Fully interactive (hover, zoom, filter)
* Clean and professional UI
* Works on both mobile and desktop
* Scalable for large datasets

---

## 🛠️ 10. How to Run

### Install dependencies:

```bash
pip install streamlit pandas plotly
```

### Run the app:

```bash
streamlit run app.py
```

---

## 📌 Note

Developed as part of the **Python Programming Mini Project**.

---

If you want:

* 🔥 Add **screenshots + GIF preview (makes GitHub look pro)**
* 📈 Add **badges (stars, version, tech stack)**
* 🌐 Help you **deploy it online (so you can share link in viva)**
