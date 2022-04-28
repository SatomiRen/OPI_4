#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


if __name__ == '__main__':
    with open("foo1.txt", "r") as f:
        contents = f.read()
    my_list = json.loads(contents)
    print(my_list)
    # вариант 2
    with open("foo2.txt", "r") as f:
        my_list = json.load(f)
    print(my_list)

    