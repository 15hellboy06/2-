money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_capital = money_capital + salary
current_spend = spend

while current_capital >= current_spend:
    current_capital -= current_spend
    months += 1
    if months > 1:
        current_spend *= (1 + increase)
        current_capital += salary
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
