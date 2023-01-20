# Автоматизация тестирования API для сервиса [SurveysAPI](https://surveys-biof.onrender.com)

## Содержание

+ [Технологии и инструменты](#Технологии)
+ [Тест-кейсы](#Тесты)
+ [Запуск автотестов из Jenkins](#Jenkins)
+ [Оповещение о результатах через Telegram-бот](#Telegram)
+ [Отчеты о прохождении тестов Allure report](#Allure)

<a name="Технологии"></a>

## Технологии и инструменты

<p align="center">
<img width="6%" title="PyCharm" style="margin: 0 1%;" src="docs/assets/images/pycharm.png">
<img width="6%" title="Python" style="margin: 0 1%;" src="docs/assets/images/python.png">
<img width="6%" title="Pytest" style="margin: 0 1%;" src="docs/assets/images/pytest.png">
<img width="6%" title="Requests" style="margin: 0 1%;" src="docs/assets/images/requests.png">
<img width="6%" title="Jenkins" style="margin: 0 1%;" src="docs/assets/images/jenkins.png">
<img width="6%" title="Allure" style="margin: 0 1%;" src="docs/assets/images/allure_report.png">
<img width="6%" title="Telegram" style="margin: 0 1%;" src="docs/assets/images/telegram.png">
</p>

<a name="Тесты"></a>

## Тест-кейсы

###### Авторизация:

- Успешная авторизация
- Неуспешная авторизация. Не указан пароль

###### Действия с пользователем:

- Добавление пользователя
- Изменение данных пользователя
- Удаление пользователя

<a name="Jenkins"></a>

## Запуск автотестов из Jenkins

Для удаленного запуска автотестов в <a href="http://45.80.71.190:8080/" target="_blank">Jenkins</a> создана задача (job), настроена и связана с репозиторием в GitHub.

<img title="Jenkins job" src="docs/assets/images/jenkins_job.png">

<a name="Telegram"></a>

## Уведомление о результатах тестирования через Telegram-бот

После завершения тестов происходит отправка сообщения в Telegram с помощью заранее созданного Telegram-бота, подключенного в
задаче Jenkins.

<img width="360" alt="Telegram report" src="docs/assets/images/telegram_report.png">

<a name="Allure"></a>

## Отчеты тестов Allure report

После выполнения тестов формируются отчеты Allure, которые можно посмотреть со страницы задачи в Jenkins.

<img width="1384" alt="image" src="docs/assets/images/jenkins_allure_report.png">

<img width="1384" alt="image" src="docs/assets/images/allure_test_report.png">
