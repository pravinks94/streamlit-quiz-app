import sqlite3

class Database:
    def __init__(self):
        self.db_name = 'questions.db'

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS questions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category TEXT,
                        subcategory TEXT,
                        level TEXT,
                        question TEXT,
                        options TEXT,
                        answer TEXT
                    )''')
        conn.commit()
        conn.close()

    def init_results_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user TEXT,
                        question_id INTEGER,
                        selected_option TEXT,
                        is_correct BOOLEAN,
                        FOREIGN KEY (question_id) REFERENCES questions (id)
                    )''')
        conn.commit()
        conn.close()