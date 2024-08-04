# Blog Project

## Overview

This is a website where users can create a blog to post their ideas and other users can join this blog to discuss by giving comments. This README provides an overview of the project's architecture, including the technologies used and instructions for setting up the development environment.

## Features

- **User Authentication**: Secure user authentication using the Django authentication system.
- **Database Management**: PostgreSQL for robust and scalable database management.
- **Redis**: Redis is an in-memory data store used by millions of developers as a cache, vector database, document database, streaming engine, and message broker.
- **ORM**: Object-Relational Mapping (ORM) for seamless interaction with the database.
- **Containerization**: Docker for containerizing the application, ensuring consistency across different environments.

## Technologies Used


### Python

[Python](https://www.python.org/) is a versatile programming language that allows for rapid development and deployment. It is widely used in web development, data analysis, artificial intelligence, and more.

### Django

[Django](https://docs.djangoproject.com) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### PostgreSQL

[PostgreSQL](https://www.postgresql.org/) is a powerful, open-source object-relational database system with over 30 years of active development. It is known for its reliability, robustness, and performance.

### Redis

[Redis](https://redis.io/) is an in-memory data store used by millions of developers as a cache, vector database, document database, streaming engine, and message broker. Redis has built-in replication and different levels of on-disk persistence. It supports complex data types (for example, strings, hashes, lists, sets, sorted sets, and JSON), with atomic operations defined on those data types.

### Docker

[Docker](https://www.docker.com/) is a distributed event streaming platform capable of handling trillions of events a day. It is used in this project to manage real-time messaging and event streaming.

### ORM

An Object-Relational Mapper (ORM) is used to interact with the database in an object-oriented manner. This project uses SQLAlchemy to handle the database operations seamlessly.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install virtualenv

python3 -m venv env

source env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
```

## Run

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
