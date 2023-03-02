import random

print("Игра 'Камень, ножницы, бумага'")
options = ['Камень', 'Ножницы', 'Бумага']

while True:
    # Запрос хода пользователя
    user_choice = input("Выберите свой ход (Камень, Ножницы, Бумага): ")

    # Проверка на корректность хода пользователя
    if user_choice not in options:
        print("Ошибка! Некорректный ход.")
        continue

    # Выбор случайного хода компьютера
    computer_choice = random.choice(options)

    # Проверка на ничью
    if user_choice == computer_choice:
        print("Ничья! Оба выбрали", user_choice)
        continue

    # Проверка на выигрыш пользователя
    if (user_choice == "Камень" and computer_choice == "Ножницы") or \
       (user_choice == "Ножницы" and computer_choice == "Бумага") or \
       (user_choice == "Бумага" and computer_choice == "Камень"):
        print("Вы выиграли! Выбор компьютера:", computer_choice)
    # Иначе - выигрыш компьютера
    else:
        print("Вы проиграли! Выбор компьютера:", computer_choice)
