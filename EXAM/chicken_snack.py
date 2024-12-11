from collections import deque

money_in_pocket = [int(el) for el in input().split()]
prices = deque([int(el) for el in input().split()])
eaten_food = 0

while money_in_pocket and prices:
    current_money = money_in_pocket[-1]
    current_price = prices[0]

    if current_money == current_price:
        money_in_pocket.pop()
        prices.popleft()
        eaten_food += 1
    elif current_money > current_price:
        money_in_pocket.pop()
        difference = current_money - current_price
        money_in_pocket[-1] += difference
        eaten_food += 1
        prices.popleft()
    else:
        money_in_pocket.pop()
        prices.popleft()

if eaten_food == 1:
    print(f"Henry ate: {eaten_food} food.")
elif eaten_food > 1 and eaten_food < 4:
    print(f"Henry ate: {eaten_food} foods.")
elif eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")



