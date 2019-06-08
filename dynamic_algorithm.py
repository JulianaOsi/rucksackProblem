import pandas as pd

def dynamic(weights, profits, capacity, size):

    table = []
    prev_max = 0
    for i in range(0, size):
        table.append([])
        for j in range(0, capacity):
            another_price = 0
            delta_weight = j + 1 - weights[i]  # оставшийся вес
            if i > 0:
                prev_max = table[i - 1][j]  # предыдущий максимум
                if delta_weight > 0:
                    another_price = table[i - 1][delta_weight - 1]  # стоимость оставшегося места
            if delta_weight < 0:
                table[i].append(prev_max)
            else:
                table[i].append(max(prev_max, profits[i] + another_price))
    return table

df = pd.read_csv('data15.csv', sep=',')
#print(df)
weights = df['weights']
profits = df['profits']
size = int(df['size'][:1])
capacity = int(df['capacity'][:1])
exp_result = int(df['exp_result'][:1])

#print(size)
#print(capacity)
#print(result)

knapsack = dynamic(weights, profits, capacity, size)
#print(knapsack)

result = knapsack[size - 1][capacity-1]
col = capacity-1
packed = []
sum = 0
for row in range(size-1, -1, -1):
    if row == 0 and knapsack[row][col] != 0:
        packed.insert(0, row)
    elif knapsack[row][col] != knapsack[row - 1][col]:
        packed.insert(0, row)
        col -= weights[row]
        sum += profits[row]
        if sum == result:
            break
print('exp_result: {1}\nresult: {0}'.format(exp_result, result))
print('packed item indexes: {0}'.format(packed))



