# Profiles REST API
Profiles REST API made in Python and DJANGO framework.
## Vagrant configuration
- Instal virtual machine and get shh conection with it
```sh
 vagrant up
 vagrant ssh
```

## Create Python Virtual Environment
> Docs: https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/

```sh
 cd /vagrant
 python -m venv ~/env
 # Activate Python Env
 source ~/env/bin/activate
 # Deactivate Python Env
 deactivate
```
## Install Required Packages
> Docs: https://pypi.org/

- Set requirements.txt file 

```sh
 django==2.2
 djangorestframework==3.9.2
```
- Activate python env
```sh
 vagrant ssh
 cd /vagrant
 source ~/env/bin/activate
```
- Install requirements
```sh
 pip install -r requirements.txt
```
## Create new Django Project
- In python env active {package, action, name, location}
```sh
 django-admin.py startproject profiles_project .
```

## Create Django App
- In python env active {package, django project file, action, name }
```sh
 python manage.py startapp profiles_api
```

## Enable Django Api in Django Project
- In profiles_project file, add in INSTALLED_APPS 
```sh
  'rest_framework',
  'rest_framework.authtoken',
  'profiles_api'
```
- Save file

## Test
- In Python env 

```sh
  python manage.py runserver 0.0.0.0:8000
```

## Create models
> Docs: https://docs.djangoproject.com/en/1.11/ref/models/fields/
> Docs: https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user
> Docs: https://peps.python.org/pep-0008/

- Create User Profile model
- Create User Manager Profile

## Migrations

- Run in Python env

```sh
  python manage.py makemigrations profiles_api
```




