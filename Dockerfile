FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
# Устанавливаем через pip зависимости
RUN python -m pip install --no-cache -r requirements.txt
# Копируем код приложения
COPY project project
COPY tests tests
COPY constants.py .
COPY container.py .
COPY create_tables.py .
COPY fixtures.json .
COPY load_fixtures.py .
COPY entrypoint.sh .
COPY app.py .

CMD ["sh", "entrypoint.sh"]