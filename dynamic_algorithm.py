import pandas as pd

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


df = pd.read_csv('data20.csv', header=0, sep=';')
print(df)
prices = df['price']
weights = df['weight']
print(prices, weights)
rucksack_weight = 1278

print(dynamic(weights, prices, rucksack_weight))