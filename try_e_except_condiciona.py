# -*- coding: utf-8 -*-
"""Try e except condicional.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eBeiQRTPGPOC9KQTHt6LTKtxsd7Mivo2
"""

def converte_numero(valor):
  try:
    valor = int (valor)
    return valor
  except ValueError:
    try:
      valor = float (valor)
      return valor
    except ValueError:
      pass

while True:
  numero = converte_numero(input('Digite um número: '))

  if numero is None:
    print('Isso não é um número')
  else:
    print(numero * 2)