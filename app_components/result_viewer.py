import streamlit as st

class ResultViewer:
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def fetch_results(self):
        conn = sqlite3.connect(self.db.db_name)
        c = conn.cursor()
        c.execute('''SELECT q.category, q.subcategory, q.level, q.question, r.selected_option, r.is_correct 
                     FROM results r 
                     JOIN questions q ON r.question_id = q.id''')
        results = c.fetchall()
        conn.close()
        return results

    def render(self):
        st.subheader("View Results")
        results = self.fetch_results()
        if results:
            for res in results:
                st.write(f"**Category:** {res[0]} > {res[1]} > {res[2]}")
                st.write(f"**Question:** {res[3]}")
                st.write(f"**Your Answer:** {res[4]}")
                st.write(f"**Correct:** {'Yes' if res[5] else 'No'}")
                st.write("---")
            self.logger.info("Results displayed successfully.")
        else:
            st.info("No results to display. Take a test first.")