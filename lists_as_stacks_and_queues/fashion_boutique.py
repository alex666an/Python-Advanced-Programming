clothes = [int(x) for x in input().split()]
rack_space = int(input())

racks_count = 1
current_rack_space = rack_space

while clothes:
    clothing = clothes.pop()

    if current_rack_space >= clothing:
        current_rack_space -= clothing

    else:
        racks_count += 1
        current_rack_space = rack_space - clothing

print(racks_count)
