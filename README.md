# Advanced Blog Application

This is a Django-based web application that allows users to read blog content and to comment on them. Users can  view, share and comment on books, as well as subscribe to a feed.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)

## Features

- **View Blogs**: Get access to blog content published in the website.
- **Search for blogs**: Exploit the full-text search capabilities of Postgresql to search for blog content.
- **Comment on blogs**: Write comments on blog content published
- **Share blogs**: Share blogs via email to recommend others read blog posts
- **Subscribe to feed**: Subscribe to a feed to get access to new blog content
- **Smart recommendation and categorization using tags**

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.10+**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python package installer. It typically comes with Python.
- **Git**: For version control. Download from [git-scm.com](https://git-scm.com/).
- **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

## Usage

Follow these steps to set up and run the Book Collections application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/abeni-al7/advanced-blog-django.git
cd advanced-blog-django
```

### 2. Create a Virtual Environment

```bash
python3 -m venv my_venv
```

### 3. Activate the Virtual Environment

```bash
source my_env/bin/activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### 5. Set Up Environment Variables
```bash
cp .env.example .env
```
Edit the .env file with your configurations
### 6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Run the app
```bash
python manage.py runserver
```
