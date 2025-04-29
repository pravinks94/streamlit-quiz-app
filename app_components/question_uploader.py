import json
import streamlit as st
import re

class QuestionUploader:
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def process_uploaded_file(self, file):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            if file.type == "application/json":
                data = json.load(file)
                for item in data:
                    cursor.execute("""
                        INSERT INTO questions (category, subcategory, level, question, options, answer) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (item['category'], item['subcategory'], item['level'], item['question'], json.dumps(item['options']), item['answer']))
            elif file.type == "application/pdf":
                from PyPDF2 import PdfReader
                reader = PdfReader(file)
                for page in reader.pages:
                    text = page.extract_text()
                    lines = text.split('\n')
                    question_lines = []
                    for line in lines:
                        line = line.strip()
                        if re.match(r"^(Question|Q:|What is|Who|When|Where|Why|How|Which|Describe|Define)\s*", line, re.IGNORECASE):
                            question_lines.append(line)

                    for question in question_lines:
                        cursor.execute("""
                            INSERT INTO questions (category, subcategory, level, question, options, answer) 
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """, ("pdf_uploaded", "pdf_questions", "unknown", question, json.dumps([]), ""))
            else:
                st.error("Unsupported file format")
                self.logger.error(f"Unsupported file format {file.type}")
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    def render(self):
        st.subheader("Upload Questions")
        uploaded_file = st.file_uploader("Upload a file (PDF, JSON, or GitHub link)", type=["pdf", "json"])
        if uploaded_file:
            self.process_uploaded_file(uploaded_file)
            st.success("Questions uploaded and stored successfully!")
            self.logger.info("Questions uploaded successfully.")