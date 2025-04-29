import streamlit as st
import json

class TestTaker:
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def render(self):
        st.subheader("Take Test")
        conn = sqlite3.connect(self.db.db_name)
        c = conn.cursor()
        c.execute('SELECT * FROM questions')
        questions = c.fetchall()
        conn.close()

        if questions:
            for q in questions:
                st.write(f"**Question:** {q[4]}")
                options = json.loads(q[5])
                selected_option = st.radio("Options", options, key=f"option_{q[0]}")
                if st.button("Submit", key=f"submit_{q[0]}"):
                    is_correct = selected_option == options[0]  # Assuming the first option is correct
                    self.store_result("default_user", q[0], selected_option, is_correct)
                    st.success("Answer submitted!")
                    self.logger.info(f"Question {q[0]} answered.")

    def store_result(self, user, question_id, selected_option, is_correct):
        conn = sqlite3.connect(self.db.db_name)
        c = conn.cursor()
        c.execute('''INSERT INTO results (user, question_id, selected_option, is_correct) 
                     VALUES (?, ?, ?, ?)''', (user, question_id, selected_option, is_correct))
        conn.commit()
        conn.close()