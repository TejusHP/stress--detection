"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")
    st.markdown(
        """
        <style>
            /* Customize the title style */
            .title {
                font-size: 36px;
                color: #0072b1; /* Change the title text color */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Add image to the home page
    st.image("Stress-Level-Detector\images\heroimage.jpg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
              Welcome to our stress level detection project! We have developed an innovative solution that
              leverages physiological parameters to predict and assess stress levels accurately. 
              Stress is a prevalent issue in today's fast-paced world, and our system aims to provide individuals with valuable insights into their stress levels 
              for better self-care and well-being.        
        </p>
    """, unsafe_allow_html=True)
