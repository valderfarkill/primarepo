
import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def main():
    st.text("Multi Linear Regression")
    # slider
    df = pd.read_csv("https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv")
    
    X = df.drop(columns="Profit")
    y = df["Profit"]
    df

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 667)

    model = LinearRegression(fit_intercept=True)
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    y_train_pred = model.predict(X_train)

    l = y_test_pred.shape[0]
    x = np.linspace(0,l,l)

    fig, ax = plt.subplots()
    ax.plot(x, y_test_pred, label="predicted y")
    ax.plot(x, y_test, label="real y")
    st.pyplot(fig)

    #inference
    st.text("Try the model")
    input1 = st.number_input("Insert R&D value:",)
    input2 = st.number_input("Insert Administration value:",)
    input3 = st.number_input("Insert Marketing Spend value:",)

    prediction = model.predict([[input1, input2, input3]])[0]
    st.write(f"Predicted profit: {round(prediction,1)}$")


if __name__ == "__main__":
    main()

#streamlit run app.py