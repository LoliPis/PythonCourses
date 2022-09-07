HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today = []
tomorrow = []
other = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print('Сегодня: ', today, '\n', 'Завтра: ', tomorrow, '\n', 'Другие дни: ', other)
  elif command == "add":
    date = input('Введите дату: ')
    task = input("Введите название задачи: ")
    if date == 'Сегодня':
        today.append(task)
        print("Задача добавлена")
    elif date == 'Завтра':
        tomorrow.append(task)
        print("Задача добавлена")
    else:
        other.append(task)
        print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else:
    print("Неизвестная команда")
    break
