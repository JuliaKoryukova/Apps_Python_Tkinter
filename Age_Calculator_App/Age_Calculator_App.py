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
        now = datetime.datetime.now()
        years = int(now.year) - int(str(self.birthdate.year))
        months = int(now.month) - int(str(self.birthdate.month))
        days = int(now.day) - int(str(self.birthdate.day))

        if months == 12:
            years += 1
            months -= 12
        if months <= 0:
            years -= 1
            months += 12
        if days <= 0:
            months -= 1
            days += 31
        return years, months, days

# Создание функции для получения данных пользователя
def getInput():
    name = nameEntry.get()
    birthdate = datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get()))
    monkey = Person(name, birthdate)
    years, months, days = monkey.age()
    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = f'Приветик, {name}!!!\nТебе {years} лет, {months} месяцев и {days} дней!!!'
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


