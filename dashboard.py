import time
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Load the test data
@st.cache_data
def load_data():
    return pd.read_csv('web_server_logs.csv')

# Generate the dashboard
def main():
    st.set_page_config(page_title="Sales and Marketing Dashboard", layout="wide")
    st.title("Sales and Marketing Dashboard")

    # Load data
    df = load_data()

    # Sidebar for filtering
    st.sidebar.header("Filter Options")
    country_filter = st.sidebar.multiselect("Select Country", options=df['Country'].unique())
    job_filter = st.sidebar.multiselect("Select Job Type", options=df['Job Requested'].unique())
    demo_request_filter = st.sidebar.multiselect("Demo Request", options=df['Demo Request'].unique())
    payment_method_filter = st.sidebar.multiselect("Payment Method", options=df['Payment Method'].unique())

    # Apply filters
    if country_filter:
        df = df[df['Country'].isin(country_filter)]
    if job_filter:
        df = df[df['Job Requested'].isin(job_filter)]
    if demo_request_filter:
        df = df[df['Demo Request'].isin(demo_request_filter)]
    if payment_method_filter:
        df = df[df['Payment Method'].isin(payment_method_filter)]


    # Creating a single-element container for real-time updates
    placeholder = st.empty()

    # Near real-time / live feed simulation
    for seconds in range(200):
        # Simulate new data
        df["Jobs Placed"] = df["Jobs Placed"] + np.random.choice(range(1, 5))
        df["Satisfaction Rating"] = df["Satisfaction Rating"] + np.random.choice(range(1, 5))

        # Calculate KPIs
        total_requests = len(df)
        total_jobs_placed = df['Jobs Placed'].sum()
        unique_countries = df['Country'].nunique()
        avg_satisfaction = df['Satisfaction Rating'].mean()
        total_sales_revenue = df['Sales Revenue'].sum()

        with placeholder.container():
            # Create three columns for KPIs
            kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

            # Display KPIs
            kpi1.metric(label="Total Requests", value=total_requests)
            kpi2.metric(label="Total Jobs Placed", value=total_jobs_placed)
            kpi3.metric(label="Unique Countries", value=unique_countries)
            kpi4.metric(label="Average Satisfaction Rating", value=round(avg_satisfaction, 2))
            kpi5.metric(label="Total Sales Revenue", value=f"${total_sales_revenue:,.2f}")

            # Create two columns for charts
            fig_col1, fig_col2,fig_col3 = st.columns(3)

            with fig_col1:
                st.subheader("Jobs Placed by Country")
                fig1 = px.bar(df, x='Country', y='Jobs Placed', title='Jobs Placed by Country', color='Country')
                st.plotly_chart(fig1, key=f"JPC_{seconds}")

            with fig_col2:
                st.subheader("Satisfaction Rating Distribution")
                fig2 = px.histogram(df, x='Satisfaction Rating',y='Job Requested', title='Satisfaction Rating Distribution')
                st.plotly_chart(fig2, key=f"SRJB_{seconds}")
            
            with fig_col3:
                st.subheader("Sales Revenue by Payment Method")
                fig3 = px.pie(df, names='Payment Method', values='Sales Revenue', title='Sales Revenue by Payment Method')
                st.plotly_chart(fig3,key=f"SRPM_{seconds}")

            # Summary statistics
            st.subheader("Summary Statistics")
            summary_stats = df[['Jobs Placed', 'Satisfaction Rating', 'Sales Revenue']].agg(['mean', 'std', 'min', 'max'])
            st.dataframe(summary_stats)

        time.sleep(1)  # Delay for real-time simulation

    # Export functionality
    st.subheader("Export Data")
    if st.button("Export to Excel"):
        df.to_excel("exported_data.xlsx", index=False)
        st.success("Data exported successfully!")

if __name__ == "__main__":
    main()