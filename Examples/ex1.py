#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


if __name__ == '__main__':
    my_list = ['foo', 'bar']
    # Вариант 1
    contents = json.dumps(my_list)
    with open("foo1.txt", "w", encoding="utf-8") as f:
        f.write(contents)
    # Вариант 2
    with open("foo2.txt", "w", encoding="utf-8") as f:
        json.dump(my_list, f)
