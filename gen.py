#!/usr/bin/env python3
# coding=utf-8

'''
CPF Generator

Author: FelipeCRamos
'''
import random

cpf = random.randint(10**8, 999999999)  # random cpf
v1, v2 = 0, 0                           # verification digits

s_format = False

# creation of reversed CPF
reversed_cpf = list(str(cpf))
reversed_cpf.reverse()

# verification digit 1
for i in list(range(0,9)):
    v1 += int(reversed_cpf[i]) * (9 - (i % 10))
    v2 += int(reversed_cpf[i]) * (9 -((i + 1) % 10))

v1 = (v1 % 11) % 10
v2 += (v1 * 9)
v2 = (v2 % 11) % 10

cpf = str(cpf)

# print of generated CPF
if s_format:
    print("{}.{}.{}-{}{}".format(cpf[0:3], cpf[3:6], cpf[6:9], v1, v2))
else:
    print("{}{}{}".format(cpf, v1, v2))
