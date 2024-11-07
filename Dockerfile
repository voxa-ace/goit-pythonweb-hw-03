FROM python:3.9-slim

WORKDIR /app

# Копіюємо файли проекту до контейнера
COPY app.py ./
COPY error.html ./
COPY index.html ./
COPY message.html ./
COPY read.html ./
COPY style.css ./
COPY logo.png ./

RUN pip install flask

RUN mkdir -p /app/storage

# Вказуємо порт, який використовує додаток
EXPOSE 3000

CMD ["python", "app.py"]
