from fasthtml.common import *

app, rt = fast_app()

def create_header():
    return Nav(
        Div(
            A(
                Img(src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23667eea'%3E%3Cpath d='M12 2L2 7v10c0 5.55 3.84 10 9 11 1.09.2 2.91.2 4 0 5.16-1 9-5.45 9-11V7l-10-5z'/%3E%3C/svg%3E", 
                     alt="Rental Manager", style="width: 32px; height: 32px;"),
                Span("Rental Manager", style="font-size: 20px; font-weight: bold; color: #1f2937; margin-left: 8px;"),
                href="/", style="display: flex; align-items: center; text-decoration: none;"
            ),
            style="display: flex; align-items: center;"
        ),
        Div(
            A("Features", href="#features", style="color: #6b7280; text-decoration: none; padding: 8px 16px; border-radius: 6px; transition: all 0.2s;"),
            A("About", href="#about", style="color: #6b7280; text-decoration: none; padding: 8px 16px; border-radius: 6px; transition: all 0.2s;"),
            A("Contact", href="#contact", style="color: #6b7280; text-decoration: none; padding: 8px 16px; border-radius: 6px; transition: all 0.2s;"),
            style="display: flex; gap: 8px; align-items: center;"
        ),
        Div(
            A("Get Started", href="https://rental-manager.streamlit.app/", 
              style="background: #667eea; color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 500; transition: all 0.2s;"),
            style="display: flex; align-items: center;"
        ),
        style="display: flex; justify-content: space-between; align-items: center; padding: 16px 32px; background: white; border-bottom: 1px solid #e5e7eb; position: sticky; top: 0; z-index: 50;"
    )

def create_hero():
    return Section(
        Div(
            Div(
                H1("All-in-One", style="font-size: 4rem; font-weight: bold; color: #1f2937; margin-bottom: 16px; line-height: 1.1;"),
                H1(
                    Span("Smart assistant", style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;"),
                    " for rental managers",
                    style="font-size: 4rem; font-weight: bold; color: #1f2937; margin-bottom: 24px; line-height: 1.1;"
                ),
                P("Streamline your rental business with AI-powered automation, smart analytics, and seamless property management tools.", 
                  style="font-size: 1.25rem; color: #6b7280; margin-bottom: 32px; max-width: 600px; line-height: 1.6;"),
                Div(
                    A("Start Managing", href="https://rental-manager.streamlit.app/", 
                      style="background: #1f2937; color: white; padding: 16px 32px; border-radius: 12px; text-decoration: none; font-weight: 600; font-size: 1.1rem; margin-right: 16px; display: inline-block; transition: all 0.2s;"),
                    A("View Demo", href="#demo", 
                      style="background: transparent; color: #667eea; padding: 16px 32px; border: 2px solid #667eea; border-radius: 12px; text-decoration: none; font-weight: 600; font-size: 1.1rem; display: inline-block; transition: all 0.2s;"),
                    style="margin-top: 16px;"
                ),
                style="text-align: center; max-width: 800px; margin: 0 auto;"
            ),
            style="padding: 80px 32px; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); min-height: 600px; display: flex; align-items: center; justify-content: center;"
        ),
        id="hero"
    )

def create_features():
    features = [
        {
            "icon": "🏠",
            "title": "Smart Property Management",
            "description": "Automated booking management, calendar synchronization, and intelligent pricing optimization for maximum revenue."
        },
        {
            "icon": "📊",
            "title": "Advanced Analytics",
            "description": "Real-time insights into your rental performance, revenue trends, and customer behavior patterns."
        },
        {
            "icon": "🤖",
            "title": "AI-Powered Automation",
            "description": "Intelligent task management, automated communications, and smart maintenance scheduling."
        },
        {
            "icon": "📱",
            "title": "Mobile-First Design",
            "description": "Manage your rentals on-the-go with our responsive web application accessible from any device."
        },
        {
            "icon": "💰",
            "title": "Revenue Optimization",
            "description": "Dynamic pricing suggestions, occupancy rate optimization, and profit margin analysis."
        },
        {
            "icon": "🔒",
            "title": "Secure & Reliable",
            "description": "Enterprise-grade security with encrypted data storage and reliable cloud infrastructure."
        }
    ]
    
    return Section(
        Div(
            H2("Everything you need to manage rentals", 
               style="font-size: 2.5rem; font-weight: bold; color: #1f2937; text-align: center; margin-bottom: 16px;"),
            P("Professional-grade tools designed for modern rental managers", 
              style="font-size: 1.2rem; color: #6b7280; text-align: center; margin-bottom: 64px; max-width: 600px; margin-left: auto; margin-right: auto;"),
            Div(
                *[
                    Div(
                        Div(feature["icon"], style="font-size: 3rem; margin-bottom: 16px;"),
                        H3(feature["title"], style="font-size: 1.5rem; font-weight: bold; color: #1f2937; margin-bottom: 12px;"),
                        P(feature["description"], style="color: #6b7280; line-height: 1.6;"),
                        style="background: white; padding: 32px; border-radius: 16px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); text-align: center; transition: all 0.3s;"
                    ) for feature in features
                ],
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px;"
            ),
            style="padding: 80px 32px; max-width: 1200px; margin: 0 auto;"
        ),
        id="features"
    )

def create_categories():
    categories = [
        {
            "title": "Property Management",
            "icon": "🏢",
            "color": "#667eea",
            "features": ["Multi-property dashboard", "Automated bookings", "Calendar sync", "Guest communications"]
        },
        {
            "title": "Analytics & Insights",
            "icon": "📈",
            "color": "#764ba2", 
            "features": ["Revenue tracking", "Performance metrics", "Occupancy rates", "Profit analysis"]
        },
        {
            "title": "Automation Tools",
            "icon": "⚡",
            "color": "#f093fb",
            "features": ["Smart scheduling", "Auto-responses", "Task management", "Maintenance alerts"]
        }
    ]
    
    return Section(
        Div(
            H2("Comprehensive rental management platform", 
               style="font-size: 2.5rem; font-weight: bold; color: #1f2937; text-align: center; margin-bottom: 64px;"),
            Div(
                *[
                    Div(
                        Div(
                            Div(cat["icon"], style=f"font-size: 3rem; color: {cat['color']}; margin-bottom: 16px;"),
                            H3(cat["title"], style="font-size: 1.8rem; font-weight: bold; color: #1f2937; margin-bottom: 20px;"),
                            Ul(
                                *[Li(feature, style="color: #6b7280; margin-bottom: 8px; list-style: none; position: relative; padding-left: 20px;") for feature in cat["features"]],
                                style="padding: 0;"
                            ),
                            style="text-align: center;"
                        ),
                        style=f"background: linear-gradient(135deg, {cat['color']}15 0%, {cat['color']}05 100%); padding: 40px; border-radius: 20px; border: 2px solid {cat['color']}20; transition: all 0.3s;"
                    ) for cat in categories
                ],
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 32px;"
            ),
            style="padding: 80px 32px; max-width: 1200px; margin: 0 auto;"
        ),
        id="categories"
    )

def create_cta():
    return Section(
        Div(
            Div(
                H2("Ready to transform your rental business?", 
                   style="font-size: 2.5rem; font-weight: bold; color: white; margin-bottom: 16px; text-align: center;"),
                P("Join thousands of property managers who trust Rental Manager for their business success.", 
                  style="font-size: 1.2rem; color: rgba(255,255,255,0.9); margin-bottom: 32px; text-align: center; max-width: 600px; margin-left: auto; margin-right: auto;"),
                Div(
                    A("Get Started Now", href="https://rental-manager.streamlit.app/", 
                      style="background: white; color: #667eea; padding: 16px 32px; border-radius: 12px; text-decoration: none; font-weight: 600; font-size: 1.1rem; margin-right: 16px; display: inline-block; transition: all 0.2s;"),
                    style="text-align: center;"
                ),
                style="max-width: 800px; margin: 0 auto;"
            ),
            style="padding: 80px 32px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); text-align: center;"
        ),
        id="cta"
    )

def create_footer():
    return Footer(
        Div(
            Div(
                Div(
                    H4("Rental Manager", style="font-size: 1.2rem; font-weight: bold; color: #1f2937; margin-bottom: 16px;"),
                    P("Smart rental management platform for modern property managers.", 
                      style="color: #6b7280; line-height: 1.6; max-width: 300px;"),
                    style="flex: 1;"
                ),
                Div(
                    H4("Platform", style="font-size: 1.1rem; font-weight: bold; color: #1f2937; margin-bottom: 16px;"),
                    Div(
                        A("Dashboard", href="https://rental-manager.streamlit.app/", style="color: #6b7280; text-decoration: none; display: block; margin-bottom: 8px;"),
                        A("Analytics", href="https://rental-manager.streamlit.app/Analytics", style="color: #6b7280; text-decoration: none; display: block; margin-bottom: 8px;"),
                        A("Calendar", href="https://rental-manager.streamlit.app/Calendar", style="color: #6b7280; text-decoration: none; display: block; margin-bottom: 8px;"),
                    ),
                    style="flex: 1;"
                ),
                Div(
                    H4("Resources", style="font-size: 1.1rem; font-weight: bold; color: #1f2937; margin-bottom: 16px;"),
                    Div(
                        A("Documentation", href="#", style="color: #6b7280; text-decoration: none; display: block; margin-bottom: 8px;"),
                        A("Support", href="#", style="color: #6b7280; text-decoration: none; display: block; margin-bottom: 8px;"),
                        A("GitHub", href="https://github.com/kaljuvee/rental-manager", style="color: #6b7280; text-decoration: none; display: block; margin-bottom: 8px;"),
                    ),
                    style="flex: 1;"
                ),
                style="display: flex; gap: 64px; flex-wrap: wrap;"
            ),
            Hr(style="border: none; border-top: 1px solid #e5e7eb; margin: 32px 0;"),
            Div(
                P("© 2025 Rental Manager. All rights reserved.", style="color: #6b7280; margin: 0;"),
                style="text-align: center;"
            ),
            style="padding: 40px 32px; max-width: 1200px; margin: 0 auto;"
        ),
        style="background: #f9fafb; border-top: 1px solid #e5e7eb;"
    )

@rt("/")
def get():
    return Html(
        Head(
            Title("Rental Manager - Smart Rental Management Platform"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Meta(name="description", content="All-in-one smart assistant for rental managers. Streamline your rental business with AI-powered automation and analytics."),
            Style("""
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #1f2937; }
                a:hover { opacity: 0.8; }
                .feature-item::before { content: '✓'; color: #10b981; font-weight: bold; position: absolute; left: 0; }
                @media (max-width: 768px) {
                    h1 { font-size: 2.5rem !important; }
                    .hero { padding: 40px 16px !important; }
                    .section { padding: 40px 16px !important; }
                    .grid { grid-template-columns: 1fr !important; }
                }
            """)
        ),
        Body(
            create_header(),
            create_hero(),
            create_features(),
            create_categories(),
            create_cta(),
            create_footer()
        )
    )

if __name__ == "__main__":
    serve()

