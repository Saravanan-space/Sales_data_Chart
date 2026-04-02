import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Monitor", page_icon="📈", layout="wide")

# Reverting to default Streamlit theme (removing custom CSS injections)
# This ensures that text colors and backgrounds follow the user's system theme (Light/Dark)

def main():
    st.title("Business Sales Tracker")
    st.markdown("Detailed Business Performance Analysis & Reporting Dashboard")
    
    # 1. Sidebar Controls
    st.sidebar.header("Control Panel")
    uploaded_file = st.sidebar.file_uploader("Upload Sales CSV", type="csv")
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            df.columns = [c.strip().capitalize() for c in df.columns]
            
            # Data Formatting
            df['Date'] = pd.to_datetime(df['Date'])
            df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)
            df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
            df['Revenue'] = df['Quantity'] * df['Price']

            # 2. Custom Date Feature (in Sidebar)
            min_date, max_date = df['Date'].min(), df['Date'].max()
            st.sidebar.subheader("Date Filter")
            date_range = st.sidebar.date_input("Select Period", [min_date, max_date], min_value=min_date, max_value=max_date)
            
            if len(date_range) == 2:
                df = df[(df['Date'].dt.date >= date_range[0]) & (df['Date'].dt.date <= date_range[1])]

            # 3. Summary Metrics Row
            st.subheader("Key Performance Indicators")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Revenue", f"₹{df['Revenue'].sum():,.0f}")
            col2.metric("Total Items Sold", f"{int(df['Quantity'].sum()):,}")
            col3.metric("Average Sale Value", f"₹{df['Revenue'].mean():,.0f}")

            st.divider()

            # 4. Vertical Chart Layout (One below the other for mobile & professional feel)
            
            # Chart 1: Category Analysis
            st.subheader("Sales Distribution by Category")
            fig_pie = px.pie(df, values='Revenue', names='Category', hole=0.4, 
                           color_discrete_sequence=px.colors.qualitative.Safe)
            # Remove explicit color overrides to let Plotly adapt to the theme
            st.plotly_chart(fig_pie, use_container_width=True)

            # Chart 2: Time Trend
            st.subheader("Revenue Growth Trend")
            trend = df.groupby('Date')['Revenue'].sum().reset_index()
            fig_line = px.line(trend, x='Date', y='Revenue', markers=True)
            fig_line.update_traces(line_width=3)
            st.plotly_chart(fig_line, use_container_width=True)

            # Chart 3: Product Performance
            st.subheader("Top 5 Products by Revenue")
            top_prods = df.groupby('Product')['Revenue'].sum().nlargest(5).reset_index()
            fig_bar = px.bar(top_prods, x='Revenue', y='Product', orientation='h', 
                           color='Revenue', color_continuous_scale='Viridis')
            fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_bar, use_container_width=True)

            # Table: Transactions
            st.subheader("Detailed Transaction Logs")
            st.dataframe(df[['Date', 'Product', 'Category', 'Quantity', 'Revenue']].sort_values('Date', ascending=False).head(20), 
                         use_container_width=True)

        except Exception as e:
            st.error(f"Error Processing File: {e}")
    else:
        st.info("👋 Welcome! Please upload a CSV file to generate your dashboard. The file must include columns: Date, Product, Category, Quantity, Price.")
        
        # Test file generator
        sample = "Date,Product,Category,Quantity,Price\n2024-05-01,Smartphone,Electronics,2,45000\n2024-05-02,Headphones,Electronics,5,2500\n2024-05-03,Office Chair,Furniture,1,12000\n2024-05-04,Smartwatch,Electronics,3,15000\n2024-05-05,Coffee Mug,Home,10,450"
        st.download_button("📥 Download Sample CSV", sample, "sample_sales_data.csv")

if __name__ == "__main__":
    main()