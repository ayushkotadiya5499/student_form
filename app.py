import streamlit as st
import pandas as pd
import os

# Title
st.title("Student Registration Form")

# Input fields
student_name = st.text_input("Student Name")
student_mark = st.number_input("Student Mark", min_value=0, max_value=100)
student_degree = st.selectbox("Student Degree", ["BSc", "MSc", "PhD"])

# File path
file_path = "students.csv"

# Submit button
if st.button("Submit"):
    if student_name:
        # New data
        new_data = pd.DataFrame({
            "Name": [student_name],
            "Mark": [student_mark],
            "Degree": [student_degree]
        })

        # Append to CSV or create new one
        if os.path.exists(file_path):
            new_data.to_csv(file_path, mode='a', header=False, index=False)
        else:
            new_data.to_csv(file_path, index=False)

        st.success("Student record saved successfully!")
    else:
        st.error("Please enter the student's name.")
