<h1>Описание</h1>

API для проекта социальной сети YaTube, основанный на Django-Rest-Framework

Функционал включает в себя:

1. Авторизацию по JWT (JSON Web Token) токену
2. Сериализацию данных для всех моделей проекта (Post, Comment, Group, Follow)
3. Обработку GET, POST, PATCH, PUT и DELETE запросов к базе данных YaTube

<h1>Установка</h1>

1. Склонировать репозиторий
2. Создать и активировать виртуальное окружение для проекта


        python -m venv venv

    unix консоль:

        source venv/scripts/activate

    windows консоль:

        venv/scripts/activate.bat

3. Установить зависимости и сделать миграции

        python pip install -r requirements.txt
        python manage.py makemigrations
        python manage.py migrate
    
4. Запустить сервер

        python manage.py runserver

<h1>Примеры использования</h1>

+ **Получение токена авторизации**

    <h3>Request</h3>

        POST /api/v1/token/
        form-data: {"username": "username_string", "password": "password_string"}
    
    <h3>Response</h3>

        {
            "refresh": "<JRW-refresh-token>",
            "access": "<JRW-access-token>",
        }
    
+ **Обновление токена**

    <h3>Request</h3>

        POST /api/v1/token/refresh/
        form-data: {"refresh": "JRW-refresh-token"}
    
    <h3>Response</h3>

        {
            "access": "<new-JRW-access-token>"
        }
    
+ **Получение списка всех постов**

    <h3>Request</h3>

        GET /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    
    <h3>Response</h3>

        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
    
+ **Создание нового поста**

    <h3>Request</h3>

        POST /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}

    <h3>Response</h3>

        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    
+ **Получение поста по его id**

    <h3>Request</h3>

        GET /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}

    <h3>Response</h3>

        status_code: 200
        {
            "id": <post_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    
+ **Обновление поста по его id**

    <h3>Request</h3>

        PUT /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}

    <h3>Response</h3>

        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    
+ **Частичное обновление поста по его id**

    <h3>Request</h3>

        PATCH /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}

    <h3>Response</h3>

        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
+ **Удаление поста по его id**

    <h3>Request</h3>
    
        DELETE /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
        
    <h3>Response</h3>
    
        status_code: 204
        
+ **Получение списка всех комментариев**

    <h3>Request</h3>
    
        GET /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        
    <h3>Response</h3>

        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
  
+ **Создание нового комментария**

    <h3>Request</h3>
    
        POST /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
        
    <h3>Response</h3>
    
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
        
+ **Получение комментария по его id**

    <h3>Request</h3>
    
        POST /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}

    <h3>Response</h3>
    
        status_code: 200
        {
            "id": <comment_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
        
+ **Обновление комментария по его id**

    <h3>Request</h3>
    
        PUT /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}

    <h3>Response</h3>
    
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

+ **Частичное обновление комментария по его id**

    <h3>Request</h3>
    
        PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
        
    <h3>Response</h3>
    
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
        
+ **Удаление комментария по его id**

    <h3>Request</h3>
    
        DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}

    <h3>Response</h3>
    
        status_code: 204

+ **Получение списка всех подписчиков**

    <h3>Request</h3>
    
        GET /api/v1/follow/?search={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}

    <h3>Response</h3>
    
        status_code: 200
        [
            {
                "user": "string",
                "following": "string"
            },
            ...
        ]
        
+ **Создание подписки**

    <h3>Request</h3>
    
        POST /api/v1/follow/?user={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"following": "string"}

    <h3>Response</h3>
    
        status_code: 200
        {
            "user": "string",
            "following": "string"
        }
  
+ **Получение списка всех групп**

    <h3>Request</h3>
    
        GET /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}

    <h3>Response</h3>
    
        status_code: 200
        [
            {
                "title": "string"
            },
            ...
        ]

+ **Создание новой группы**

    <h3>Request</h3>
    
        POST /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"title": "string"}

    <h3>Response</h3>
    
        status_code: 200
        {
            "title": "string"
        }
