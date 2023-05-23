
import streamlit as st
import plotly.graph_objects as go

def main():
    st.text("Ciao questo front-end funziona")

    fig = go.Figure()

    #Actual 
    fig.add_trace(go.Scatter(x = df.index, 
                            y = df['tavg'],
                            mode = "lines",
                            name = "Aveg",
                            line_color='#0000FF',
                            ))
    ##############################################################
    #Predicted 
    fig.add_trace(go.Scatter(x = df.index, 
                            y = df['tmax'],
                            mode = "lines", 
                            name = "Max",
                            line_color='#ff8c00',
                            ))

    ##############################################################
    # adjust layout
    fig.update_layout(title = "Titolo",
                    xaxis_title = "Date",
                    yaxis_title = "Sales",
                    width = 1700,
                    height = 700,
                    )
    ####################################################################
    # zoomming
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=2, label="3y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    
st.write("la somma è ")


if __name__ == "__main__":
    main()

#streamlit run app.py