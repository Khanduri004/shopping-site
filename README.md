# 🛍️ Shopping Site

A simple Flask-based shopping website built for learning and practicing Docker, Flask, and web development fundamentals.

What is a Flask App?
A Flask app is a Python program that runs a web server and shows web pages when you visit it in your browser.

It's like teaching Python how to behave like a mini-website backend.

You write Python code, and Flask helps turn that into:

-Web pages (like home page, about page)

-APIs (data that apps or JavaScript can fetch)

-Web forms (like login, search, checkout)

✅ Think of it like this:
Flask is like a chef 👨‍🍳:

You tell it what you want (“user profile page”), and it makes it on demand from scratch using Python and templates.

Nginx or static web server is like a vending machine 🥤:

It just gives you pre-made files (HTML, CSS, images) — nothing more, nothing less.

🧠 When is Flask used?
Use Flask when:

You want logic like user login/signup

You’re connecting to a database

You want to return dynamic pages

You’re building an API

🌐 When is Nginx used?
Use Nginx when:

You're just serving static websites (plain HTML)

Or, as a reverse proxy to forward requests to a backend app (like Flask)


---

## 📁 Project Structure

shopping-site/
│
├── app/ # Main application code
│ ├── init.py # Initializes Flask app
│ ├── routes.py # Web routes (URLs)
│ ├── models.py # Data models (Product, Cart)
│ └── templates/ # HTML templates (views)
│ └── index.html
│
├── static/ # CSS, JS, and images
│ └── style.css
│
├── app.py # Main file to run the app
├── Dockerfile # Docker build instructions
├── docker-compose.yml # Docker services configuration
├── requirements.txt # List of Python dependencies
└── README.md # You're here
```



## 🚀 Features

- Flask web server
- Basic product catalog and cart logic
- Dockerized (easily run anywhere)
- Hot reload with development server
- HTML templating with Jinja2


## 🐳 Run with Docker

### 🧱 Step-by-step

```bash
# Clone the repo
git clone https://github.com/Khanduri004/shopping-site.git
cd shopping-site

# Build and run the container
docker-compose up --build

🌐 Access the app
Visit your browser at:
```bash
http://localhost:5000
```

If running on a cloud server (like AWS EC2), use:

```bash
http://<your-ec2-ip>:5000
```

🧪 Tech Stack
  - Python
  - Flask
  - Jinja2 (Templating)
  - Docker
  - HTML/CSS

📝 License
This project is for educational purposes. You are free to use, modify, and build upon it.

🙋‍♂️ Author
@Khanduri004 
