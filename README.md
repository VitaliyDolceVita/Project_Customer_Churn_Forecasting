# Project_Customer_Churn_Forecasting
Customer Churn Forecasting for a Telecommunications Company



 https://pr-cust-churn-forecast.streamlit.app/



                           Проект складаэться з наступних файлів :



Dockerfile                       : Визначає середовище для запуску застосунку.
docker-compose.yml               : Конфігураційний файл для Docker Compose.
requirements.txt                 : Список залежностей Python для проекту.
app.py                           : Головний файл застосунку Streamlit.
data.xlsx                        : Вхідні дані у форматі Excel.
internet_service_churn.csv       : Додаткові вхідні дані у форматі CSV.
project_chornovuk.ipynb          : Jupyter Notebook з аналізом даних.
data_distrib.ipynb               : Jupyter Notebook з попереднім вивченням розподілу даних.
rf_model.pkl                     : Файл збереженої моделі Random Forest.
scaler.pkl                       : Файл збереженого масштабувальника даних.




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

