shop = {
    "торт": [
        ["мука", "яйцо", "сахар", "сметана", "клубника"], 25, 500
    ],
    "пироженое": [
        ["сахар-песок", "белок яичный", "масло сливочное", "шоколад"], 15, 300
    ],
    "маффин": [
        ["мука", "яйцо", "сахар", "шоколад", "изюм"], 15, 200
    ],
}
print(('Здравствуйте. Что подсказать? Для выбора введите: "состав", "цена", "количество", '
       '"вся информация", "приступить к покупке"'))
while True:

    a = input('Введите что вам подсказать: ')
    if a == "состав":
        for key, value in shop.items():
            print(key, '-', ','.join(value[0]))
    if a == "цена":
        for key, value in shop.items():
            print(key, f' - {value[1]}р. за 100гр.')
    if a == "количество":
        for key, value in shop.items():
            print(key, f' - {value[2]} гр')
    if a == "вся информация":
        for key, value in shop.items():
            print(f'{key}', '\nсостав:',','.join(value[0]), f'\nцена: {value[1]}р. за 100гр.',
                  f'\nколичество: {value[2]} гр')
    else:
        total = 0
        while True:
            product_name = input('Что вы хотите купить? "торт", "маффин", "пироженое" или '
                                 'введите n для завершения покупок')

            if product_name == 'n':
                break

            selected_product = shop[product_name]

            grams_to_buy = int(input('Введите количество граммов для покупки'))

            product_cost = selected_product[1] / 100 * grams_to_buy

            total += product_cost

            selected_product[2] -= grams_to_buy

        print('Цена купленных товаров', total)

        print('\nОстатки товаров\n')

        for key, value in shop.items():
            print(f'{key}', '\nсостав:',','.join(value[0]), f'\nцена: {value[1]}р. за 100гр.',
                  f'\nколичество: {value[2]} гр')


