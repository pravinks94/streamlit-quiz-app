from app_components.logger import setup_logger
from app_components.database import Database
from app_components.question_uploader import QuestionUploader
from app_components.test_taker import TestTaker
from app_components.result_viewer import ResultViewer

# Initialize logger
logger = setup_logger()

# Initialize database
db = Database()
db.init_db()
db.init_results_table()

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