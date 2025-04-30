import streamlit as st
import sqlite3
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

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

    def calculate_category_results(self, results):
        category_results = {}
        for res in results:
            category = res[0]
            is_correct = res[5]
            if category not in category_results:
                category_results[category] = {'correct': 0, 'incorrect': 0}
            if is_correct:
                category_results[category]['correct'] += 1
            else:
                category_results[category]['incorrect'] += 1
        return category_results

    def display_category_bar_chart_bokeh(self, category_results):
         categories = list(category_results.keys())
         correct_counts = [category_results[cat]['correct'] for cat in categories]
        incorrect_counts = [category_results[cat]['incorrect'] for cat in categories]

        source = ColumnDataSource(data=dict(
            categories=categories,
            correct=correct_counts,
            incorrect=incorrect_counts,
        ))

        p = figure(x_range=categories, height=350, title="Correct vs Incorrect Answers per Category",
                   toolbar_location=None, tools="hover", tooltips="$name @categories: @$name")
        p.vbar(x='categories', top='correct', width=0.4, source=source, color="green", legend_label="Correct")
        p.vbar(x='categories', top='incorrect', width=0.4, source=source, color="red", legend_label="Incorrect", y_offset='correct')

        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.legend.location = "top_left"
        st.bokeh_chart(p, use_container_width=True)
    def render(self):
        st.subheader("View Results")
        results = self.fetch_results()
        if results:
            category_results = self.calculate_category_results(results)
            self.display_category_bar_chart_bokeh(category_results)

            self.logger.info("Results displayed successfully.")
        else:
            st.info("No results to display. Take a test first.")