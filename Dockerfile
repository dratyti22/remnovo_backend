FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ARG DEBIAN_FRONTEND=noninteractive

# Установка зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3-pip \
     && \
    apt-get clean

# Обновление pip
RUN pip install --upgrade pip --no-cache-dir

# Копирование проекта
COPY . /app/

# Установка зависимостей для проекта
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt --no-cache-dir


# Установка прав доступа
RUN chmod -R 755 /app/

# Очистка
RUN rm -rf /var/lib/apt/lists/*
