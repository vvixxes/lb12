# Используем базовый образ Python
FROM python:3.11-slim AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости в промежуточном образе
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости из первого этапа
COPY --from=builder /install /usr/local

# Копируем файлы проекта в контейнер
COPY . .

# Открываем порт для приложения
EXPOSE 8000

# Указываем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]