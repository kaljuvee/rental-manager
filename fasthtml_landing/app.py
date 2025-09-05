from fasthtml.common import *

# Create FastHTML app
app, rt = fast_app()

# Streamlit backend URL
STREAMLIT_URL = "https://rental-manager.streamlit.app"

# CSS styles
css = Style("""
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
    }

    .header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 0;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }

    .logo {
        font-size: 1.5rem;
        font-weight: bold;
    }

    .nav-links {
        display: flex;
        list-style: none;
        gap: 2rem;
    }

    .nav-links a {
        color: white;
        text-decoration: none;
        transition: opacity 0.3s;
    }

    .nav-links a:hover {
        opacity: 0.8;
    }

    .auth-buttons {
        display: flex;
        gap: 1rem;
    }

    .btn {
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.3s;
        font-weight: 500;
        display: inline-block;
    }

    .btn-outline {
        background: transparent;
        color: white;
        border: 2px solid white;
    }

    .btn-outline:hover {
        background: white;
        color: #667eea;
    }

    .btn-primary {
        background: #4CAF50;
        color: white;
    }

    .btn-primary:hover {
        background: #45a049;
        transform: translateY(-2px);
    }

    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8rem 2rem 4rem;
        text-align: center;
        margin-top: 60px;
    }

    .hero-content {
        max-width: 800px;
        margin: 0 auto;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }

    .hero p {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }

    .features {
        padding: 4rem 2rem;
        background: #f8f9fa;
    }

    .features-container {
        max-width: 1200px;
        margin: 0 auto;
    }

    .features h2 {
        text-align: center;
        margin-bottom: 3rem;
        font-size: 2.5rem;
        color: #333;
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }

    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }

    .feature-card:hover {
        transform: translateY(-5px);
    }

    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #667eea;
    }

    .feature-card h3 {
        margin-bottom: 1rem;
        color: #333;
    }

    .pricing {
        padding: 4rem 2rem;
        background: white;
    }

    .pricing-container {
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
    }

    .pricing h2 {
        margin-bottom: 3rem;
        font-size: 2.5rem;
        color: #333;
    }

    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .pricing-card {
        background: white;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 2rem;
        transition: all 0.3s;
    }

    .pricing-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
    }

    .pricing-card.featured {
        border-color: #667eea;
        transform: scale(1.05);
    }

    .price {
        font-size: 3rem;
        font-weight: bold;
        color: #667eea;
        margin: 1rem 0;
    }

    .footer {
        background: #333;
        color: white;
        padding: 2rem;
        text-align: center;
    }

    @media (max-width: 768px) {
        .nav {
            flex-direction: column;
            gap: 1rem;
        }
        
        .hero h1 {
            font-size: 2rem;
        }
        
        .nav-links {
            flex-direction: column;
            gap: 1rem;
        }
    }
""")

app, rt = fast_app(hdrs=[css])

@rt("/")
def get():
    return Title("Rental Manager - Rental Management Platform"), \
        Header(
            Nav(
                Div("Rental Manager", cls="logo"),
                Ul(
                    Li(A("Home", href="#")),
                    Li(A("Features", href="#features")),
                    Li(A("Pricing", href="#pricing")),
                    Li(A("Contact", href="#contact")),
                    cls="nav-links"
                ),
                Div(
                A("Login", href=f"{STREAMLIT_URL}", target="_blank", cls="btn"),
                A("Sign Up", href=f"{STREAMLIT_URL}", target="_blank", cls="btn btn-primary"),
                    cls="auth-buttons"
                ),
                cls="nav"
            ),
            cls="header"
        ), \
        Section(
            Div(
                H1("Rental Management Platform"),
                P("Comprehensive rental management solution with digital calendar, order processing, digital signatures, online payments, and contactless rental capabilities."),
                A("Get Started", href=f"{STREAMLIT_URL}", target="_blank", cls="btn btn-primary", style="font-size: 1.1rem; padding: 1rem 2rem;"),
                cls="hero-content"
            ),
            cls="hero"
        ), \
        Section(
            Div(
                H2("Core Features"),
                Div(
                    Div(
                        Div("📅", cls="feature-icon"),
                        H3("Synchronized Online Calendar"),
                        P("Integrate with home calendar, phone, Outlook, Mac, or Google Calendar for seamless scheduling."),
                        cls="feature-card"
                    ),
                    Div(
                        Div("💳", cls="feature-icon"),
                        H3("Payment Links"),
                        P("Integrated payment service for smooth and secure payment experiences without third-party redirects."),
                        cls="feature-card"
                    ),
                    Div(
                        Div("🌐", cls="feature-icon"),
                        H3("Free Website Platform"),
                        P("Complete rental platform with domain connection for effortless rental management."),
                        cls="feature-card"
                    ),
                    Div(
                        Div("✍️", cls="feature-icon"),
                        H3("Digital Signatures"),
                        P("EU-legally binding document signing with automated digital solutions."),
                        cls="feature-card"
                    ),
                    Div(
                        Div("🔐", cls="feature-icon"),
                        H3("Access Management"),
                        P("Integrate rental spaces, parcel machines, and warehouses with smart access control."),
                        cls="feature-card"
                    ),
                    Div(
                        Div("📦", cls="feature-icon"),
                        H3("Parcel Machine Integration"),
                        P("Seamless rental delivery and return through integrated parcel machine network."),
                        cls="feature-card"
                    ),
                    cls="features-grid"
                ),
                cls="features-container"
            ),
            cls="features",
            id="features"
        ), \
        Section(
            Div(
                H2("Choose Your Plan"),
                Div(
                    Div(
                        H3("Free Plan"),
                        Div("€0", cls="price"),
                        P("per month"),
                        Ul(
                            Li("1 User / 1 Account"),
                            Li("Rental Management"),
                            Li("Digital Signatures"),
                            Li("9% Transaction Fee"),
                            style="text-align: left; margin: 1rem 0;"
                        ),
                        A("Get Started", href="#", cls="btn btn-outline"),
                        cls="pricing-card"
                    ),
                    Div(
                        H3("Business Plan"),
                        Div("€59", cls="price"),
                        P("per month (annual billing)"),
                        Ul(
                            Li("All Free Plan Features"),
                            Li("Max 10 Users"),
                            Li("Max 5 Locations"),
                            Li("API Integrations"),
                            Li("0% Transaction Fee"),
                            style="text-align: left; margin: 1rem 0;"
                        ),
                        A("Choose Plan", href="#", cls="btn btn-primary"),
                        cls="pricing-card featured"
                    ),
                    Div(
                        H3("Premium Plan"),
                        Div("€99", cls="price"),
                        P("per month (annual billing)"),
                        Ul(
                            Li("All Business Plan Features"),
                            Li("Max 100 Users"),
                            Li("Max 50 Locations"),
                            Li("Advanced API Access"),
                            Li("Full Service Support"),
                            style="text-align: left; margin: 1rem 0;"
                        ),
                        A("Choose Plan", href="#", cls="btn btn-outline"),
                        cls="pricing-card"
                    ),
                    cls="pricing-grid"
                ),
                cls="pricing-container"
            ),
            cls="pricing",
            id="pricing"
        ), \
        Footer(
            P("© 2024 Rental Manager. All rights reserved."),
            cls="footer",
            id="contact"
        )

serve()

