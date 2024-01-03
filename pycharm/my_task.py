#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generate(n, t=[]):
    if n == 0:
        print(t)
        return
    generate(n - 1, t + [n])
    generate(n - 1, t)

if __name__ == '__main__':
    n = int(input("Введите значения n: "))
    generate(n)