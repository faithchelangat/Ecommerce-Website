# E-Commerce Website

A full-stack e-commerce web application built with **Python and Django**, providing an online shopping platform with product browsing, shopping cart management, and payment processing.

## Features

* 🛍️ Product browsing and storefront
* 🛒 Shopping cart functionality
* 💳 Payment processing
* 📦 Product management
* 🖼️ Product image and media management
* 🔐 Django-based backend
* 📱 Responsive web interface
* ⚙️ Static and media file management
* 🚀 Deployment configuration

## Technology Stack

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Backend programming language |
| Django       | Web framework                |
| HTML         | Page structure               |
| CSS          | Styling                      |
| JavaScript   | Client-side functionality    |
| SQLite       | Database                     |
| Git & GitHub | Version control              |

## Project Structure

```text
Ecommerce-Website/
│
├── cart/               # Shopping cart functionality
├── ecommerce/          # Main Django project configuration
├── payment/            # Payment processing functionality
├── storefront/         # Products and storefront functionality
├── media/              # Uploaded product media
├── static/             # CSS, JavaScript and static assets
├── templates/          # HTML templates
├── manage.py            # Django management utility
├── requirements.txt     # Python dependencies
├── Procfile             # Deployment configuration
└── runtime.txt          # Python runtime configuration
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/faithchelangat/Ecommerce-Website.git
cd Ecommerce-Website
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Application Overview

The application is organized into separate Django applications responsible for different areas of the e-commerce platform.

### Storefront

Handles product presentation and the online shopping experience.

### Cart

Provides functionality for adding products to a shopping cart, managing cart items, and preparing orders.

### Payment

Handles the payment-processing workflow within the application.

## Future Improvements

Potential improvements include:

* User registration and customer profiles
* Order history and order tracking
* Product reviews and ratings
* Advanced product search and filtering
* Inventory management
* Multiple payment methods
* REST API integration
* Automated testing
* Production database configuration
* Improved security and deployment configuration

## Author

**Faith Chelangat**

Computer Science Graduate | Software Developer

GitHub: [@faithchelangat](https://github.com/faithchelangat)
