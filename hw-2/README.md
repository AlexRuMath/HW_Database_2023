# HW 2

## Настройка БД

Запустить контейнер с MongoDB и загрузить датасет
```
sh run.sh
```

Остановить MongoDB и подчистить контейнер
```
sh stop.sh
```

## Create
![Запрос на создание одной записи](/hw-2/screenshot/query_insert_one.png "Запрос на создание одной записи")

![Запрос на создание множества записей](/hw-2/screenshot/query_insert_many.png "Запрос на создание множества записей")

## Read
![](/hw-2/screenshot/query_get_all.png "Получение всех записей")

![](/hw-2/screenshot/query_get_have_word_DOWN.png "Получение всех записей, которые содержат в название слово DOWN")

## Update
![](/hw-2/screenshot/query_update_one.png "Обнволение записи")

## Delete
![](/hw-2/screenshot/query_delete_one.png "Удаление дубликатов записи")

## Indexes
![](/hw-2/screenshot/before_indexes.png "До индексации, значение executionStats.executionTimeMillis: 12")

![](/hw-2/screenshot/after_indexes.png)
![](/hw-2/screenshot/after_indexes_1.png "После индексации по полю author значение executionStats.executionTimeMillis: 7")