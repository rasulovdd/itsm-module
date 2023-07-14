# ITSM модуль #itsm-module
Модуль для выгрузки очередей и их названия

## Установка

1. Клонируем проект 

    ```bash
    git clone https://github.com/rasulovdd/itsm-module.git
    cd itsm-module
    ```
    ssh
    ```bash
    git clone git@github.com:rasulovdd/itsm-module.git
    cd itsm-module
    ```

2. Установка вертуального окружения для проекта

    ```bash
    python -m venv env
    ```

3. Активируем его 
    
    ```cmd
    .\env\Scripts\activate
    ```

4. Скачиваем библиотеки для проекта
    
    ```bash
    pip install -r requirements.txt
    ```
    
5. Получаем ACCESS_KEY
    В панели настройки ITSM перейдем в Консоль и выполним команду:
    ```bash
    return api.auth.getAccessKey('rasulovdd').setDeadlineDays(365).uuid
    ```
    где 'rasulovdd' - логин выбранного нами пользователя с ролью администратора. 
    Система сгенерирует и вернет нам ключ вида:
    accessKey=8a5d0671-ae00-4870-8751-269ed963932b
    добавляем его в .env файл 

## Пример полученного JSON

    {
    "10000000001": {
        "queue": "10000000001",
        "title": "Подольск-4",
        "pull_ext": "1210-1219",
        "status": "registered",
        "number_in_queue": [{
                "UUID": "objectBase$19881036",
                "title": "4952217551",
                "metaClass": "objectBase$Citynumber",
                "status": "registered"
            }, {
                "UUID": "objectBase$25331304",
                "title": "4950238779",
                "metaClass": "objectBase$Citynumber",
                "status": "closed"
            }, {
                "UUID": "objectBase$30578356",
                "title": "4950212360",
                "metaClass": "objectBase$Citynumber",
                "status": "closed"
            }, {
                "UUID": "objectBase$30578358",
                "title": "4950857554",
                "metaClass": "objectBase$Citynumber",
                "status": "closed"
            }
        ]
    }
    
registered - В эксплуатации
 
closed - Архивный

результат запроса запишется в файл text.txt

## Пример данных в файле .env
    
    ACCESS_KEY = "8a5d0671-ae00-4870-8751-269ed963932b"
    SERVER_ADDRESS = "https://test.itsm365.com/sd/"
    QUEUE_MIN = 10000000000
    QUEUE_MAX = 10000000100