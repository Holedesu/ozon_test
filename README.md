## Описание логики
Функция делает запрос к API и:

- проверяет входные аргументы (`gender` — строка, `is_working` — булев тип)
- фильтрует всех супергероев по полу и занятости
- из подходящих возвращает самого высокого
- если ни один герой не подошёл — возвращает `None`

Тесты написаны с использованием pytest и проверяют следующее:
- test_filter_heroes_gender	Проверка, что фильтрация не зависит от регистра по полу
- test_filter_heroes_work Проверка корректной работы фильтрации по занятости
- test_filter_heroes_returns_tallest_* Проверка, что функция возвращает самого высокого героя среди подходящих
- test_filter_heroes_incorrect_* Проверка обработки исключений при некорректных аргументах функции

## Установка и запуск

### 1. Клонировать репозиторий (если ещё не сделал)
git clone git@github.com:Holedesu/ozon_test.git
cd ozon_test

### 2. Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate *(macOS/Linux)* <br>
venv\Scripts\activate *(Windows)*

### 3. Установить зависимости
pip install -r requirements.txt

### 4. Запустить тесты
pytest -v

## Обьяснение логики функции

1. Проверка входящих данных
   1.  Функция проверяет, что `gender` — это строка, а `is_working` — булево значение
```python
if not isinstance(gender, str):
    raise TypeError("gender должен быть строкой")

if not isinstance(is_working, bool):
    raise TypeError("is_working должен быть логическим значением")
```
2. Получение всех супергероев
   1. Делаю HTTP-запрос к API для получения списка всех героев
```python
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
data = response.json()
```
3. Фильтрация по полу и занятости
   1. Сначала проверяю пол, затем проверяю, работает ли герой
   2. Если герой соответствует обоим условиям, то его добавляю в `correct_heroes`
```python
correct_heroes = []
for hero in data:
    if hero["appearance"]["gender"] == gender.capitalize():
        if hero["work"]["occupation"] == "-" and is_working == False:
            correct_heroes.append(hero)
        elif hero["work"]["occupation"] != "-" and is_working == True:
            correct_heroes.append(hero)
```
4. Поиск самого высокого из отфильтрованных
   1. Для каждого подходящего героя беру рост в метрической системе
   2. Проверяю тип измерения, если он в метрах, то умножаю на 100
   3. Затем сравниваю с текущим максимумом и если рост выше, добавляю героя в `result`
```python
result = None
max_height = 0
for hero in correct_heroes:
    height, measurement_type = hero["appearance"]["height"][1].split(" ")
    height = int(float(height) * 100) if measurement_type == "meters" else int(height)

    if height > max_height:
        max_height = height
        result = hero
```
5. В конце возвращаю героя удовлетворяющего условия, если никто не найдем, возвращаю `None`
```python
return result
```