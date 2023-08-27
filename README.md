# YaCut
Сервис коротких ссылок. 


## Возможности
- Автоматическая и ручная генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам
- web и api интерфейс

## Запуск проекта:
Установить зависимости:
```
pip install -r requirements.txt 
```

В корне проекта необходимо создать `.env` файл
```
FLASK_APP=yacut
FLASK_DEBUG=False
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<секретный ключ>
```

Выполнить миграции

```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```

Запустить проект
```
flask run
```

## API
- **POST** `/api/id/`

> Запрос:
>```json
>{
>  "url": "string",
>  "custom_id": "string"
>}
>```

> Ответ:
>```json
>{
>  "url": "string",
>  "short_link": "string"
>}
>```

- **GET** `/api/id/{short_id}/`


> Ответ:
>```json
>{
>  "url": "string",
>}
>```