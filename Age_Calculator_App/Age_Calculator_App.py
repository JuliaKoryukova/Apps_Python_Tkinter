import datetime
import tkinter as tk
from PIL import Image, ImageTk

# Создание окна для приложения
window = tk.Tk()
window.geometry('450x500')
window.title('Калькулятор возраста')

# Создание ярлыков с названиями, в сетке
name = tk.Label(text='Имя')
name.grid(column=0, row=1)
year = tk.Label(text='Год')
year.grid(column=0, row=2)
month = tk.Label(text='Месяц')
month.grid(column=0, row=3)
date = tk.Label(text='День')
date.grid(column=0, row=4)

# Создание соответствующих полей ввода
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)

# Определение класса Person
class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        year_age = today.year-self.birthdate.year
        month_age = today.month-self.birthdate.month
        day_age = today.day-self.birthdate.day
        if month_age < 0:
            year_age -= 1
            month_age +=12
        if day_age < 0:
            month_age -= 1
            day_age += (today.replace(year=today.year-1, month=self.birthdate.month).day - self.birthdate.day)

        return year_age, month_age, day_age

# Создание функции для получения данных пользователя
def getInput():
    name = nameEntry.get()
    birthdate = datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get()))
    monkey = Person(name, birthdate)
    year_age, month_age, day_age = monkey.age()
    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = f'Приветик, {name}!!!\nТебе {year_age} лет, {month_age} месяцев и {day_age} дней!!!'
    textArea.insert(tk.END, answer)

# Создание кнопки для входных значений
button = tk.Button(window, text='Посчитать возраст', command=getInput, bg='pink')
button.grid(column=1, row=5)

# Добавление изображения для красивого приложения
image = Image.open('1.jpg')
image.thumbnail((300, 300))
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.image = photo
label_image.grid(column=1, row=0)

window.mainloop()


