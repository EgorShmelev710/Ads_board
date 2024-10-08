﻿# Ads_board - Доска объявлений

## Описание

Это backend-часть для сайта объявлений. Она включает в себя следующий функционал:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте.
- Возможность оставлять отзывы под каждым объявлением .
- Возможность осуществлять поиск объявлений по названию в заголовке сайта.

## Технологии

- Python
- Django
- DRF
- PostgreSQL
- Docker
- Pytest

## Настройка проекта

### Клонирование проекта

Для работы с проектом клонируйте репозиторий

  ```sh
  git clone git@github.com:EgorShmelev710/Diploma_work.git
  ```

### Настройка .env и .env.docker файлов

Проект может быть запущен двумя способами. С помощью docker или на локальном сервере.

1) Docker - настройте файл .env.docker, опираясь на .env.sample, а в файле .env укажите DOCKER_ENV=True


- В корне проекта переименуйте файл .env.sample в .env.docker и отредактируйте параметры:
    ```text
    SECRET_KEY=секретный ключ джанго

    POSTGRES_DB=название базы данных
    POSTGRES_USER=pпользователь базы данных
    POSTGRES_PASSWORD=ваш пароль
    POSTGRES_HOST=хост докеровской базы данных
    POSTGRES_PORT=порт
    
    TIME_ZONE=ваш часовой пояс
    
    EMAIL_HOST=почтовый хост
    EMAIL_PORT=почтовый порт
    EMAIL_HOST_USER=почта, с которой будут отправляться письма
    EMAIL_HOST_PASSWORD=пароль
    EMAIL_USE_TLS=False
    EMAIL_USE_SSL=True
    
    BASE_URL=http://localhost:8000 # укажите url своего хоста
    ```
- Создайте файл .env и добавьте туда параметр DOCKER_ENV=True
- Запустите проект командой docker-compose up -d --build

2) Локально - настройте файл .env и укажите в нем DOCKER_ENV=False

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    SECRET_KEY=секретный ключ джанго

    POSTGRES_DB=название базы данных
    POSTGRES_USER=pпользователь базы данных
    POSTGRES_PASSWORD=ваш пароль
    POSTGRES_HOST=хост докеровской базы данных
    POSTGRES_PORT=порт
    
    TIME_ZONE=ваш часовой пояс
    
    EMAIL_HOST=почтовый хост
    EMAIL_PORT=почтовый порт
    EMAIL_HOST_USER=почта, с которой будут отправляться письма
    EMAIL_HOST_PASSWORD=пароль
    EMAIL_USE_TLS=False
    EMAIL_USE_SSL=True
    
    BASE_URL=http://localhost:8000 # укажите url своего хоста
  
    DOCKER_ENV=False
    ```

## Использование

Есть 2 варианта использования:

1) Локально у себя на компьютере:

- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```

2) Через Docker:

- Убедитесь, что у вас установлен Docker

- В терминале введите команду:
  ```text
  docker-compose up -d --build
  ```

### Документация

Для всего проекта есть документация. Она доступна по адресу http://localhost:8000/swagger/ или в другом
формате  http://localhost:8000/redoc/ после запуска сервера.

## Контакты

Ссылка на репозиторий: [https://github.com/EgorShmelev710](https://github.com/EgorShmelev710)



