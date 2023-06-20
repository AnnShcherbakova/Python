#Игра викторина: 5 лекция
print('Привет!')
answer = input("Готов к игре!(yes/no): ")
score = 0
total_questions = 7
if answer.lower() == 'yes':
    answer = input("Вопрос 1: Какой национальный цветок Японии? ")
    if answer.lower() == ('сакура'):
        score += 1
        print('Отличный выбор!')
    else:
        print(' К сожалению это неправильный ответ!')
    answer = input("Вопрос 2: Как называется столица американского штата Калифорния? ")
    if answer.lower() == ('сакраменто'):
        score += 1
        print('Молодец!')
    else:
        print('Ответ неправильный(')
    answer = input("Вопрос 3: Какая валюта Дании? ")
    if answer.lower() == ('крона'):
        score += 1
        print('Отлично!')
    else:
        print('Попробуй ещё раз!')

    answer = input("Вопрос 4: Сколько элементов в периодической таблице? ")
    if answer.lower() == ('118'):
        score += 1
        print('Умница!')
    else:
        print('К сожалению нет!')

    answer = input("Вопрос 5: В какой части вашего тела вы найдёте крестообразную связку? ")
    if answer.lower() == ('колено'):
        score += 1
        print('Умница!')
    else:
        print('К сожалению нет!')

    answer = input("Вопрос 6: Какая планета ближе всех расположена к Солнцу? ")
    if answer.lower() == ('меркурий'):
        score += 1
        print('Здорово!')
    else:
        print('Ты ответил неправильно!')

    answer = input("Вопрос 7: В какой стране больше всего островов в мире? ")
    if answer.lower() == ('швеция'):
        score += 1
        print('У тебя отлично получается!')
    else:
        print('Как жаль!')

print('Спасибо, что поиграли со мной. Вы ответили на:', score, 'вопросов правильно!')
mark = (score/total_questions)*10
print('Заработано; ', int(mark))
print('До следующей встречи!')






