# Rentster.eu Clone

This project is a clone of the Rentster.eu rental management platform, built with a Streamlit backend and a FastHTML landing page.

## Project Structure

- `streamlit_app/`: Contains the Streamlit backend application.
  - `Home.py`: The main application file.
  - `pages/`: Additional pages for the Streamlit app.
  - `requirements.txt`: Streamlit-specific dependencies.
  - `rentster.db`: The SQLite database file.
- `fasthtml_landing/`: Contains the FastHTML landing page.
  - `app.py`: FastHTML application file.
  - `requirements.txt`: FastHTML-specific dependencies.
- `business_analysis.md`: Comprehensive business logic analysis.
- `rentster_analysis.md`: Analysis of the original Rentster.eu website.
- `data_model.md`: Data model and database schema.

## Setup and Installation

### Quick Start

1.  Clone the repository:
    ```bash
    git clone https://github.com/kaljuvee/rental-manager.git
    cd rental-manager
    ```

### Backend (Streamlit)

1.  Install Streamlit dependencies:
    ```bash
    cd streamlit_app
    pip install -r requirements.txt
    ```

2.  Run the Streamlit application:
    ```bash
    streamlit run Home.py
    ```
    Access at: http://localhost:8501

### Frontend (FastHTML)

1.  Install FastHTML dependencies:
    ```bash
    cd fasthtml_landing
    pip install -r requirements.txt
    ```

2.  Run the FastHTML application:
    ```bash
    python app.py
    ```
    Access at: http://localhost:5001

### Database

The SQLite database file (`rentster.db`) is automatically created in the `streamlit_app` directory when the Streamlit application is first run.


