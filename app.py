import streamlit as st
import pandas as pd
import os

# CSV file path
CSV_FILE = 'students.csv'

# Title
st.title("Student Details Form")

# Form for data entry
with st.form("student_form"):
    name = st.text_input("Name")
    roll_no = st.text_input("Roll Number")
    degree = st.text_input("Degree")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and roll_no and degree:
            # Check if CSV exists
            if os.path.exists(CSV_FILE):
                df = pd.read_csv(CSV_FILE)
            else:
                df = pd.DataFrame(columns=["Name", "Roll Number", "Degree"])

            # Add new data
            new_data = {"Name": name, "Roll Number": roll_no, "Degree": degree}
            df = df.append(new_data, ignore_index=True)

            # Save to CSV
            df.to_csv(CSV_FILE, index=False)
            st.success("Student details saved successfully!")
        else:
            st.error("Please fill out all fields.")

# Display current data
if os.path.exists(CSV_FILE):
    st.subheader("Saved Student Details")
    df = pd.read_csv(CSV_FILE)
    st.dataframe(df)
else:
    st.info("No data found. Please add student details.")
