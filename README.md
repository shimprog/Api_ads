Метод получения списка объявлений:
http://127.0.0.1:8000/api/

Метод получения конкретного объявления:
  обязательные поля в ответе: название объявления, цена, ссылка на главное фото
  http://127.0.0.1:8000/api/1/
  
  опциональные поля (можно запросить, передав параметр fields): описание, ссылки на все фото
  http://127.0.0.1:8000/api/1/fields/
  
 Метод создания объявления:
  http://127.0.0.1:8000/api/create/
