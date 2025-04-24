import streamlit as st
import pandas as pd
import os

# Path to CSV file
CSV_FILE = 'students.csv'

# Streamlit App Title
st.title("Student Registration Form")

# Student data form
with st.form("student_form"):
    name = st.text_input("Name")
    roll_no = st.text_input("Roll Number")
    degree = st.text_input("Degree")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and roll_no and degree:
            # Create or load existing CSV
            if os.path.exists(CSV_FILE):
                df = pd.read_csv(CSV_FILE)
            else:
                df = pd.DataFrame(columns=["Name", "Roll Number", "Degree"])

            # Add new row
            new_row = {"Name": name, "Roll Number": roll_no, "Degree": degree}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

            # Save to CSV
            df.to_csv(CSV_FILE, index=False)
            st.success("Student details saved successfully!")
        else:
            st.error("Please fill in all fields.")

# ✅ No data is shown on the web — only stored in the CSV
