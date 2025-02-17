from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles = deque([int(bottle) for bottle in input().split()])

wasted_litres = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_litres += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print("Cups:", *cups)
else:
    print("Bottles:", *bottles)

print(f"Wasted litters of water: {wasted_litres}")

