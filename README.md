Simple Toy Project - Scrap html text and analyse
=====================

# 1. Installation
## 1.1 Dependencies
The key dependencies including django are written in requirements.txt file.
The dependencies are:
      1. asgiref==3.2.3
      2. certifi==2019.11.28
      3. chardet==3.0.4
      4. Django==3.0.3
      5. idna==2.9
      6. pytz==2019.3
      7. requests==2.23.0
      8. sqlparse==0.3.0
      9. urllib3==1.25.8

## 1.2 Django Environment      
If you already installed django environment as above, you don't need to build the Dockerfile and make a docker container.
Just run this command
>   >   > python manage.py runserver

## 1.3 Build a Dockerfile
If your local environment are too complicated to manage, then I recommend to build the Dockerfile.
>   >   > (sudo) docker build -t {container name} .
>   >   > docker run -d -p 8000:8000 {container name}

# 2. Connect the django server
After starting django server either the method explained in 1.2 or the method explained in 1.3, you can browse django template
at http://127.0.0.1:8000/dashboard/ 


