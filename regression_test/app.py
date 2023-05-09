
import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/stock-assets/getty/image/others/f8/6f/f86f1cab-7223-4653-b1c8d2550e8ca474.component.xl.ts=1666030995092.jpg/content/adobe-cms/us/en/topics/linear-regression/jcr:content/root/leadspace");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


def main():
    st.text("Multi Linear Regression")
    # slider
    
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        
        df = pd.read_csv(file) if file.type == "application/vnd.ms-excel" else pd.read_excel(file)
        #inference
        st.write("Try the model")
        st.write(df)

        input1 = st.number_input("Insert R&D value:",)
        input2 = st.number_input("Insert Administration value:",)
        input3 = st.number_input("Insert Marketing Spend value:",)

        newmodel = joblib.load('regression_test.pkl')
        prediction = newmodel.predict([[input1, input2, input3]])[0]
        df["Predicted Profit"] = np.round(prediction,1)
        st.write(f"Predicted profit: {round(prediction,1)}$")    
        st.write(df)
    
if __name__ == "__main__":
    main()

#streamlit run app.py