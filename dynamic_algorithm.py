import pandas as pd


def fill_knapsack(weights, values, size, capacity):  # Укладывает рюкзак с максимальной суммарной ценностью предметов
    knapsack = [[] for _ in range(0, size)]  # Создание строк таблицы весов укладок
    prev_max = 0  # Предыдущий максимум в текущем подрюкзаке
    for i in range(0, size):  # Пробег по строкам
        for j in range(0, capacity):  # Пробег по столбцам
            val_free_place = 0  # Стоимость оставшегося места в подрюкзаке
            delta_wts = j + 1 - weights[i]  # Оставшийся вес в подрюкзаке
            if i > 0:
                prev_max = knapsack[i - 1][j]
                if delta_wts > 0:  # Если в подрюкзаке осталось место
                    val_free_place = knapsack[i - 1][delta_wts - 1]
            if delta_wts < 0:  # Если текущий предмет весит больше подрюкзака
                knapsack[i].append(prev_max)  # Кладём предыдущий максимум
            else:
                knapsack[i].append(max(prev_max, values[i] + val_free_place))  # Берём предыдущий или текущий максимум с добавочной стоимостью
    return knapsack  # Возвращаем полученный рюкзак


df = pd.read_csv('data29.csv', sep=',')
weights = df['weights']  # Веса предметов
values = df['values']  # Ценности предметов
capacity = int(df['capacity'][0])  # Грузоподъемность рюкзака
expected_result = int(df['exp_result'][0])  # Ожидаемая суммарная максимальная ценность упакованного
size = int(df['size'][0])  # Количество всех предметов

knapsack = fill_knapsack(weights, values, size, capacity)

result = knapsack[-1][-1]  # Получаем максимальную ценность упакованного рюкзака
packed_indxs = []  # Индексы упакованных предметов
col = capacity - 1
for row in range(size - 1, -1, -1):  # Поиск помещенных в рюкзак предметов
    if row == 0 and knapsack[row][col] != 0:
        packed_indxs.append(row)  # Добавляем индекс, соответствующий стоимости добавленного в рюкзак предмета
    elif knapsack[row][col] != knapsack[row - 1][col]:
        packed_indxs.append(row)  # Добавляем индекс, соответствующий стоимости добавленного в рюкзак предмета
        col -= weights[row]  # Смещаемся на столбец с оставшимся весом
        if col < 0:
            break  # Выход из цикла, когда все помещенные в рюкзак предметы найдены

packed_vals = [values[i] for i in packed_indxs]  # Стоимости всех упакованных предметов
selected = [int(packed_indxs.count(i) == 1) for i in range(0, size)]   # 0-1 выборка
selection = df['selection'].tolist()
print(
    'Expected value: {0}\n'  # Вывод результатов
    'Result value: {1}\n'
    'Packed values: {2}\n'
    'Expected selection equals the result selection: {3}'
    .format(
    expected_result,
    result,
    packed_vals,
    selection == selected
))
