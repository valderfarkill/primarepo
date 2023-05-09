
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    st.text("Esercizio Regressione")
    # slider
    n_points = st.slider("Points number",100,300,100)
    generate_random = np.random.RandomState(667)
    x = 10 * generate_random.rand(n_points)

    n_range = st.slider("Noise Range", 1,10,1)
    noise = np.random.normal(0,n_range,n_points)
    y = 3 * x + noise

    X = x.reshape(-1 ,1)

    n_split = st.slider("Split index",0.1,1.0,0.1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = n_split, random_state = 667)

    model = LinearRegression(fit_intercept=True)
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    y_train_pred = model.predict(X_train)

    fig, ax = plt.subplots()
    ax.plot(y_test_pred)
    ax.plot(y_test)
    st.pyplot(fig)


if __name__ == "__main__":
    main()

#streamlit run app.py