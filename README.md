# Social-Network
Simple REST API based social network in Django and Python


# Project Startup:

- migrations: 
```
python manage.py makemigrations social

python manage.py migrate social

python manage.py migrate


```
- run the server

```
python manage.py runserver 

```
# Bot usage:
- python manage.py bot --data json_file_path
- there is example data in /social/bot/data.json


# Endpoints:

    - signup:
        /auth/register/
        method POST
        payload_to_create={"username": username, "email": email, "password": password}
        respone serialized data

    - login:
        /auth/login/
        method POST
        payload_to_create={"username": username, "password": password}
        respone user serialized data and auth cred


    - posts:
        /post/
            methods (GET, POST, PATCH)
            payload_to_create={"title", title, "text": text}
            response serialized data

        /post/{id}/like/
        methods POST
        response 201

        /post/{id}/dislike/
        methods DELETE
        response 201

# 3rd party:

- username-generator
- pyhunter --> for email existence check
- clearbit --> enriching user data on sing up
