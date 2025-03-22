import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import hashlib
import subprocess
import base64

load_dotenv()
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")

schema_name = "emoryhackathon"

# Construct the SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{schema_name}")

# Set page configuration
st.set_page_config(page_title="Student Info Input", layout="wide")

# Ensure user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please log in first!")
    st.stop()

# Retrieve username from session
username = st.session_state.get("username")

st.title("🎓 Tutor Connect - Student Registration")

def personal_information(user_id=username):
    # Fetch current values from the DB
    try:
        with engine.connect() as conn:
            query = text("SELECT * FROM student WHERE user_id = :username")
            result = conn.execute(query, {"username": user_id}).fetchone()

            if result:
                current_info = result._mapping  # ✅ correct way to access row data as dict
            else:
                st.error("No student record found for this user.")
                return
    except Exception as e:
        st.error(f"Database error fetching current data: {e}")
        return

    # Set default values from DB or show placeholder if empty
    email = st.text_input(
        "Enter your Email",
        value=current_info.get("email") or "",
        key="email"
    )

    university = st.text_input(
        "Enter your University", 
        value=current_info.get("university"), 
        key="university"
    )
    grad_year = st.number_input(
        "Graduation Year", 
        min_value=1990, 
        max_value=2035, 
        step=1, 
        value=current_info.get("graduation_year"), 
        key="grad_year"
    )
    majors = ["Computer Science", "Biology", "Business", "Engineering", "Psychology", "Other"]
    major = st.selectbox(
        "Select your Major", 
        majors, 
        index=majors.index(current_info.get("major")) if current_info.get("major") in majors else 0,
        key="major"
    )
    employed_status = st.checkbox(
        "Currently Employed?", 
        value=bool(current_info.get("employed_status")), 
        key="employed_status"
    )
    internships = st.checkbox(
        "Have you done any Internships?", 
        value=bool(current_info.get("internships")), 
        key="internships"
    )
    grad_school = st.checkbox(
        "Are you currently in Graduate School?", 
        value=bool(current_info.get("grad_school")), 
        key="grad_school"
    )
    gpa_options = ["Below 2.5", "2.5 - 3.0", "3.0 - 3.5", "3.5 - 4.0"]
    gpa_range = st.selectbox(
        "Select your GPA Range (on a scale of 4)", 
        gpa_options, 
        index=gpa_options.index(current_info.get("gpa_range")) if current_info.get("gpa_range") in gpa_options else 0,
        key="gpa_range"
    )
    classes_taking = st.text_area(
        "Enter the classes you are taking (comma-separated)", 
        value=current_info.get("classes_taking"), 
        key="classes_taking"
    )
    bio = st.text_area(
        "Write a short bio about yourself", 
        value=current_info.get("bio"), 
        key="bio"
    )

    # Submit updated info
    if st.button("Submit Information"):
        # Check required fields
        if not university or university == "empty" or not classes_taking or classes_taking == "empty" or not bio or bio == "empty":
            st.warning("Please fill in all required fields.")
            return

        try:
            with engine.connect() as conn:
                modify_query = text("""                                
                    UPDATE student
                    SET university = :university, 
                        graduation_year = :grad_year, 
                        major = :major, 
                        employed_status = :employed_status,
                        internships = :internships, 
                        grad_school = :grad_school, 
                        gpa_range = :gpa_range, 
                        classes_taking = :classes_taking, 
                        bio = :bio,
                        email = :email
                    WHERE user_id = :username
                ;""")

                conn.execute(modify_query, {
                    "university": university,
                    "grad_year": grad_year,
                    "major": major,
                    "employed_status": employed_status,
                    "internships": internships,
                    "grad_school": grad_school,
                    "gpa_range": gpa_range,
                    "classes_taking": classes_taking,
                    "bio": bio,
                    "username": user_id,
                    "email": email
                })

                conn.commit()
                st.success("Personal Information Updated!")

        except Exception as e:
            st.error(f"Database error: {e}")


st.header("Fill in or Edit Your Personal Information")
personal_information()