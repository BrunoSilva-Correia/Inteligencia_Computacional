#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Para que o código funcione, é necessário
# instalar a biblioteca skfuzzy.

import numpy as np
import skfuzzy as fuzz

print('Qual o Valor da Conta?')
conta = input()

print('\nQual a Nota para o Serviço:')
servico = input()

print('\nQual a Nota para a Comida:')
comida = input()

# range definda para as notas e também para que a gorjeta seja de no max 25%
x_qual = np.arange(0, 10.1, 0.1)
x_serv = np.arange(0, 10.1, 0.1)
x_tip = np.arange(0, 25.1, 0.1)

# criando as funçoes de pertinecia
qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_qual, [5, 10, 10])
serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
serv_md = fuzz.trimf(x_serv, [0, 5, 10])
serv_hi = fuzz.trimf(x_serv, [5, 10, 10])
tip_lo = fuzz.trimf(x_tip, [0, 0, 13])
tip_md = fuzz.trimf(x_tip, [0, 13, 25])
tip_hi = fuzz.trimf(x_tip, [13, 25, 25])

# retornado o grau de pertinencia de acordo com a nota obtida nos input's
qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, comida)
qual_level_md = fuzz.interp_membership(x_qual, qual_md, comida)
qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, comida)
serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, servico)
serv_level_md = fuzz.interp_membership(x_serv, serv_md, servico)
serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, servico)

# regras relacionando diretamente qualidade do serviço/comida com a % da gorjeta
active_rule1 = np.fmax(qual_level_lo, serv_level_lo)
tip_activation_lo = np.fmin(active_rule1, tip_lo)
tip_activation_md = np.fmin(serv_level_md, tip_md)
active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)

# agregando as 3 funçoes acima
aggregated = np.fmax(tip_activation_lo, np.fmax(tip_activation_md, tip_activation_hi))

# calculo do resultado da gorjeta
tip = fuzz.defuzz(x_tip, aggregated, "centroid")
tip_activation = fuzz.interp_membership(x_tip, aggregated, tip)

# transformando ambos os valores para inteiro, para facilitar as operaçoes basicas de aritmetica
tip = int(tip)
conta = int(conta)

# calculo da gorjeta baseado na porcentagem(tip/100)
valorGorjeta = conta * (tip/100)
print('\n\n')
print('percentual da gorjeta', tip,'%')
print('\nValor da Gorjeta',valorGorjeta)

# print(type(conta))
# print(type(tip))


# In[ ]:




