import streamlit as st
import pandas as pd
import os

CSV_FILE = 'students.csv'

st.title("Student Registration Form")

with st.form("student_form"):
    name = st.text_input("Name")
    roll_no = st.text_input("Roll Number")
    degree = st.text_input("Degree")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and roll_no and degree:
            if os.path.exists(CSV_FILE):
                df = pd.read_csv(CSV_FILE)
            else:
                df = pd.DataFrame(columns=["Name", "Roll Number", "Degree"])

            new_row = {"Name": name, "Roll Number": roll_no, "Degree": degree}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

            # Save and show save location
            df.to_csv(CSV_FILE, index=False)
            st.success("Student details saved successfully!")
            st.write("Saved to:", os.path.abspath(CSV_FILE))
        else:
            st.error("Please fill in all fields.")
