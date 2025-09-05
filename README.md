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

### Backend (Streamlit)

1.  Install dependencies:
    ```bash
    pip install streamlit pandas
    ```
2.  Run the Streamlit application:
    ```bash
    streamlit run streamlit_app/Home.py
    ```

### Frontend (FastHTML)

1.  Install dependencies:
    ```bash
    pip install fasthtml
    ```
2.  Run the FastHTML application:
    ```bash
    python app.py
    ```

### Database

The SQLite database file (`rentster.db`) is automatically created in the `streamlit_app` directory when the Streamlit application is first run.


