import random
import tkinter as tk

# создание окна
window = tk.Tk()
window.geometry('400x300')
window.title('Игра Камень-Ножницы-Бумага')

# определение глобальных переменных
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ''
COMP_CHOICE = ''


# определяем два метода для преобразования выбора пользователя в число и наоборот
def choice_to_number(chpice):
    rps = {'камень': 0, 'бумага': 1, 'ножницы': 2}
    return rps[chpice]


def number_to_choice(number):
    rps = {0: 'камень', 1: 'бумага', 2: 'ножницы'}
    return rps[number]


# функция для получения выбора компьютера
def random_comp_choice():
    return random.choice(['камень', 'бумага', 'ножницы'])


# основная логика
def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    if user == comp:
        print('Ничья')
    elif (user - comp) % 3 == 1:
        print('Вы выйграли!')
        USER_SCORE += 1
    else:
        print('Вы проиграли :(')
        COMP_SCORE += 1

    text_area = tk.Text(master=window, height=12, width=30, bg='#FFFF99')
    text_area.grid(column=0, row=4)

    answer = f'Ваш выбор: {USER_CHOICE}\nВыбор компа: {COMP_CHOICE}\nВы выйграли {USER_SCORE} раз\nКомп выйграл {COMP_SCORE} раз.'
    text_area.insert(tk.END, answer)


# создание кнопок для пользователя
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'камень'
    COMP_CHOICE = random_comp_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'бумага'
    COMP_CHOICE = random_comp_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'ножницы'
    COMP_CHOICE = random_comp_choice()
    result(USER_CHOICE, COMP_CHOICE)


button1 = tk.Button(text='Камень 🗿', bg='skyblue', command=rock)
button1.grid(column=0, row=1)

button2 = tk.Button(text='Бумага 📜', bg='pink', command=paper)
button2.grid(column=0, row=2)

button3 = tk.Button(text='Ножницы ✂', bg='lightgreen', command=scissor)
button3.grid(column=0, row=3)

window.mainloop()