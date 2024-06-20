# DescriptionFile

информация о DescriptionFile

    Создавать - владелец файла и админ
    Обновлять - владелец файла и админ
    Удалять - владелец файла и админ
    Смотреть - Все

## Путь:

    /api/description/file/

### Пример данных которые приходят:

    {
        "pk": 3,
        "file": "ф",
        "user_id": 2,
        "title": "uuu",
        "description": "uu",
        "line_video": "https://yootube.com/uuu",
        "tags": [
            "a"
        ],
        "image_file": [
            {
                "image": "http://localhost:8000/media/file_image/biker-digital-art-butterflies-uhdpaper.com-4K-6.1044_YbhOmDk.jpg"
            }
        ],
        "time_create": 1718810317
    },

### Данные которые надо отсылать:

    {
        "file": "",
        "title": '',
        "description": '',
        "line_video": '',
        "tags": [],
        "uploaded_images": []
    }

#### Описание полей

file: Уникальное имя для файла \
title: Название. \
description: Описание. \
line_video: Ссылка на видео. \
tags: Список к каким тегам привязан
uploaded_images: Фото
User: Создается автоматически

#### Информация о создание

    Создавать если вместе с фото то через multipart/form-data
    Если без фото то можно через json

    Обновлять без фото можно json
    С фото multipart/form-data

#### Поиск

    /api/description/file/?search=

Поля:

    time_create 
    user__id 
    tags__name
