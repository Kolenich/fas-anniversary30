# Шаблон сайта 30-летия ФАС

## Запуск проекта
Для начала необходимо создать виртуальную среду
```bash
virtualenv venv
```
Теперь активировать её
```bash
source venv/bin/activate
```
Затем установить зависимости
```bash
pip install requirements.txt
```
Далее выполнит миграции в БД
```bash
python manage.py migrate
```
И наконец запустить сервер
```bash
python manage.py runserver
```
[Шаблон верстки](https://www.figma.com/file/TjVhWvEimgDXxV2Qwf91Am/30%D0%9B%D0%95%D0%A2?node-id=18%3A3)
