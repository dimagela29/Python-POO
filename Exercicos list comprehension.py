# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qy4Cv12NXglLRPzYHWNmPoIRJ8MorDGU
"""

string  = '012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)