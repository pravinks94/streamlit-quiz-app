import json
from PyPDF2 import PdfReader
import streamlit as st

class QuestionUploader:
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def process_uploaded_file(self, file):
        conn = sqlite3.connect(self.db.db_name)
        c = conn.cursor()

        if file.type == "application/json":
            data = json.load(file)
            for item in data:
                c.execute('''INSERT INTO questions (category, subcategory, level, question, options, answer) 
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                          (item['category'], item['subcategory'], item['level'], item['question'], json.dumps(item['options']), item['answer']))
        elif file.type == "application/pdf":
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                # Add logic to parse text into questions and insert into the database

        conn.commit()
        conn.close()

    def render(self):
        st.subheader("Upload Questions")
        uploaded_file = st.file_uploader("Upload a file (PDF, JSON, or GitHub link)", type=["pdf", "json"])
        if uploaded_file:
            self.process_uploaded_file(uploaded_file)
            st.success("Questions uploaded and stored successfully!")
            self.logger.info("Questions uploaded successfully.")