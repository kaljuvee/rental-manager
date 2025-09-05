import streamlit as st
import pandas as pd
from datetime import datetime, date
from database import RentsterDB

# Initialize database
@st.cache_resource
def init_database():
    return RentsterDB()

db = init_database()

# Page configuration
st.set_page_config(
    page_title="Rental Manager - Rental Platform",
    page_icon="🏢",
    layout="wide"
)
# Check if user session exists, if not create a default user
if 'user' not in st.session_state:
    st.session_state.user = {
        'id': 1,
        'username': 'demo_user',
        'email': 'demo@rentalmanager.com',
        'role': 'business_owner',
        'company_id': 1
    }
def main():
    """Main application - directly show dashboard"""
    dashboard_page()
        
        st.markdown("---")
        st.markdown("### Create New Account")
        
        with st.form("register_form"):
            reg_username = st.text_input("Username")
            reg_email = st.text_input("Email Address")
            reg_password = st.text_input("Password", type="password")
            reg_role = st.selectbox("Role", ["customer", "business_owner"])
            register = st.form_submit_button("Register")
            
            if register:
                if reg_username and reg_email and reg_password:
                    user_id = db.create_user(reg_username, reg_email, reg_password, reg_role)
                    if user_id:
                        st.success("Account created successfully! Please login.")
                    else:
                        st.error("Username or email already exists")
                else:
                    st.error("Please fill in all fields")

def dashboard():
    """Main dashboard"""
    st.title(f"Welcome, {st.session_state.user['username']}!")
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"**Role:** {st.session_state.user['role'].title()}")
        if st.button("Logout"):
            st.session_state.user = None
            st.rerun()
    
    # Main content based on role
    if st.session_state.user['role'] == 'business_owner':
        business_dashboard()
    else:
        customer_dashboard()

def business_dashboard():
    """Dashboard for business owners"""
    st.subheader("Business Dashboard")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📦 Rental Items", "📅 Bookings", "⚙️ Settings"])
    
    with tab1:
        # Overview metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Items", "12", "2")
        with col2:
            st.metric("Active Bookings", "8", "1")
        with col3:
            st.metric("Monthly Revenue", "€1,450", "€320")
        with col4:
            st.metric("Customer Satisfaction", "4.8/5", "0.2")
        
        # Revenue chart
        st.subheader("Revenue Overview")
        chart_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Revenue': [1200, 1350, 1100, 1450, 1600, 1450]
        })
        st.line_chart(chart_data.set_index('Month'))
    
    with tab2:
        st.subheader("Manage Rental Items")
        
        # Add new item form
        with st.expander("Add New Rental Item"):
            with st.form("add_item_form"):
                item_name = st.text_input("Item Name")
                item_description = st.text_area("Description")
                item_category = st.selectbox("Category", ["Electronics", "Tools", "Vehicles", "Equipment", "Other"])
                price_per_day = st.number_input("Price per Day (€)", min_value=0.0, step=0.01)
                submit_item = st.form_submit_button("Add Item")
                
                if submit_item and item_name and price_per_day > 0:
                    st.success(f"Item '{item_name}' added successfully!")
        
        # Display existing items
        items = db.get_rental_items(st.session_state.user.get('company_id'))
        if items:
            items_df = pd.DataFrame(items, columns=[
                'ID', 'Name', 'Description', 'Category', 'Company ID', 'Location ID',
                'Status', 'Price/Day', 'Image URL', 'Created', 'Company', 'Location'
            ])
            st.dataframe(items_df[['Name', 'Category', 'Status', 'Price/Day']], use_container_width=True)
        else:
            st.info("No rental items found. Add your first item above!")
    
    with tab3:
        st.subheader("Booking Management")
        
        bookings = db.get_bookings(company_id=st.session_state.user.get('company_id'))
        if bookings:
            bookings_df = pd.DataFrame(bookings, columns=[
                'Booking ID', 'Item ID', 'User ID', 'Start Date', 'End Date',
                'Total Price', 'Status', 'Created', 'Item Name', 'Username'
            ])
            st.dataframe(bookings_df[['Item Name', 'Username', 'Start Date', 'End Date', 'Total Price', 'Status']], 
                        use_container_width=True)
        else:
            st.info("No bookings found.")
    
    with tab4:
        st.subheader("Business Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Company Information")
            st.text_input("Company Name", value="Sample Company")
            st.text_input("Registration Code", value="12345678")
            st.text_input("Phone", value="+372 123 4567")
            st.text_area("Address", value="Sample Address")
        
        with col2:
            st.markdown("#### Subscription Plan")
            st.info("Current Plan: Business (€59/month)")
            st.markdown("- Max 10 Users")
            st.markdown("- Max 5 Locations")
            st.markdown("- 0% Transaction Fee")
            st.button("Upgrade Plan")

def customer_dashboard():
    """Dashboard for customers"""
    st.subheader("Customer Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["🔍 Browse Items", "📅 My Bookings", "👤 Profile"])
    
    with tab1:
        st.subheader("Available Rental Items")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            category_filter = st.selectbox("Category", ["All", "Electronics", "Tools", "Vehicles", "Equipment"])
        with col2:
            max_price = st.number_input("Max Price per Day (€)", min_value=0, value=100)
        with col3:
            availability = st.selectbox("Availability", ["Available", "All"])
        
        # Sample items (in real app, this would come from database)
        sample_items = [
            {"name": "Professional Camera", "category": "Electronics", "price": 25.0, "status": "available"},
            {"name": "Power Drill", "category": "Tools", "price": 15.0, "status": "available"},
            {"name": "Mountain Bike", "category": "Vehicles", "price": 20.0, "status": "rented"},
            {"name": "Projector", "category": "Electronics", "price": 30.0, "status": "available"},
        ]
        
        for item in sample_items:
            if (category_filter == "All" or item["category"] == category_filter) and \
               item["price"] <= max_price and \
               (availability == "All" or item["status"] == "available"):
                
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                    with col1:
                        st.write(f"**{item['name']}**")
                        st.write(f"Category: {item['category']}")
                    with col2:
                        st.write(f"€{item['price']}/day")
                    with col3:
                        status_color = "🟢" if item['status'] == 'available' else "🔴"
                        st.write(f"{status_color} {item['status'].title()}")
                    with col4:
                        if item['status'] == 'available':
                            if st.button(f"Book", key=f"book_{item['name']}"):
                                st.success(f"Booking request sent for {item['name']}")
                    st.divider()
    
    with tab2:
        st.subheader("My Bookings")
        
        bookings = db.get_bookings(user_id=st.session_state.user['user_id'])
        if bookings:
            bookings_df = pd.DataFrame(bookings, columns=[
                'Booking ID', 'Item ID', 'User ID', 'Start Date', 'End Date',
                'Total Price', 'Status', 'Created', 'Item Name', 'Username'
            ])
            st.dataframe(bookings_df[['Item Name', 'Start Date', 'End Date', 'Total Price', 'Status']], 
                        use_container_width=True)
        else:
            st.info("No bookings found. Browse items to make your first booking!")
    
    with tab3:
        st.subheader("Profile Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Username", value=st.session_state.user['username'])
            st.text_input("Email", value=st.session_state.user['email'])
        
        with col2:
            st.markdown("#### Account Statistics")
            st.metric("Total Bookings", "3")
            st.metric("Total Spent", "€245")
            st.metric("Member Since", "2024")

# Main app logic
def main():
    dashboard()

if __name__ == "__main__":
    main()

