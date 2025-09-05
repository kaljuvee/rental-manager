import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os

# Add the parent directory to the path to import database
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

try:
    from database import Database
    # Initialize database
    db = Database()
except ImportError:
    # Fallback if database module is not available
    db = None

st.set_page_config(
    page_title="Provider Management - Rental Manager",
    page_icon="🏪",
    layout="wide"
)

st.title("🏪 Provider Management")

# Check if user session exists
if 'user' not in st.session_state:
    st.session_state.user = {
        'id': 1,
        'username': 'demo_user',
        'email': 'demo@rentalmanager.com',
        'role': 'business_owner',
        'company_id': 1
    }

# Sidebar for provider actions
st.sidebar.header("Provider Actions")
action = st.sidebar.selectbox(
    "Choose Action",
    ["Dashboard", "Add New Item", "Manage Items", "Bookings", "Analytics", "Settings"]
)

if action == "Dashboard":
    st.header("Provider Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Items", "24", "+3")
    
    with col2:
        st.metric("Active Bookings", "8", "+2")
    
    with col3:
        st.metric("Monthly Revenue", "€1,245", "+15%")
    
    with col4:
        st.metric("Avg Rating", "4.8", "+0.2")
    
    # Recent activity
    st.subheader("Recent Activity")
    
    activity_data = {
        'Time': ['2 hours ago', '5 hours ago', '1 day ago', '2 days ago'],
        'Activity': [
            'New booking: MacBook Pro 15',
            'Item added: Wireless Projector',
            'Booking completed: Toyota Prius',
            'Payment received: €127'
        ],
        'Status': ['New', 'Added', 'Completed', 'Paid']
    }
    
    st.dataframe(pd.DataFrame(activity_data), use_container_width=True)

elif action == "Add New Item":
    st.header("Add New Rental Item")
    
    with st.form("add_item_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            item_name = st.text_input("Item Name*")
            category = st.selectbox("Category*", [
                "Presentation tech", "Conference tech", "Sound/Audio",
                "Photography equipment", "Vehicles", "Desktop computers",
                "Laptops", "Tools", "Lighting", "Camping", "Party",
                "Light vehicles", "Rooms", "Trailers", "Water sports",
                "Software", "Heavy machinery", "Containers",
                "Children's supplies", "Garden tools", "Cleaning equipment",
                "Air-conditioning equipment", "Sport", "Ports",
                "Outdoor toilets", "Parking spaces"
            ])
            
            # Pricing
            st.subheader("Pricing")
            hourly_price = st.number_input("Hourly Price (€)", min_value=0.0, step=0.1)
            daily_price = st.number_input("Daily Price (€)", min_value=0.0, step=0.1)
            monthly_price = st.number_input("Monthly Price (€)", min_value=0.0, step=0.1)
            
        with col2:
            description = st.text_area("Description*", height=100)
            location = st.text_input("Location*")
            
            # Features
            st.subheader("Features")
            contactless = st.checkbox("Contactless rental available")
            available_24_7 = st.checkbox("24/7 availability")
            
            # Availability
            st.subheader("Availability")
            min_rental_period = st.selectbox("Minimum rental period", 
                ["1 hour", "2 hours", "4 hours", "1 day", "1 week"])
            
        # Images
        st.subheader("Images")
        uploaded_files = st.file_uploader(
            "Upload item images", 
            accept_multiple_files=True,
            type=['png', 'jpg', 'jpeg']
        )
        
        submitted = st.form_submit_button("Add Item")
        
        if submitted:
            if item_name and category and description and location:
                st.success(f"Item '{item_name}' added successfully!")
                st.balloons()
            else:
                st.error("Please fill in all required fields marked with *")

elif action == "Manage Items":
    st.header("Manage Your Items")
    
    # Search and filter
    col1, col2, col3 = st.columns(3)
    with col1:
        search_term = st.text_input("Search items...")
    with col2:
        filter_category = st.selectbox("Filter by category", ["All"] + [
            "Presentation tech", "Vehicles", "Laptops", "Tools", "Photography equipment"
        ])
    with col3:
        filter_status = st.selectbox("Filter by status", ["All", "Active", "Inactive", "Rented"])
    
    # Sample items data
    items_data = {
        'Item Name': ['MacBook Pro 15', 'Toyota Prius', 'Wireless Projector', 'Professional Camera'],
        'Category': ['Laptops', 'Vehicles', 'Presentation tech', 'Photography equipment'],
        'Hourly Price': ['€5.00', '€12.00', '€3.17', '€8.00'],
        'Daily Price': ['€35.00', '€85.00', '€25.00', '€60.00'],
        'Status': ['Active', 'Rented', 'Active', 'Active'],
        'Bookings': [12, 8, 15, 6],
        'Rating': [4.8, 4.9, 4.7, 4.6]
    }
    
    df = pd.DataFrame(items_data)
    
    # Display items with action buttons
    for idx, row in df.iterrows():
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([3, 2, 1, 1, 1])
            
            with col1:
                st.write(f"**{row['Item Name']}**")
                st.write(f"Category: {row['Category']}")
            
            with col2:
                st.write(f"Hourly: {row['Hourly Price']}")
                st.write(f"Daily: {row['Daily Price']}")
            
            with col3:
                status_color = "🟢" if row['Status'] == 'Active' else "🔴" if row['Status'] == 'Rented' else "🟡"
                st.write(f"{status_color} {row['Status']}")
            
            with col4:
                st.write(f"⭐ {row['Rating']}")
                st.write(f"📅 {row['Bookings']} bookings")
            
            with col5:
                if st.button("Edit", key=f"edit_{idx}"):
                    st.info(f"Editing {row['Item Name']}")
                if st.button("Delete", key=f"delete_{idx}"):
                    st.warning(f"Delete {row['Item Name']}?")
            
            st.divider()

elif action == "Bookings":
    st.header("Booking Management")
    
    # Booking status tabs
    tab1, tab2, tab3, tab4 = st.tabs(["All Bookings", "Pending", "Active", "Completed"])
    
    with tab1:
        # Sample booking data
        bookings_data = {
            'Booking ID': ['#001', '#002', '#003', '#004'],
            'Item': ['MacBook Pro 15', 'Toyota Prius', 'Wireless Projector', 'Professional Camera'],
            'Customer': ['John Doe', 'Jane Smith', 'Mike Johnson', 'Sarah Wilson'],
            'Start Date': ['2025-09-06', '2025-09-07', '2025-09-08', '2025-09-09'],
            'End Date': ['2025-09-08', '2025-09-10', '2025-09-08', '2025-09-11'],
            'Total': ['€70.00', '€255.00', '€25.00', '€180.00'],
            'Status': ['Active', 'Pending', 'Completed', 'Active']
        }
        
        df_bookings = pd.DataFrame(bookings_data)
        st.dataframe(df_bookings, use_container_width=True)
    
    with tab2:
        st.info("Pending bookings require your approval")
        # Filter for pending bookings
        pending_bookings = df_bookings[df_bookings['Status'] == 'Pending']
        if not pending_bookings.empty:
            for idx, booking in pending_bookings.iterrows():
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.write(f"**{booking['Item']}** - {booking['Customer']}")
                        st.write(f"{booking['Start Date']} to {booking['End Date']} - {booking['Total']}")
                    with col2:
                        if st.button("Approve", key=f"approve_{idx}"):
                            st.success("Booking approved!")
                    with col3:
                        if st.button("Decline", key=f"decline_{idx}"):
                            st.error("Booking declined!")
        else:
            st.write("No pending bookings")

elif action == "Analytics":
    st.header("Provider Analytics")
    
    # Revenue chart
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Monthly Revenue")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        revenue = [800, 950, 1100, 1200, 1150, 1245]
        
        fig = px.line(x=months, y=revenue, title="Revenue Trend")
        fig.update_layout(xaxis_title="Month", yaxis_title="Revenue (€)")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Item Performance")
        items = ['MacBook Pro', 'Toyota Prius', 'Projector', 'Camera']
        bookings = [12, 8, 15, 6]
        
        fig = px.bar(x=items, y=bookings, title="Bookings by Item")
        fig.update_layout(xaxis_title="Items", yaxis_title="Number of Bookings")
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed analytics
    st.subheader("Detailed Analytics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Average Booking Value", "€89.50", "+12%")
        st.metric("Booking Conversion Rate", "23%", "+3%")
    
    with col2:
        st.metric("Customer Retention", "67%", "+8%")
        st.metric("Average Rating", "4.8/5", "+0.1")
    
    with col3:
        st.metric("Response Time", "2.3 hours", "-0.5h")
        st.metric("Cancellation Rate", "5%", "-2%")

elif action == "Settings":
    st.header("Provider Settings")
    
    tab1, tab2, tab3 = st.tabs(["Business Info", "Locations", "Notifications"])
    
    with tab1:
        st.subheader("Business Information")
        
        with st.form("business_info"):
            business_name = st.text_input("Business Name", value="Nutirent")
            business_email = st.text_input("Business Email", value="info@nutirent.ee")
            business_phone = st.text_input("Phone Number", value="+372 123 4567")
            business_description = st.text_area("Business Description", 
                value="Professional rental services for tech equipment and vehicles")
            
            # Business hours
            st.subheader("Business Hours")
            col1, col2 = st.columns(2)
            with col1:
                open_time = st.time_input("Opening Time")
            with col2:
                close_time = st.time_input("Closing Time")
            
            if st.form_submit_button("Update Business Info"):
                st.success("Business information updated!")
    
    with tab2:
        st.subheader("Business Locations")
        
        # Add new location
        with st.expander("Add New Location"):
            location_name = st.text_input("Location Name")
            address = st.text_input("Address")
            city = st.selectbox("City", ["Tallinn", "Tartu", "Pärnu", "Narva"])
            
            if st.button("Add Location"):
                st.success(f"Location '{location_name}' added!")
        
        # Existing locations
        st.subheader("Current Locations")
        locations_data = {
            'Name': ['Main Office', 'Warehouse'],
            'Address': ['Keemia 4, Kristiine', 'Peterburi tee 46'],
            'City': ['Tallinn', 'Tallinn'],
            'Active': [True, True]
        }
        
        df_locations = pd.DataFrame(locations_data)
        st.dataframe(df_locations, use_container_width=True)
    
    with tab3:
        st.subheader("Notification Settings")
        
        st.checkbox("Email notifications for new bookings", value=True)
        st.checkbox("SMS notifications for urgent matters", value=False)
        st.checkbox("Weekly analytics reports", value=True)
        st.checkbox("Customer review notifications", value=True)
        
        if st.button("Save Notification Settings"):
            st.success("Notification settings saved!")

# Footer
st.markdown("---")
st.markdown("**Rental Manager** - Provider Management System")

