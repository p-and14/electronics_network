Electronics Network
========
________
#### *API-приложение сети по продаже электроники*
________
## Stack:
- Python 3.10
- Django
- Django REST framework 3.10
- Postgres
___
## Project launch:
1. Создать виртуальное окружение.
2. Установить зависимости:
> pip install -r requirements.txt
3. Создать ".env" файл на примере ".env_example".
4. Создать БД:
   1. Установить к себе на компьютер по инструкции из [официальной документации](https://www.postgresql.org/download/). 
   2. Установить docker-контейнер с уже готовой и настроенной СУБД. 
    > docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres
5. Создать миграцию для приложений:
> python manage.py makemigrations 
6. Применить все миграции:
> python manage.py migrate
