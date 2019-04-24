def dynamic(weights, prices, rucksack_weight):
    table = []
    prev_max = 0
    for i in range(0, len(prices)):
        table.append([])
        for j in range(0, rucksack_weight):
            another_price = 0
            delta_weight = j + 1 - weights[i]  # оставшийся вес

            if i > 0:
                prev_max = table[i - 1][j]  # предыдущий максимум
                if delta_weight > 0:
                    another_price = table[i - 1][delta_weight - 1]  # стоимость оставшегося места

            if delta_weight < 0:
                table[i].append(prev_max)
            else:
                table[i].append(max(prev_max, prices[i] + another_price))
    return table


prices = [1500, 3000, 2000]
weights = [1, 4, 3]

rucksack_weight = 4

print(dynamic(weights, prices, rucksack_weight))