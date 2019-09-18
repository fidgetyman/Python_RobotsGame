import math
from abc import *
'''Сумма чисел ФИббоначчи, кратных двум ( до 4-х миллионов)'''
# a = [0, 1]
# i = 1
# summary = 0
#
# while a[i] < 4000000:
#     a.append(a[i] + a[i-1])
#     summary = summary + a[i]
#     i = i + 1
#     if a[i] % 2 == 0:
#         summary = summary + a[i]
#         print(a[i])
# print('summa:', summary)
'''Подсчет количества рукопожвтий'''
# def handShakes(a):
#     r = a  *(a - 1)/2
#     print(r)
# handShakes(2)
'''Разложение на простые множители'''
# global mass
# mass = []
# def prostMnozh(a):
#     k = 2
#     while a not in range(1, 9):
#         while k * k <= a:
#             while a % k == 0:
#                 a = a / k
#                 mass.append(k)
#             k = k + 1
#     if a > 1: mass.append(a)
#     print(mass)
# prostMnozh(28)
'''10001-e простое число'''
# from math import *
# from itertools import *
# def issimple(n):
#     r = math.ceil(math.sqrt(n))
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = 5
# s = [2, 3]
# while True:
#     if issimple(n) is True:
#         s.append(n)
#     if len(s) == 10001:
#         break
#     n += 2
#
# print(s[-1])
'''Разность квадрата суммы и суммы квадратов первых 100 натуральных чисел'''
# mass = []
# mass2 = []
# def sqSum(n):
#     j = 1
#     while j <= n:
#         mass.append(j)
#         j += 1
#     mass2 = mass
#     i = 0
#     while i < n:
#         mass[i] **= 2
#         i += 1
#     summary = sum(mass2) ** 2
#     rez = summary - sum(mass)
#     return print(rez)
# sqSum(100)

'''Особая тройка Пифагора (равная 1000)'''
# a = b = c = 0
# def Pifagor(n):
#     a = (2 * n + 1)**2
#     b = (2 * n * (n + 1))**2
#     c = (2 * n * (n + 1) + 1)**2
#     print(a, b, c)
# Pifagor()

class RobotsGame:
    def __init__(self, name, hp, ad):
        self.name = name
        print('Created new WarRobot {0}'.format(self.name))
        print()

    def stats(self):
        print('Name: {0}\nHP: {1}\nAttack: {2}'.format(self.name, self.hp, self.ad))
        print()

class RobotLaser(RobotsGame):
    def __init__(self, name, hp, ad):
        RobotsGame.__init__(self, name, hp, ad)
        self.hp = hp
        self.ad = ad
        print("New robot's {0} stats:\nName: {1}\nHP: {2}\nAttack: {3}".format(self.name, self.name, self.hp, self.ad))
        print()
class RobotWeapon:
    def __init__(self, name, weapon):
        self.weapon = weapon
    def getWeapon(self, weaponName):


class RobotsFight:
    def startFight(self, robot1, robot2):
        print("Initialised fight between {0} and {1}".format(robot1.name, robot2.name))
        print("---------------------- FIGHT! --------------------------")

        i = 1
        count = 1
        while robot1.hp > 0 and robot2.hp > 0:
            if count == 1:
                print('Step {0} : {1} attacks {2}'.format(i, robot1.name, robot2.name))
                robot2.hp = robot2.hp - robot1.ad
                print("{0} sliced {1} for {2} HP".format(robot1.name, robot2.name, robot1.ad))
                print("{0}'s HP is {1} now".format(robot2.name, robot2.hp))
                print()
                count = 2
            elif count == 2:
                print('Step {0} : {1} attacks {2}'.format(i, robot2.name, robot1.name))
                robot1.hp = robot1.hp - robot2.ad
                print("{0} sliced {1} for {2} HP".format(robot2.name, robot1.name, robot2.ad))
                print("{0}'s HP is {1} now".format(robot1.name, robot1.hp))
                print()
                count = 1
            i += 1

robot1 = RobotLaser("Borya-2000", 10, 5)
robot2 = RobotLaser("Mark-II", 11, 5)

RobotsFight.startFight(robot1, robot2)

