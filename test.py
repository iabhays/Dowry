#This is only for Fun and Learning purpose.

import streamlit as st

# Function to calculate dowry based on different factors
def calculate_dowry(salary, property_value, job_type, caste, region, state, city):
    dowry = 0

    # Base dowry calculation using salary and property value
    dowry += (salary * 0.2) + (property_value * 0.05)

    # Job type influence
    if job_type == "Government":
        dowry += 50000  # Government jobs contribute more to dowry
    else:
        dowry += 30000  # Private jobs contribute less

    # Caste influence (Higher caste may lead to higher dowry)
    if caste == "General":
        dowry += 30000
    elif caste == "OBC":
        dowry += 20000
    elif caste == "SC":
        dowry += 10000
    else:
        dowry += 15000  # For ST caste

    # Region influence (Urban areas tend to have higher dowry amounts)
    if region == "Urban":
        dowry += 25000
    else:
        dowry += 10000

    # State influence (Major states like Delhi, Maharashtra, UP lead to higher dowry)
    if state in ["Delhi", "Maharashtra", "Uttar Pradesh", "Karnataka", "Tamil Nadu"]:
        dowry += 40000
    else:
        dowry += 20000

    # City influence (Big cities contribute more to dowry)
    big_cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']
    if city in big_cities:
        dowry += 50000
    else:
        dowry += 20000

    return dowry

# Function to assign car, bike, and flat based on dowry amount
def assign_assets(dowry):
    # Car selection based on dowry amount
    if dowry < 250000:
        car = "Tata Nano (Budget Car)"
        bike = "Hero Splendor (Budget Bike)"
        flat = "1BHK (Smaller Flat)"
    elif dowry < 500000:
        car = "Maruti Swift (Mid-Range Car)"
        bike = "Honda CB Shine (Standard Bike)"
        flat = "2BHK (Mid-Range Flat)"
    elif dowry < 750000:
        car = "Honda City (Premium Car)"
        bike = "Yamaha R15 (Sports Bike)"
        flat = "3BHK (Spacious Flat)"
    else:
        car = "BMW 3 Series (Luxury Car)"
        bike = "Harley Davidson (Superbike)"
        flat = "Luxury Flat (High-End Flat)"

    return car, bike, flat

# Streamlit UI
def main():
    st.title("Dowry Prediction System")

    # Input fields with clear labels and no pre-filled values
    salary = st.number_input("Enter your Salary (in ₹)", min_value=10000, max_value=1000000)
    property_value = st.number_input("Enter Property Value (in ₹)", min_value=100000, max_value=10000000)
    job_type = st.selectbox("Select Job Type", ["Government", "Private"])
    caste = st.selectbox("Select Caste", ["General", "OBC", "SC", "ST"])
    region = st.selectbox("Select Region", ["Urban", "Rural"])
    state = st.selectbox("Select State", [
        "Delhi", "Maharashtra", "Uttar Pradesh", "Karnataka", "Tamil Nadu", "Bihar", "UP", "West Bengal", "Rajasthan", 
        "Gujarat", "Kerala", "Telangana", "Madhya Pradesh", "Andhra Pradesh", "Haryana", "Punjab", "Odisha", "Uttarakhand", 
        "Chhattisgarh", "Bihar", "Jharkhand", "Assam", "Himachal Pradesh", "Goa", "Jammu and Kashmir", "Sikkim", 
        "Arunachal Pradesh", "Nagaland", "Manipur", "Mizoram", "Tripura", "Meghalaya", "Andaman and Nicobar Islands", 
        "Lakshadweep", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu"
    ])
    city = st.selectbox("Select City", ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad', 'Surat', 
                                      'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Chandigarh', 'Coimbatore', 'Visakhapatnam', 
                                      'Vadodara', 'Bhopal', 'Patna', 'Vadodara', 'Agra', 'Nashik', 'Faridabad'])

    # Add a button to trigger dowry prediction
    if st.button("Generate Dowry Prediction"):
        if salary > 0 and property_value > 0:
            # Calculate dowry based on user inputs
            dowry = calculate_dowry(salary, property_value, job_type, caste, region, state, city)

            # Assign assets (car, bike, flat) based on dowry amount
            car, bike, flat = assign_assets(dowry)

            # Display results
            st.write(f"**Predicted Dowry Amount**: ₹{dowry}")
            st.write("**With this dowry, you could receive the following:**")
            st.write(f"- **Car**: {car}")
            st.write(f"- **Bike**: {bike}")
            st.write(f"- **Flat**: {flat}")
        else:
            st.error("Please enter valid Salary and Property Value.")

if __name__ == "__main__":
    main()
