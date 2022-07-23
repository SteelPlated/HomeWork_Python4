'''4. Задана натуральная степень k. Сформировать
случайным образом список коэффициентов (значения от
0 до 100) многочлена и вывести на экран.
Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0
или 10*x² = 0'''

import random


k = int(input("Введите число: "))
mnogochlen=""

while k>=0:
    a=random.randint(0,100)
    if a!=0 and k!=0:
        if k==1:
            mnogochlen= mnogochlen+str(a)+'*x'+'+'
        else:
            mnogochlen= mnogochlen+str(a)+'*x^'+str(k)+'+'
    if k==0 and a!=0:
        mnogochlen= mnogochlen+str(a)
    k-=1
if mnogochlen!="":
    mnogochlen=mnogochlen+'=0'
print(mnogochlen)