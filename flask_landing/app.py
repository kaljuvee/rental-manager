from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rental Manager - Rental Management Platform</title>
    <style>
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
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <nav class="nav">
            <div class="logo">Rental Manager</div>
            <ul class="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="auth-buttons">
                <a href="#" class="btn btn-outline">Login</a>
                <a href="#" class="btn btn-primary">Sign Up</a>
            </div>
        </nav>
    </header>
    
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Rental Management Platform</h1>
            <p>Comprehensive rental management solution with digital calendar, order processing, digital signatures, online payments, and contactless rental capabilities.</p>
            <a href="#" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2rem;">Get Started</a>
        </div>
    </section>
    
    <!-- Features Section -->
    <section class="features" id="features">
        <div class="features-container">
            <h2>Core Features</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📅</div>
                    <h3>Synchronized Online Calendar</h3>
                    <p>Integrate with home calendar, phone, Outlook, Mac, or Google Calendar for seamless scheduling.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💳</div>
                    <h3>Payment Links</h3>
                    <p>Integrated payment service for smooth and secure payment experiences without third-party redirects.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🌐</div>
                    <h3>Free Website Platform</h3>
                    <p>Complete rental platform with domain connection for effortless rental management.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">✍️</div>
                    <h3>Digital Signatures</h3>
                    <p>EU-legally binding document signing with automated digital solutions.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔐</div>
                    <h3>Access Management</h3>
                    <p>Integrate rental spaces, parcel machines, and warehouses with smart access control.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📦</div>
                    <h3>Parcel Machine Integration</h3>
                    <p>Seamless rental delivery and return through integrated parcel machine network.</p>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Pricing Section -->
    <section class="pricing" id="pricing">
        <div class="pricing-container">
            <h2>Choose Your Plan</h2>
            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3>Free Plan</h3>
                    <div class="price">€0</div>
                    <p>per month</p>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>1 User / 1 Account</li>
                        <li>Rental Management</li>
                        <li>Digital Signatures</li>
                        <li>9% Transaction Fee</li>
                    </ul>
                    <a href="#" class="btn btn-outline">Get Started</a>
                </div>
                <div class="pricing-card featured">
                    <h3>Business Plan</h3>
                    <div class="price">€59</div>
                    <p>per month (annual billing)</p>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>All Free Plan Features</li>
                        <li>Max 10 Users</li>
                        <li>Max 5 Locations</li>
                        <li>API Integrations</li>
                        <li>0% Transaction Fee</li>
                    </ul>
                    <a href="#" class="btn btn-primary">Choose Plan</a>
                </div>
                <div class="pricing-card">
                    <h3>Premium Plan</h3>
                    <div class="price">€99</div>
                    <p>per month (annual billing)</p>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>All Business Plan Features</li>
                        <li>Max 100 Users</li>
                        <li>Max 50 Locations</li>
                        <li>Advanced API Access</li>
                        <li>Full Service Support</li>
                    </ul>
                    <a href="#" class="btn btn-outline">Choose Plan</a>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Footer -->
    <footer class="footer" id="contact">
        <p>© 2024 Lohusalu Capital Management. All rights reserved.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

