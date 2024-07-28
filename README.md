# Project_Customer_Churn_Forecasting

Customer Churn Forecasting for a Telecommunications Company



 https://pr-cust-churn-forecast.streamlit.app/



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
- **rf_model.pkl**                     : Збережена модель Random Forest.
- **scaler.pkl**                       : Збережений скейлер для нормалізації даних.




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

