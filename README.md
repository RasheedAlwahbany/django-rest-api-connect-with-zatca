## Django Rest API To Connect With Zatca API
This is django Rest API app to connect with zatca API

## Project
Django rest API first learning app and connection with **ZATCA API** online

## What is Django?
Django is a free, open source, Python-based web framework that follows the Model-View-Template (MVT) architectural pattern. It reduces the hassle of web development so that you can focus on writing your app instead of reinventing the wheel.

## What is a REST API?
A REST API is a popular way for systems to expose useful functions and data. REST, which stands for representational state transfer, can be made up of one or more resources that can be accessed at a given URL and returned in various formats, like JSON, images, HTML, and more.

## Why Django REST framework?
Django REST framework (DRF) is a powerful and flexible toolkit for building Web APIs. Its main benefit is that it makes serialization much easier.

Django REST framework is based on Django’s class-based views, so it’s an excellent option if you’re familiar with Django. It adopts implementations like class-based views, forms, model validator, QuerySet, and more.

Setting up Django REST framework
Ideally, you’d want to create a virtual environment to isolate dependencies, however, this is optional. Run the command python -m venv django_env from inside your projects folder to create the virtual environment. Then, run source ./django_env/bin/activate to turn it on.

Keep in mind that you’ll need to reactivate your virtual environment in every new terminal session. You’ll know that it is turned on because the environment’s name will become part of the shell prompt.

## How to use 

Navigate to an empty folder in your terminal and install Django and Django REST framework in your project with the commands below:

`pip install django`

Create a Django project called todo with the following command:

`django-admin startproject todo`


`pip install django_rest_framework`

For get json data from outside API:

`pip install requests`



Run your initial migrations of the built-in user model:

`python manage.py migrate`


