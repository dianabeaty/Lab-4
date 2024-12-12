from itertools import combinations


items = {
    'r': (3, 25),  # Винтовка
    'p': (2, 15),  # Пистолет
    'a': (2, 15),  # Боекомплект
    'm': (2, 20),  # Аптечка
    'i': (1, 5),   # Ингалятор
    'k': (1, 15),  # Нож
    'x': (3, 20),  # Топор
    't': (1, 25),  # Оберег
    'f': (1, 15),  # Фляжка
    'd': (1, 10),  # Антидот
    's': (2, 20),  # Еда
    'c': (2, 20)   # Арбалет
}

max_size = 9
initial_survival_points = 15
must_have_item = ['i']

best_combination = None
best_survival_points = float('-inf')

for size in range(1, len(items) + 1):
    for combination in combinations(items.keys(), size):
        total_size = sum(items[item][0] for item in combination)
        total_points = sum(items[item][1] for item in combination)

        if total_size <= max_size and all(item in combination for item in must_have_item):
            final_points = initial_survival_points + total_points

            if final_points > best_survival_points:
                best_survival_points = final_points
                best_combination = combination

if best_combination:
    inventory = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i * 3 + j < len(best_combination):
                inventory[i][j] = best_combination[i * 3 + j]

    for row in inventory:
        print(['[{}]'.format(item) for item in row])

    print(f"Итоговые очки выживания: {best_survival_points}")