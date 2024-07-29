# Використовуємо офіційний образ Python 3.8-slim з Docker Hub
FROM python:3.8-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файл із залежностями в контейнер
COPY requirements.txt requirements.txt

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду додатку в контейнер
COPY . .

# Відкриваємо порт, який використовує Streamlit
EXPOSE 8501

# Команда для запуску Streamlit-додатку
CMD ["streamlit", "run", "app.py"]