# Django Ecommerce Website

A full-stack **e-commerce web application built with Django** that allows users to browse products, filter products by category, search for products, add items to a shopping cart, and proceed through the checkout process.

The project demonstrates practical experience in **Python, Django, PostgreSQL, HTML, CSS, Bootstrap, JavaScript, database management, and deployment**.

## Live Demo

**Live Website:** https://ecommerce-website-1-rbvf.onrender.com

## GitHub Repository

https://github.com/faithchelangat/Ecommerce-Website

---

## Features

### Product Management

* Display products dynamically from the database
* Product categories
* Product detail pages
* Product pricing and sale prices
* Product images
* Product descriptions
* Sale/discount support

### Product Discovery

* Browse products by category
* Search for products
* View individual product details

### Shopping Cart

* Add products to cart
* Update product quantities
* Remove products from cart
* Calculate cart totals

### Checkout & Payments

* Checkout workflow
* Customer billing information
* PayPal payment integration
* PayPal sandbox/test environment support

### Administration

* Django Admin interface
* Manage products and categories
* Manage users and application data

### Production Deployment

* Deployed on Render
* PostgreSQL database support
* Static files served using WhiteNoise
* Production configuration with `DEBUG=False`
* Gunicorn application server
* Automated database migrations during deployment
* Automated static file collection

---

## Technologies Used

| Technology   | Purpose                    |
| ------------ | -------------------------- |
| Python       | Backend programming        |
| Django       | Web application framework  |
| PostgreSQL   | Production database        |
| SQLite       | Local development database |
| HTML5        | Page structure             |
| CSS3         | Styling                    |
| Bootstrap    | Responsive UI              |
| JavaScript   | Client-side functionality  |
| PayPal       | Payment integration        |
| WhiteNoise   | Static file serving        |
| Gunicorn     | Production WSGI server     |
| Render       | Cloud deployment           |
| Git & GitHub | Version control            |

---

## Project Structure

```text
Ecommerce-Website/
│
├── cart/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── context_processors.py
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── payment/
│   ├── views.py
│   └── urls.py
│
├── storefront/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── management/
│
├── static/
│   └── uploads/
│       └── product/
│
├── media/
│   └── uploads/
│
├── manage.py
├── requirements.txt
├── build.sh
├── runtime.txt
└── ecommerce_data.json
```

---

## Database

The application uses Django's ORM to manage application data.

The main product models include:

### Category

Stores product categories such as:

* Cell Phones
* Novels
* Beauty Products

### Product

Stores:

* Product name
* Price
* Sale price
* Category
* Description
* Product image
* Sale status

The project uses **SQLite during local development** and **PostgreSQL in production**.

---

## Production Deployment

The application is deployed on **Render** using:

```text
Gunicorn
    ↓
Django
    ↓
PostgreSQL
```

The deployment process runs the following build script:

```bash
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py load_ecommerce_data
```

### Production Configuration

The application uses environment variables for sensitive configuration:

```text
SECRET_KEY
DATABASE_URL
DEBUG
PAYPAL_RECEIVER_EMAIL
```

`DEBUG` is disabled in production:

```python
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

This prevents Django's detailed debugging information from being exposed to website visitors.

---

## Static Files

Static files are handled using **WhiteNoise**.

```python
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
```

Product images used as fixed portfolio assets are stored under:

```text
static/uploads/product/
```

and served using Django's static-file system.

---

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/faithchelangat/Ecommerce-Website.git
```

### 2. Navigate into the project

```bash
cd Ecommerce-Website
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv virt
```

Activate it:

```bash
virt\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv virt
source virt/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Load sample ecommerce data

```bash
python manage.py load_ecommerce_data
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Environment Variables

Create the required environment variables for local/production use.

Example:

```text
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
PAYPAL_RECEIVER_EMAIL=your-paypal-email
```

Do not commit production credentials or secret keys to GitHub.

---

## Problem Solved

Many small businesses require an online platform where customers can discover products, view prices, manage shopping carts, and complete purchases.

This project demonstrates how a traditional product catalogue can be transformed into a **database-driven e-commerce platform** with:

* Dynamic product management
* Category-based organization
* Search functionality
* Shopping cart functionality
* Checkout processing
* Payment integration
* Database persistence
* Responsive design
* Cloud deployment

The project also demonstrates the ability to take a Django application from **local development to a production environment**.

---

## Key Development Challenges

### Production Database Configuration

The project was configured to support different databases depending on the environment:

* SQLite for local development
* PostgreSQL for production

This allowed development to remain simple while using a production-ready relational database in deployment.

### Static File Management

Production deployment required proper handling of Django static files. WhiteNoise and `collectstatic` were configured to allow the application to serve static assets correctly when:

```python
DEBUG=False
```

### Production Data Loading

A custom Django management command was created to load the ecommerce categories and products:

```bash
python manage.py load_ecommerce_data
```

The command uses `update_or_create`, allowing the deployment process to load data without unnecessarily creating duplicate records.

---

## Future Improvements

Planned improvements include:

* User registration and authentication
* Customer order history
* Order confirmation emails
* Improved payment processing
* Persistent production media storage using Cloudinary or Amazon S3
* Product reviews and ratings
* Wishlist functionality
* Inventory management
* Advanced product filtering
* Improved checkout experience
* Automated testing
* CI/CD pipeline

---

## Author

**Faith Chelangat**

Computer Science graduate and software developer focused on building practical web applications using **Python, Django, JavaScript, React, and modern backend and frontend technologies**.

### Portfolio

GitHub: https://github.com/faithchelangat

---

## License

This project is intended primarily as a portfolio and learning project.
