#!/usr/bin/env bash

DATA_BASE_FILE=./db.sqlite3
LISTEN_IP=127.0.0.1
LISTEN_PORT=8000

if [ ! ${VIRTUAL_ENV} ]
    then
        echo "Внимание! Не запущено виртуальное окружение! Если вы продолжите, потребуются права администратора и необходимые для работы зависимости будут установлены в корень системы. Хотите продолжить (Y/N y/n 1/0) ?"
        read start_pip
    else
        start_pip=1
fi

if [ $start_pip ] && ( [ $start_pip == Y ] || [ $start_pip == y ] || [ $start_pip == 1 ] )
    then
        echo
    else
        echo "Запуск сервера отменён по решению пользователя."
        exit 0
fi

if ! [ -f $DATA_BASE_FILE ]
    then
        echo "Нет файла БД. Начинается процедура первого запуска и создания первого пользователя в системе:"
        echo "    Шаг 1. Идет установка необходимых зависимостей."
        pip install -r requirements.txt
        echo "    Шаг 2. Создается начальная база данных."
        ./manage.py migrate
        echo "    Шаг 3.1. Введите E-mail адрес первого пользователя:"
        read first_email
        echo "    Шаг 3.2. Введите логин первого пользователя:"
        read first_username
        echo "    Шаг 3.3. 2 раза введите пароль первого пользователя:"
        ./manage.py createsuperuser --email $first_email --username $first_username
fi

echo "    Всё готово. Для управления пользователями используйте одну из этих ссылок:"
echo "        http://$LISTEN_IP:$LISTEN_PORT/admin/"
echo "        https://$LISTEN_IP:$LISTEN_PORT/admin/"
./manage.py runserver $LISTEN_IP:$LISTEN_PORT
