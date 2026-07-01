import requests
import json

print("Выберете тему:")
print("1.Лучшые статьи")
print("2.Программирование")
print("3.Электроника")
print("4.Diy проекты")
print("5.Компьютерное жедезо")
a = input("Введите число от 1 до 5: ")

respons = requests.get(f"http://127.0.0.1:8000/api/dashboard/widgets/run-line/{a}")
data = respons.json()

for i in range(1, 6):
    print(data[f"title{i}"])
    print(data[f"text{i}"])
    print(data[f"date{i}"])
    print("---")