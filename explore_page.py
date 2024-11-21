import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv('Dataset .csv')
    df = df[df["Average Cost for two"] < 70000]
    df = df[df["Rating text"] != "Not rated"]
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Restaurant Review Data")
    st.divider()

    col1, col2 = st.columns([0.5, 0.5])
    
    with col1:
        data = df["Has Online delivery"].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
        ax1.axis("equal")
        st.write("""#### Percentage of Restaurants based on Online Delivery""")
        st.pyplot(fig1)

    with col2:
        data = df["Has Table booking"].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
        ax2.axis("equal")
        st.write("""#### Percentage of Restaurants based on Table Booking""")
        st.pyplot(fig2)

    st.write("""#### Average Rating vs. Average Cost (for 2 people)""")
    st.scatter_chart(data=df, x="Aggregate rating", y="Average Cost for two", x_label="Rating", y_label="Cost")

    st.write("""#### Average Cost (for 2 people) based on City""")
    data = df.groupby(["City"])["Average Cost for two"].mean().sort_values(ascending=True)
    st.bar_chart(data)