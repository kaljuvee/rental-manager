import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta, date
import calendar

st.set_page_config(page_title="Calendar", page_icon="📅", layout="wide")

# Check if user is logged in
if 'user' not in st.session_state or st.session_state.user is None:
    st.error("Please login first")
    st.stop()

st.title("📅 Rental Calendar")

# Calendar view selector
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    view_type = st.selectbox("Calendar View", ["Month", "Week", "Day"])

with col2:
    selected_date = st.date_input("Select Date", value=datetime.now().date())

with col3:
    if st.button("Today"):
        selected_date = datetime.now().date()
        st.rerun()

# Generate sample booking data
@st.cache_data
def generate_calendar_data():
    # Generate sample bookings for the current month
    start_date = datetime.now().replace(day=1)
    end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    bookings = []
    items = ['Professional Camera', 'Power Drill', 'Mountain Bike', 'Projector', 'Laptop']
    
    current = start_date
    while current <= end_date:
        # Random number of bookings per day (0-5)
        num_bookings = max(0, int(np.random.normal(2, 1)))
        
        for i in range(num_bookings):
            booking = {
                'date': current.date(),
                'item': np.random.choice(items),
                'customer': f"Customer {np.random.randint(1, 100)}",
                'start_time': f"{np.random.randint(8, 18):02d}:00",
                'duration': np.random.choice([1, 2, 3, 7, 14]),  # days
                'status': np.random.choice(['confirmed', 'pending', 'completed'], p=[0.6, 0.2, 0.2])
            }
            bookings.append(booking)
        
        current += timedelta(days=1)
    
    return pd.DataFrame(bookings)

import numpy as np
bookings_df = generate_calendar_data()

if view_type == "Month":
    st.subheader(f"Month View - {selected_date.strftime('%B %Y')}")
    
    # Create month calendar
    year = selected_date.year
    month = selected_date.month
    
    # Get calendar data
    cal = calendar.monthcalendar(year, month)
    
    # Convert date column to datetime for filtering
    bookings_df['date'] = pd.to_datetime(bookings_df['date'])
    
    month_bookings = bookings_df[
        (bookings_df['date'].dt.year == year) & 
        (bookings_df['date'].dt.month == month)
    ]
    
    # Create calendar grid
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Display calendar header
    cols = st.columns(7)
    for i, day in enumerate(days):
        cols[i].markdown(f"**{day}**")
    
    # Display calendar days
    for week in cal:
        cols = st.columns(7)
        for i, day in enumerate(week):
            if day == 0:
                cols[i].markdown("")
            else:
                day_date = date(year, month, day)
                day_bookings = month_bookings[month_bookings['date'].dt.date == day_date]
                
                with cols[i]:
                    # Highlight today
                    if day_date == datetime.now().date():
                        st.markdown(f"**🔵 {day}**")
                    else:
                        st.markdown(f"**{day}**")
                    
                    # Show bookings for this day
                    if len(day_bookings) > 0:
                        st.markdown(f"📅 {len(day_bookings)} booking(s)")
                        for _, booking in day_bookings.head(2).iterrows():  # Show max 2
                            status_emoji = "✅" if booking['status'] == 'confirmed' else "⏳" if booking['status'] == 'pending' else "✔️"
                            st.markdown(f"{status_emoji} {booking['item'][:15]}...")
                        if len(day_bookings) > 2:
                            st.markdown(f"... +{len(day_bookings) - 2} more")

elif view_type == "Week":
    st.subheader(f"Week View - Week of {selected_date.strftime('%B %d, %Y')}")
    
    # Calculate week start (Monday)
    week_start = selected_date - timedelta(days=selected_date.weekday())
    week_dates = [week_start + timedelta(days=i) for i in range(7)]
    
    # Filter bookings for this week
    week_bookings = bookings_df[
        (bookings_df['date'].dt.date >= week_start) & 
        (bookings_df['date'].dt.date < week_start + timedelta(days=7))
    ]
    
    # Create week view
    cols = st.columns(7)
    for i, day_date in enumerate(week_dates):
        day_bookings = week_bookings[week_bookings['date'].dt.date == day_date]
        
        with cols[i]:
            # Highlight today
            if day_date == datetime.now().date():
                st.markdown(f"**🔵 {day_date.strftime('%a %d')}**")
            else:
                st.markdown(f"**{day_date.strftime('%a %d')}**")
            
            # Show all bookings for this day
            for _, booking in day_bookings.iterrows():
                status_color = "🟢" if booking['status'] == 'confirmed' else "🟡" if booking['status'] == 'pending' else "🔵"
                st.markdown(f"{status_color} **{booking['start_time']}**")
                st.markdown(f"📦 {booking['item']}")
                st.markdown(f"👤 {booking['customer']}")
                st.markdown("---")

else:  # Day view
    st.subheader(f"Day View - {selected_date.strftime('%A, %B %d, %Y')}")
    
    # Filter bookings for selected day
    day_bookings = bookings_df[bookings_df['date'].dt.date == selected_date]
    
    if len(day_bookings) > 0:
        # Create timeline view
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("#### Time Slots")
            for hour in range(8, 20):  # 8 AM to 8 PM
                st.markdown(f"**{hour:02d}:00**")
                st.markdown("---")
        
        with col2:
            st.markdown("#### Bookings")
            for _, booking in day_bookings.iterrows():
                status_color = "🟢" if booking['status'] == 'confirmed' else "🟡" if booking['status'] == 'pending' else "🔵"
                
                with st.container():
                    st.markdown(f"{status_color} **{booking['start_time']} - {booking['item']}**")
                    st.markdown(f"👤 Customer: {booking['customer']}")
                    st.markdown(f"⏱️ Duration: {booking['duration']} day(s)")
                    st.markdown(f"📊 Status: {booking['status'].title()}")
                    
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        if st.button(f"Edit", key=f"edit_{booking.name}"):
                            st.info("Edit functionality would open here")
                    with col_b:
                        if st.button(f"Contact", key=f"contact_{booking.name}"):
                            st.info("Contact customer functionality")
                    with col_c:
                        if booking['status'] == 'pending':
                            if st.button(f"Confirm", key=f"confirm_{booking.name}"):
                                st.success("Booking confirmed!")
                    
                    st.markdown("---")
    else:
        st.info("No bookings for this day.")

# Sidebar - Quick Actions
with st.sidebar:
    st.markdown("### Quick Actions")
    
    if st.button("➕ New Booking"):
        st.info("New booking form would open here")
    
    if st.button("📊 View Analytics"):
        st.info("Navigate to Analytics page")
    
    if st.button("📋 Export Calendar"):
        st.info("Calendar export functionality")
    
    st.markdown("---")
    
    st.markdown("### Calendar Statistics")
    total_bookings = len(bookings_df)
    confirmed_bookings = len(bookings_df[bookings_df['status'] == 'confirmed'])
    pending_bookings = len(bookings_df[bookings_df['status'] == 'pending'])
    
    st.metric("Total Bookings", total_bookings)
    st.metric("Confirmed", confirmed_bookings)
    st.metric("Pending", pending_bookings)
    
    # Booking status chart
    status_data = bookings_df['status'].value_counts()
    fig_status = px.pie(values=status_data.values, names=status_data.index, 
                       title="Booking Status Distribution")
    fig_status.update_layout(height=300)
    st.plotly_chart(fig_status, use_container_width=True)

# Bottom section - Upcoming bookings
st.markdown("---")
st.subheader("Upcoming Bookings")

upcoming_bookings = bookings_df[
    (bookings_df['date'].dt.date >= datetime.now().date()) & 
    (bookings_df['status'].isin(['confirmed', 'pending']))
].head(10)

if len(upcoming_bookings) > 0:
    for _, booking in upcoming_bookings.iterrows():
        col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, 1])
        
        with col1:
            st.write(f"**{booking['item']}**")
        with col2:
            st.write(f"👤 {booking['customer']}")
        with col3:
            st.write(f"📅 {booking['date']}")
        with col4:
            status_emoji = "✅" if booking['status'] == 'confirmed' else "⏳"
            st.write(f"{status_emoji} {booking['status'].title()}")
        with col5:
            if st.button("View", key=f"view_{booking.name}"):
                st.info("Booking details would open here")
else:
    st.info("No upcoming bookings found.")

