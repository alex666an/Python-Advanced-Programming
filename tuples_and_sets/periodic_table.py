row_count = int(input())
table = set()

for _ in range(row_count):
    for element in input().split():
        table.add(element)

print(*table, sep='\n')

