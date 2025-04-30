import streamlit as st
import os
from app_components.logger import setup_logger
from app_components.database import Database
from app_components.question_uploader import QuestionUploader
from app_components.test_taker import TestTaker
from app_components.result_viewer import ResultViewer



# Initialize logger
logger = setup_logger()

# Initialize database
try:
    db = Database()
    db.init_db()
    db.init_results_table()
except Exception as e:
    logger.error(f"Error initializing database: {e}")
    st.error("Failed to connect to the database. Please check the logs for more details.")
    exit()

# Function to load CSS
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("assets/custom.css")

# App layout
st.title("Azure Certification Learning App")


menu = ["Upload Questions", "Take Test", "View Results"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Upload Questions":
    QuestionUploader(db, logger).render()

elif choice == "Take Test":
    TestTaker(db, logger).render()

elif choice == "View Results":
    ResultViewer(db, logger).render()