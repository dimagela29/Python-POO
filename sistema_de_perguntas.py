# -*- coding: utf-8 -*-
"""Sistema de perguntas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MCoozUOOQCE4LmCy8GAhds8Y-dPwaZk3
"""

pergunta = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2 ? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta certa': 'b',
    },

        'Pergunta 2': {
            'pergunta': 'Quanto é 3 * 2 ? ',
            'respostas': {'a': '4', 'b':'10', 'c':'6',},
            'resposta certa': 'c',
        },
}

resposta_certa = 0
for pk, pv in pergunta.items():
  print(f"{pk}: {pv['pergunta']}")


  print('Respostas')
  for rk, rv in pv['respostas'].items():
    print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    
    if resposta_usuario == pv['resposta certa']:
      print('Voce Acertou')
      resposta_certa += 1
    else:
      print('Voce errou')

    print()