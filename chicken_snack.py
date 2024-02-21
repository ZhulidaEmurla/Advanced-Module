money_sequence = list(map(int, input().split()))
prices_sequence = list(map(int, input().split()))

foods_eaten = 0

while money_sequence and prices_sequence:
    money = money_sequence.pop()
    price = prices_sequence.pop(0)

    if money == price:
        foods_eaten += 1
    elif money > price:
        foods_eaten += 1
        change = money - price
        if money_sequence:
            money_sequence[-1] += change

if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")
elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")
elif foods_eaten > 1:
    print(f"Henry ate: {foods_eaten} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")
