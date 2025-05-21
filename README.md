# myblog

## Описание

Этот Django проект представляет собой платформу для блогов. Он позволяет пользователям просматривать различные посты, а зарегистрированным пользователям - создавать собственные посты и оставлять комментарии под своими или чужими.

## Установка

1. Клонировать репозиторий:

    ```bash
    git clone <ссылка на репозиторий>
    ```

2. Cоздать и активировать виртуальное окружение:

    ```bash
    python3 -m venv venv

    source venv/bin/activate
    ```

    Если у вас Windows, то процесс будет таким:

    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```

3. Обновить pip. Далее установить зависимости из файла requirements.txt:

    ```bash
    python3 -m pip install --upgrade pip

    pip install -r requirements.txt
    ```

    Для Windows:

    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Перейти в папку с проектом, выполнить миграции и запустить сервер.

    ```bash
    cd myblog/
    python3 manage.py migrate
    python3 manage.py runserver
    ```

    Для Windows:
    ```bash
    cd myblog/
    python manage.py migrate
    python manage.py runserver
    ```