# Azure Certification Learning App

This is a Streamlit-based application designed to help users prepare for Azure certification exams. The app allows users to:

1. Upload questions via JSON or PDF.
2. Take tests with categorized questions.
3. View results of the tests.

## Features
- **Question Upload**: Upload questions in JSON or PDF format.
- **Categorization**: Questions are stored with three levels of categorization (category, subcategory, and level).
- **Test Taking**: Interactive test-taking experience.
- **Results Viewing**: View detailed results of your tests.

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python3 -m venv .env
   ```
3. Activate the virtual environment:
   ```bash
   source .env/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Requirements
See `requirements.txt` for the list of dependencies.