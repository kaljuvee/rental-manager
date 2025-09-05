# Rentster Business Logic Analysis

## Platform Overview
Rentster is a comprehensive rental marketplace platform that connects rental service providers with customers. It operates as a two-sided marketplace with advanced features for digital rental management.

## Core Business Model

### Two-Sided Marketplace
1. **Customers**: Browse, search, and rent items from various providers
2. **Service Providers**: List rental items, manage inventory, and earn revenue

### Key Features Discovered

#### Customer Side
1. **Search & Discovery**
   - Location-based search with map integration
   - Category-based browsing (27+ categories)
   - Date/time availability filtering
   - Real-time search functionality

2. **Booking System**
   - Calendar-based availability selection
   - Flexible pricing (hourly, daily, monthly, per usage)
   - Quantity selection
   - Real-time pricing calculation
   - VAT handling

3. **User Account Management**
   - Order history ("My orders")
   - Access management ("My accesses")
   - Account balance system
   - Profile management
   - Provider upgrade option

#### Provider Side
1. **Provider Onboarding**
   - 4-step registration process:
     - Brand name
     - Contact information
     - Locations
     - Juridical details

2. **Item Management**
   - Multiple item categories
   - Detailed item descriptions
   - Multiple image uploads
   - Pricing configuration
   - Availability calendar management

3. **Advanced Features**
   - Contactless rental capability
   - 24/7 availability badges
   - Location mapping with Google Maps
   - Digital signatures integration (Dokobit)

#### Platform Features
1. **Digital Transformation**
   - "Make all rental agreements digital"
   - Automated processes
   - Contactless operations
   - Digital signature integration

2. **Geographic Coverage**
   - Estonia-focused platform
   - Multiple cities supported
   - Map-based provider discovery

3. **Technology Integration**
   - Google Maps integration
   - Calendar synchronization
   - Payment processing
   - Mobile-responsive design

## Data Model Requirements

### Core Entities
1. **Users** (customers and providers)
2. **Companies** (rental service providers)
3. **Rental Items** (inventory)
4. **Categories** (item classification)
5. **Bookings** (rental transactions)
6. **Locations** (geographic data)
7. **Payments** (financial transactions)
8. **Reviews** (feedback system)
9. **Access Control** (contactless features)

### Key Relationships
- Users can be both customers and providers
- Companies have multiple locations
- Items belong to categories and companies
- Bookings connect users, items, and time slots
- Payments are linked to bookings

## Technical Architecture
- Frontend: Customer-facing marketplace
- Backend: Provider management system
- Database: Comprehensive rental management
- Integrations: Maps, payments, digital signatures
- Mobile: Responsive web application

## Revenue Model
- Commission-based (likely percentage of transactions)
- Provider subscription fees (based on pricing tiers)
- Premium features for providers
- Transaction processing fees

## Competitive Advantages
1. Contactless rental capability
2. Digital signature integration
3. Comprehensive provider tools
4. Geographic market focus
5. Multi-category support
6. Advanced calendar integration

