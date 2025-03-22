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

# Page config
st.set_page_config(page_title="TutorConnect | Learn Better", layout="wide")

# Custom CSS (basic styles mimicking your HTML)
st.markdown("""
    <style>
    html, body {
        font-family: 'Kumbh Sans', sans-serif;
    }
    .navbar {
        background-color: #4B7BE5;
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
    }
    .navbar a {
        color: white;
        text-decoration: none;
        margin-left: 1.5rem;
        font-weight: bold;
    }
    .hero {
        background: linear-gradient(to right, #4B7BE5, #6FB1FC);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .hero p {
        font-size: 1.25rem;
    }
    .hero_cta {
        background-color: white;
        color: #4B7BE5;
        padding: 0.75rem 1.5rem;
        border-radius: 5px;
        font-weight: bold;
        text-decoration: none;
        margin-top: 1.5rem;
        display: inline-block;
    }
    .services h2 {
        text-align: center;
        margin-bottom: 2rem;
        font-size: 2rem;
        color: #4B7BE5;
    }
    .card img {
        border-radius: 10px;
        width: 100%;
        height: 180px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Navbar ----
st.markdown("""
<div class="navbar">
    <div><strong>TutorConnect</strong></div>
    <div>
        <a href="#">About Us</a>
        <a href="#">Profile</a>
        <a href="#">Tutors</a>
        <a href="#">Subjects</a>
        <a href="#">Sign Out</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown("""
<div class="hero">
    <h1>Unlock Your Full Potential</h1>
    <p>Personalized tutoring for every learner, anytime, anywhere.</p>
    <a href="#" class="hero_cta">Find a Tutor</a>
</div>
""", unsafe_allow_html=True)

# ---- Services Section ----
st.markdown("<div class='services'><h2 class='section_title'>Our Tutoring Services</h2></div>", unsafe_allow_html=True)

# ---- Cards ----
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://www.the74million.org/wp-content/uploads/2024/01/tutor-one-on-one.jpg", use_column_width=True)
    st.subheader("One-on-One Tutoring")
    st.write("Work directly with a professional tutor who tailors lessons to your individual needs and pace.")

with col2:
    st.image("https://images.unsplash.com/photo-1522075469751-3a6694fb2f61", use_column_width=True)
    st.subheader("Group Sessions")
    st.write("Join small interactive study groups to learn collaboratively and stay motivated with peers.")

with col3:
    st.image("https://images.unsplash.com/photo-1607746882042-944635dfe10e", use_column_width=True)
    st.subheader("Online Resources")
    st.write("Access a wide library of lessons, quizzes, and study guides to support your learning journey anytime.")