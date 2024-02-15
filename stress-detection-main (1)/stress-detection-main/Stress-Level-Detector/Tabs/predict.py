"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict



def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <a href="https://scikit-learn.org/stable/modules/tree.html" target="_blank"><b style="color:green">Decision Tree Classifier</b></a>
                for the Prediction of Stress Level.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    sr = st.slider("Snoring Rate", int(df["sr"].min()), int(df["sr"].max()))
    rr = st.slider("Respiration Rate", int(df["rr"].min()), int(df["rr"].max()))
    bt = st.slider("Body Temperature (in °F)", int(df["bt"].min()), int(df["bt"].max()))
    lm = st.slider("Limb Movement", float(df["lm"].min()), float(df["lm"].max()))
    bo = st.slider("Blood Oxygen(%)", float(df["bo"].min()), float(df["bo"].max()))
    rem = st.slider("Rapid Eye Movement", float(df["rem"].min()), float(df["rem"].max()))
    sh = st.slider("Sleeping Hour", float(df["sh"].min()), float(df["sh"].max()))
    hr = st.slider("Heart Rate", float(df["hr"].min()), float(df["hr"].max()))
    

    # Create a list to store all the features
    features = [sr,rr,bt,lm,bo,rem,sh,hr]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Stress level detected...")

    # Display stress level meter
        st.subheader("Stress Level Meter:")
        if prediction == 1:
            progress_color = "green"
        elif prediction == 2:
            progress_color = "chartreuse"
        elif prediction == 3:
            progress_color = "orange"
        elif prediction == 4:
            progress_color = "red"
        else:
            progress_color = "light Green"

        st.markdown(
            f"""
            <div style="background-color: {progress_color}; border-radius: 5px; padding: 5px;">
                <p style="color: black; text-align: center;"</p>
            </div>
            """  
        , unsafe_allow_html=True)

        # Print the output according to the prediction
        if (prediction == 1):
            

            st.markdown(
            f"""
            <div style="background-color: {progress_color}; border-radius: 5px; padding: 5px;">
                <p style="color: white; text-align: center;">The person has low stress level 🙂 </p>
            </div>
            """  
        , unsafe_allow_html=True)
        elif (prediction == 2):
           
            st.markdown(
            f"""
            <div style="background-color: {progress_color}; border-radius: 5px; padding: 5px;">
                <p style="color: white; text-align: center;">The person has medium stress level 😐 </p>
            </div>
            """  
        , unsafe_allow_html=True)



        elif (prediction == 3):
           
            st.markdown(
            f"""
            <div style="background-color: {progress_color}; border-radius: 5px; padding: 5px;">
                <p style="color: white; text-align: center;"> The person has high stress level! 😞</p>
            </div>
            """  
        , unsafe_allow_html=True)


        elif (prediction == 4):
            
            st.markdown(
            f"""
            <div style="background-color: {progress_color}; border-radius: 5px; padding: 5px;">
                <p style="color: white; text-align: center;"> The person has very high stress level!! 😫</p>
            </div>
            """  
        , unsafe_allow_html=True)
        else:
           # st.success("The person is stress free and calm 😄")
            st.markdown(
            f"""
            <div style="background-color: {progress_color}; border-radius: 5px; padding: 5px;">
                <p style="color: white; text-align: center;"> The person has very high stress level!! 😫</p>
            </div>
            """  
        , unsafe_allow_html=True)

        
