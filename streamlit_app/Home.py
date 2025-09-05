import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# Try to import database, fallback if not available
try:
    from database import Database
    db = Database()
except ImportError:
    db = None

st.set_page_config(
    page_title="Rental Manager",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = {
        'id': 1,
        'username': 'demo_user',
        'email': 'demo@rentalmanager.com',
        'role': 'business_owner',
        'company_id': 1
    }

def dashboard_page():
    """Main dashboard page"""
    st.title(f"Welcome, {st.session_state.user['username']}!")
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"**Role:** {st.session_state.user['role'].title()}")
        st.markdown("---")
        
        # Quick stats
        st.subheader("Quick Stats")
        st.metric("Active Items", "24")
        st.metric("Total Bookings", "156")
        st.metric("Monthly Revenue", "€2,450")
        
        st.markdown("---")
        
        # Quick actions
        st.subheader("Quick Actions")
        if st.button("➕ Add New Item"):
            st.info("Navigate to Provider Management to add items")
        if st.button("📊 View Analytics"):
            st.info("Check the Analytics page for detailed insights")
        if st.button("📅 Check Calendar"):
            st.info("Visit the Calendar page for bookings")

    # Main content area
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Revenue",
            value="€12,450",
            delta="12.5%"
        )
    
    with col2:
        st.metric(
            label="Active Bookings",
            value="23",
            delta="3"
        )
    
    with col3:
        st.metric(
            label="Total Items",
            value="45",
            delta="2"
        )
    
    with col4:
        st.metric(
            label="Customer Rating",
            value="4.8/5",
            delta="0.1"
        )

    # Charts section
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue Trend")
        
        # Sample revenue data
        dates = pd.date_range(start='2025-01-01', end='2025-09-05', freq='D')
        revenue_data = pd.DataFrame({
            'date': dates,
            'revenue': [100 + i * 2 + (i % 7) * 50 for i in range(len(dates))]
        })
        
        fig_revenue = px.line(
            revenue_data, 
            x='date', 
            y='revenue',
            title="Daily Revenue"
        )
        fig_revenue.update_layout(height=400)
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        st.subheader("Booking Status")
        
        # Sample booking status data
        status_data = {
            'Status': ['Confirmed', 'Pending', 'Completed', 'Cancelled'],
            'Count': [45, 12, 89, 5]
        }
        
        fig_status = px.pie(
            values=status_data['Count'],
            names=status_data['Status'],
            title="Booking Distribution"
        )
        fig_status.update_layout(height=400)
        st.plotly_chart(fig_status, use_container_width=True)

    # Recent activity
    st.markdown("---")
    st.subheader("Recent Activity")
    
    activity_data = {
        'Time': ['2 hours ago', '5 hours ago', '1 day ago', '2 days ago', '3 days ago'],
        'Activity': [
            'New booking: Professional Camera',
            'Payment received: €125',
            'Item added: Power Drill',
            'Booking completed: Mountain Bike',
            'Customer review: 5 stars'
        ],
        'Type': ['Booking', 'Payment', 'Item', 'Booking', 'Review']
    }
    
    activity_df = pd.DataFrame(activity_data)
    
    for idx, row in activity_df.iterrows():
        col1, col2, col3 = st.columns([2, 4, 1])
        
        with col1:
            st.write(row['Time'])
        
        with col2:
            # Add emoji based on type
            emoji = {
                'Booking': '📅',
                'Payment': '💰',
                'Item': '📦',
                'Review': '⭐'
            }.get(row['Type'], '📋')
            
            st.write(f"{emoji} {row['Activity']}")
        
        with col3:
            type_color = {
                'Booking': '🟢',
                'Payment': '🟡',
                'Item': '🔵',
                'Review': '🟣'
            }.get(row['Type'], '⚪')
            
            st.write(type_color)

    # Performance overview
    st.markdown("---")
    st.subheader("Performance Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### This Month")
        st.metric("Bookings", "67", "+15%")
        st.metric("Revenue", "€3,240", "+22%")
        st.metric("New Customers", "12", "+8%")
    
    with col2:
        st.markdown("#### Top Items")
        top_items = pd.DataFrame({
            'Item': ['Professional Camera', 'Power Drill', 'Mountain Bike', 'Projector'],
            'Bookings': [23, 18, 15, 12],
            'Revenue': ['€1,150', '€720', '€900', '€480']
        })
        st.dataframe(top_items, use_container_width=True)
    
    with col3:
        st.markdown("#### Customer Satisfaction")
        st.metric("Average Rating", "4.8/5", "+0.2")
        st.metric("Response Time", "2.3 hours", "-0.5h")
        st.metric("Completion Rate", "96%", "+2%")

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 20px;'>
            <p><strong>Rental Manager</strong> - Professional Rental Management Platform</p>
            <p>Streamlit Backend • FastHTML Frontend • SQLite Database</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

def main():
    """Main application entry point"""
    dashboard_page()

if __name__ == "__main__":
    main()

