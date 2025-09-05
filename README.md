# Rentster.eu Clone

This project is a clone of the Rentster.eu rental management platform, built with a Streamlit backend and a FastHTML landing page.

## Project Structure

- `streamlit_app/`: Contains the Streamlit backend application.
  - `Home.py`: The main application file.
  - `pages/`: Additional pages for the Streamlit app.
  - `rentster.db`: The SQLite database file.
- `fasthtml_landing/`: Contains the FastHTML landing page.
- `rentster_analysis.md`: Analysis of the original Rentster.eu website.
- `data_model.md`: Data model and database schema.

## Setup and Installation

### Quick Start

1.  Clone the repository:
    ```bash
    git clone https://github.com/kaljuvee/rental-manager.git
    cd rental-manager
    ```

2.  Install all dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Backend (Streamlit)

1.  Run the Streamlit application:
    ```bash
    streamlit run streamlit_app/Home.py
    ```
    Access at: http://localhost:8501

### Frontend (FastHTML)

1.  Run the FastHTML application:
    ```bash
    cd fasthtml_landing
    python app.py
    ```
    Access at: http://localhost:5001

### Database

The SQLite database file (`rentster.db`) is automatically created in the `streamlit_app` directory when the Streamlit application is first run.


