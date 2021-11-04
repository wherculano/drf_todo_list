### "Aprenda Django REST Framework do Zero"

Curso feito na [Udemy](https://www.udemy.com/course/aprenda-django-rest-framework-do-zero/), 
ministrado pelo professor Fernando Augusto.

* Para rodar este projeto é necessário ter instalado o **pipenv**
    ```
    $ python pip install pipenv
    ```
* Com o *pipenv* instalado, basta instalar as dependências do projeto:
    ```
    $ pipenv install
    ```

* Depois basta fazer as migrações para o banco de dados e rodar o sistema:
    ```
    $ pipenv run python manage.py makemigrations
    
    $ pipenv run python manage.py migrate
   
    $ pipenv run python manage.py runserver
    ```
