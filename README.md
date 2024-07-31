# Project_Customer_Churn_Forecasting

Customer Churn Forecasting for a Telecommunications Company

Посилання на ТЗ:
[ТЗ Python Data Science "Прогнозування Відтоку Клієнтів для Телекомунікаційної компанії" - Google Документи](https://docs.google.com/document/d/1d7LTYIQfEAVoK3YZdrlRwlawLBwsfiBJWTVJ-wHpBpA/edit#heading=h.2viv4ety148c)
Посилання на сайт додатку:
https://pr-cust-churn-forecast.streamlit.app/
Посилання на відео інструкцію по запуску докер контейнера:
[Запуск докер контейнера (youtube.com)](https://www.youtube.com/watch?v=QrY3sB23xBY)






                           Проект складаэться з наступних файлів :



- **Dockerfile**                       : Файл для створення Docker образу. Він містить інструкції для   побудови середовища,необхідного для запуску додатку.

- **EDA.ipynb**                        : Jupyter Notebook для обробки даних, аналізу, впровадження алгоритму, навчання та збереження моделі.

- **README.md**                        : Файл з описом проекту та інструкціями для користувача.
- **app.py**                           : Основний скрипт для запуску Streamlit додатку.
- **data.xlsx**                        : Вхідні дані у форматі Excel.
- **data_distrib.ipynb**               : Jupyter Notebook для попереднього вивчення розподілу даних.
- **docker-compose.yml**               : Файл для налаштування та запуску декількох Docker сервісів.
- **internet_service_churn.csv**       : Вхідні дані у форматі CSV.
- **requirements.txt**                 : Файл з переліком залежностей для проекту.
- **rf_modelf1.pkl**                     : Збережена модель Random Forest.
- **scalerf1.pkl**                       : Збережений скейлер для нормалізації даних.




                            Інструкція для розгортання та запуску проекту в Docker




Ці команди потрібно виконати в терміналі вашої операційної системи.

Ось покрокові інструкції для різних операційних систем:

Windows

Відкрийте Command Prompt або PowerShell.

macOS

Відкрийте Terminal.

Linux

Відкрийте Terminal.

Перейдіть в папку,де ви хочете розташувати проект

Введіть команди:

Клонування репозиторію:
Спершу, клонувати репозиторій з проектом на локальну машину.

git clone https://github.com/VitaliyDolceVita/Project_Customer_Churn_Forecasting.git

Перехід до директорії , де знаходиться проект:

cd Project_Customer_Churn_Forecasting

Після виконання цих команд ви будете в папці з проектом, звідки зможете виконувати інші команди для збірки та запуску Docker контейнера.  

Збірка Docker образу:


docker build -t customer_churn_forecasting:latest .


Запуск контейнера з використанням Docker Compose:

docker-compose up


Перевірка роботи застосунку

Відкрийте браузер і перейдіть за адресою: [http://localhost:8501](http://localhost:8501)

За потреби, додаткові команди Docker:

    - Зупинка контейнерів:

      docker-compose down
   
    - Перевірка запущених контейнерів:

      docker ps

    - Підключення до контейнера:

      docker exec -it <container_id> /bin/bash

      Замініть `<container_id>` на фактичний ID контейнера, який можна знайти за допомогою `docker ps`.



                        Для роботи зі свого Docker аккаунту та Docker Hub,виконайте наступне 

Збірка Docker образу:

docker build -t customer_churn_forecasting:latest .

Перед тим як завантажити образ на Docker Hub, вам потрібно залогінитися на Docker Hub. 
Використовуйте команду:

docker login

Вам буде запропоновано ввести ваш логін і пароль від Docker Hub.

Тегуйте ваш образ для Docker Hub. Зазначте репозиторій у вашому обліковому записі на Docker Hub:

docker tag customer_churn_forecasting:latest <your_dockerhub_username>/customer_churn_forecasting:latest

  !!!!!! Замініть <your_dockerhub_username> на ваше ім'я користувача Docker Hub. !!!!

Далі завантажте ваш образ на Docker Hub:

docker push <your_dockerhub_username>/customer_churn_forecasting:latest

  !!!!!! Замініть <your_dockerhub_username> на ваше ім'я користувача Docker Hub. !!!!

Запуск контейнера з використанням Docker Compose:

docker-compose up


