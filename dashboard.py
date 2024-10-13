import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
all_df = pd.read_csv("../dahsboard/all_df.csv")

# Set the title of the dashboard
st.title('E-commerce Data Analysis Dashboard')

# Sidebar for navigation
menu = ['Home', 'Top Products', 'Sales by State', 'Review Scores']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Home')
    st.write('Welcome to the E-commerce Data Analysis Dashboard. Use the sidebar to navigate through different sections.')

elif choice == 'Top Products':
    st.subheader('Top Products')
    # Plot top 5 highest profit products
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="price", y="product_category_name_english", data=all_df, estimator=sum, ci=None, palette="Blues_d", order=all_df.groupby("product_category_name_english")["price"].sum().sort_values(ascending=False).index[:5])
    ax.set_xlabel('Price')
    ax.set_ylabel('Product Category')
    ax.set_title('Top 5 Highest Profit Products')
    st.pyplot(fig)

elif choice == 'Sales by State':
    st.subheader('Sales by State')
    # Plot number of orders by state
    state_counts = all_df['customer_state'].value_counts()
    st.bar_chart(state_counts)

elif choice == 'Review Scores':
    st.subheader('Review Scores')
    # Plot distribution of review scores
    score_counts = all_df['review_score'].value_counts().sort_index()
    st.bar_chart(score_counts)    