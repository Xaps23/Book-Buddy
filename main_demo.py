import streamlit as st
import pandas as pd
import random

def login_page():
    st.set_page_config(page_title="Book Buddy Login", page_icon="📚", layout="centered")
    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f6fa;
        }
        .stButton>button {
            background-color: #6c63ff;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 2em;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.image("https://img.freepik.com/free-vector/flat-design-stack-books-illustration_23-2149322943.jpg", width=250)
    st.title("Welcome to Book Buddy!")
    st.write("Please log in to continue:")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

    if login_btn:
        if username and password:
            st.success(f"Welcome, **{username}**! (login successful)")

            # --- Book Recommendation Feature ---
            try:
                # Adjust the path if needed
                books = pd.read_csv("artifacts/clean_data/clean_data.csv")
                # Pick a random book
                book = books.sample(1).iloc[0]
                st.markdown("---")
                st.subheader("📖 Book Recommendation For You")
                st.image(book['Image-URL-M'], width=150)
                st.write(f"**{book['title']}** by *{book['author']}*")
                st.caption(f"Published by {book['publisher']} ({book['year']})")
            except Exception as e:
                st.warning("Could not load book data for recommendation.")
        else:
            st.error("Please enter both username and password.")

    st.sidebar.markdown("## Book Buddy")
    st.sidebar.info("This is a sidebar. Any username and password will work.")

if __name__ == "__main__":
    login_page()