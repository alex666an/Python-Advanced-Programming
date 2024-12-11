def even_odd_filter(**numbers_sets):
    if 'odd' in numbers_sets:
        numbers_sets['odd'] = [n for n in numbers_sets['odd'] if n % 2 != 0]
    if 'even' in numbers_sets:
        numbers_sets['even'] = [n for n in numbers_sets['even'] if n % 2 == 0]

    return dict(sorted(numbers_sets.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))


