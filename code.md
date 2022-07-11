# Django Command

## Display Django All Commands
```bash
Python manage.py 
```
## Start server
```bash
Python manage.py runserver 
```
## Create Project
```bash
Django-admin startproject ProjectName
```
## Create App
```bash
python manage.py startapp app-name
```
## Create a file under app_name/migrations with the database structure to create
```bash
python manage.py makemigrations 
```
## Will read the migrations files and create the actual database and tables
```bash
python manage.py migrate  
```
## Create superuser for authenficiation/admin panel
```bash
python manage.py runserver
```
## Create a requirements file that contain project dependencies & Install Your project requirements.
```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```
## SuperUser 
```bash
python manage.py createsuperuser
```