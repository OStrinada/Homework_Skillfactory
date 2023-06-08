overall_cost = 0
while True:
    try:
        tickets = int(input('Сколько билетов хотите приобрести?'))
        if type(tickets) == int:
            break
    except ValueError:
        print('Введите целое число...')
for i in range(tickets):
    i += 1
    while True:
        try:
            age_visitor = input(f'Укажите возраст обладателя билета №{i}? ')
            age_visitor = int(age_visitor)
            if age_visitor < 18:
                print('Билет бесплатный.')
            elif 25 > age_visitor >= 18:
                overall_cost += 990
                print('Стоимость билета: 990 руб.')
            else:
                overall_cost += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_visitor) == int:
                break
        except ValueError:
            print('Введите целое число...')
if tickets > 3:
    overall_cost = overall_cost - ((overall_cost / 100) * 10)
    print(f'Сумма к оплате {overall_cost} руб. с учетом 10%-ой скидки за регистрацию более 3-х человек.')
else:
    print(f'Сумма к оплате {overall_cost} руб.')
print('Не забудьте документы, подтверждающие возраст участника!')
