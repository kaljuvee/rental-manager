import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")

# Check if user is logged in
if 'user' not in st.session_state or st.session_state.user is None:
    st.error("Please login first")
    st.stop()

st.title("📊 Analytics Dashboard")

# Generate sample data for demonstration
@st.cache_data
def generate_sample_data():
    # Revenue data
    dates = pd.date_range(start='2024-01-01', end='2024-09-05', freq='D')
    revenue_data = pd.DataFrame({
        'date': dates,
        'revenue': np.random.normal(50, 15, len(dates)).cumsum() + np.random.normal(0, 10, len(dates))
    })
    revenue_data['revenue'] = np.maximum(revenue_data['revenue'], 0)
    
    # Booking data
    booking_data = pd.DataFrame({
        'date': dates,
        'bookings': np.random.poisson(3, len(dates))
    })
    
    # Item category data
    categories = ['Electronics', 'Tools', 'Vehicles', 'Equipment', 'Other']
    category_data = pd.DataFrame({
        'category': categories,
        'bookings': np.random.randint(10, 100, len(categories)),
        'revenue': np.random.randint(500, 5000, len(categories))
    })
    
    return revenue_data, booking_data, category_data

revenue_data, booking_data, category_data = generate_sample_data()

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_revenue = revenue_data['revenue'].sum()
    st.metric("Total Revenue", f"€{total_revenue:,.0f}", "12.5%")

with col2:
    total_bookings = booking_data['bookings'].sum()
    st.metric("Total Bookings", f"{total_bookings:,}", "8.2%")

with col3:
    avg_booking_value = total_revenue / total_bookings if total_bookings > 0 else 0
    st.metric("Avg Booking Value", f"€{avg_booking_value:.2f}", "3.1%")

with col4:
    active_items = 45  # Sample number
    st.metric("Active Items", active_items, "2")

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue Trend")
    fig_revenue = px.line(revenue_data, x='date', y='revenue', 
                         title="Daily Revenue Over Time")
    fig_revenue.update_layout(height=400)
    st.plotly_chart(fig_revenue, use_container_width=True)

with col2:
    st.subheader("Bookings Trend")
    fig_bookings = px.bar(booking_data.tail(30), x='date', y='bookings',
                         title="Daily Bookings (Last 30 Days)")
    fig_bookings.update_layout(height=400)
    st.plotly_chart(fig_bookings, use_container_width=True)

# Category Analysis
st.subheader("Performance by Category")

col1, col2 = st.columns(2)

with col1:
    fig_cat_bookings = px.pie(category_data, values='bookings', names='category',
                             title="Bookings by Category")
    st.plotly_chart(fig_cat_bookings, use_container_width=True)

with col2:
    fig_cat_revenue = px.bar(category_data, x='category', y='revenue',
                            title="Revenue by Category")
    st.plotly_chart(fig_cat_revenue, use_container_width=True)

# Detailed Analytics
st.subheader("Detailed Analytics")

tab1, tab2, tab3 = st.tabs(["📈 Growth Metrics", "🎯 Performance", "📋 Reports"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Monthly Growth")
        monthly_data = revenue_data.groupby(revenue_data['date'].dt.to_period('M')).agg({
            'revenue': 'sum'
        }).reset_index()
        monthly_data['date'] = monthly_data['date'].astype(str)
        
        fig_monthly = px.bar(monthly_data, x='date', y='revenue',
                           title="Monthly Revenue Growth")
        st.plotly_chart(fig_monthly, use_container_width=True)
    
    with col2:
        st.markdown("#### Key Performance Indicators")
        
        # Calculate some KPIs
        current_month_revenue = revenue_data[revenue_data['date'].dt.month == 9]['revenue'].sum()
        previous_month_revenue = revenue_data[revenue_data['date'].dt.month == 8]['revenue'].sum()
        growth_rate = ((current_month_revenue - previous_month_revenue) / previous_month_revenue * 100) if previous_month_revenue > 0 else 0
        
        st.metric("Monthly Growth Rate", f"{growth_rate:.1f}%")
        st.metric("Customer Retention", "87.3%")
        st.metric("Average Session Duration", "12.5 min")
        st.metric("Conversion Rate", "4.2%")

with tab2:
    st.markdown("#### Top Performing Items")
    
    # Sample top items data
    top_items = pd.DataFrame({
        'Item': ['Professional Camera', 'Power Drill Set', 'Mountain Bike', 'Projector', 'Laptop'],
        'Bookings': [45, 38, 32, 28, 25],
        'Revenue': [1125, 570, 640, 840, 750],
        'Rating': [4.8, 4.6, 4.9, 4.5, 4.7]
    })
    
    st.dataframe(top_items, use_container_width=True)
    
    # Performance heatmap
    st.markdown("#### Performance Heatmap")
    
    # Generate sample heatmap data
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    hours = list(range(8, 22))  # 8 AM to 9 PM
    
    heatmap_data = np.random.randint(0, 20, size=(len(hours), len(days)))
    
    fig_heatmap = px.imshow(heatmap_data, 
                           x=days, 
                           y=hours,
                           title="Booking Activity Heatmap",
                           labels=dict(x="Day of Week", y="Hour of Day", color="Bookings"))
    st.plotly_chart(fig_heatmap, use_container_width=True)

with tab3:
    st.markdown("#### Generate Reports")
    
    col1, col2 = st.columns(2)
    
    with col1:
        report_type = st.selectbox("Report Type", 
                                  ["Revenue Report", "Booking Report", "Customer Report", "Item Performance"])
        date_range = st.date_input("Date Range", 
                                  value=[datetime.now() - timedelta(days=30), datetime.now()],
                                  max_value=datetime.now())
    
    with col2:
        format_type = st.selectbox("Format", ["PDF", "Excel", "CSV"])
        include_charts = st.checkbox("Include Charts", value=True)
        
        if st.button("Generate Report"):
            st.success(f"Generated {report_type} in {format_type} format!")
            st.info("Report would be available for download in a real implementation.")

# Footer
st.divider()
st.markdown("*Analytics data is updated in real-time. Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "*")

