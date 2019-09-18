# Проект для автоматизированного тестирования Сделки.Онлайн
------

## Используемый стек технологий
* [Selenium](http://www.seleniumhq.org/)
* [Python3](https://www.python.org)
* [PyTest](https://docs.pytest.org/en/latest/)
* [Allure](http://allure.qatools.ru/)

## Структура проекта
* `pages` - [page-объекты](https://kreisfahrer.gitbooks.io/selenium-webdriver/content/page_object_pattern_arhitektura_testovogo_proekta/ispolzovanie_patterna_page_object.html) для тестируемых страниц проекта
  * `locators` - солянка классов для страниц со специфическими локаторами и отдельный класс для общих локаторов
* `data_test` - CSV-таблицы с ID заполняемых полей и их значениями
* `conftest.py` - фикстуры запуска тестов
* `start_variables.json` - параметры для запуска тестов
* `test_*.py` - файлы со сценариями тестов

## Параметры запуска
Запуск проекта настраивается в файле `start_variables.json`. Список используемых параметров проекта:
* `enviroment` - адрес тестируемого стенда
* `login` - логин пользователя для входа
* `password` - пароль пользователя для входа
* `certificate` - название сертификата для входа
* `webdriver_path` - путь до chromedriver.exe на локальной машине
* `cryptoproextension_path` - путь до расширения от КриптоПро на локальной машине