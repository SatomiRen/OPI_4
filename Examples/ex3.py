#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import sys
from datetime import date


def get_driver():
    """
    Запросить данные о водителе.
    """
    name = input("Фамилия и имя? ")
    team = input("Команда? ")
    year = int(input("Год вступления? "))
    # Создать словарь.
    return {
        'name': name,
        'team': team,
        'year': year,
    }


def display_drivers(staff):
    """
    Отобразить список водителей.
    """
    # Проверить, что список не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Ф.И.О.",
                "Команда",
                "Год"
            )
        )
        print(line)
        # Вывести данные о всех сотрудниках.
        for idx, driver in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    driver.get('name', ''),
                    driver.get('team', ''),
                    driver.get('year', 0)
                )
            )
            print(line)
    else:
        print("Список водителей пуст.")


def select_drivers(staff, period):
    """
    Выбрать водителей с заданным стажем.
    """
    # Получить текущую дату.
    today = date.today()
    # Сформировать список работников.
    result = []
    for employee in staff:
        if today.year - employee.get('year', today.year) >= period:
            result.append(employee)
    # Возвратить список выбранных водителей.
    return result


def save_drivers(file_name, staff):
    """
    Сохранить всех водителей в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=True, indent=4)


def load_drivers(file_name):
    """
    Загрузить всех водителей из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    """
    Главная функция программы.
    """
    # Список водителей.
    drivers = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == "exit":
            break
        elif command == "add":
            # Запросить данные о работнике.
            driver = get_driver()
            # Добавить словарь в список.
            drivers.append(driver)
            # Отсортировать список в случае необходимости.
            if len(drivers) > 1:
                drivers.sort(key=lambda item: item.get('name', ''))
        elif command == "list":
            # Отобразить всех водителей.
            display_drivers(drivers)
        elif command.startswith("select"):
            # Разбить команду на части для выделения стажа.
            parts = command.split(maxsplit=1)
            # Получить требуемый стаж.
            period = int(parts[1])
            # Выбрать водителей с заданным стажем.
            selected = select_drivers(drivers, period)
            # Отобразить выбранных водителей.
            display_drivers(selected)
        elif command.startswith("save"):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            save_drivers(file_name, drivers)
        elif command.startswith("load"):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            drivers = load_drivers(file_name)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить водителя;")
            print("list - вывести список водителей;")
            print("select <стаж> - запросить водителей со стажем;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
