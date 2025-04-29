import psycopg2
import os

class Database:
    def __init__(self):
        self.db_name = os.environ.get("POSTGRES_DB", "your_db_name")
        self.db_user = os.environ.get("POSTGRES_USER", "your_db_user")
        self.db_password = os.environ.get("POSTGRES_PASSWORD", "your_db_password")
        self.db_host = os.environ.get("POSTGRES_HOST", "localhost")
        self.db_port = os.environ.get("POSTGRES_PORT", "5432")

    def init_db(self):
        conn = psycopg2.connect(database=self.db_name,
                                user=self.db_user,
                                password=self.db_password,
                                host=self.db_host,
                                port=self.db_port)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS questions (
                        id SERIAL PRIMARY KEY,
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
        conn = psycopg2.connect(database=self.db_name,
                                user=self.db_user,
                                password=self.db_password,
                                host=self.db_host,
                                port=self.db_port)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS results (
                        id SERIAL PRIMARY KEY,
                        user TEXT,
                        question_id INTEGER,
                        selected_option TEXT,
                        is_correct BOOLEAN,
                        FOREIGN KEY (question_id) REFERENCES questions (id)
                    )''')
        conn.commit()
        conn.close()