def greedy_algorithm(items, budget):
    # Сортування елементів за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    chosen_items = []
    for item in sorted_items:
        if budget >= item[1]["cost"]:
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]
            chosen_items.append(item[0])
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Перетворення словника у список для легшого доступу
    items_list = list(items.items())
    n = len(items_list)
    dp = [[0 for x in range(budget + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items_list[i-1][1]["cost"] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items_list[i-1][1]["cost"]] + items_list[i-1][1]["calories"])
            else:
                dp[i][w] = dp[i-1][w]
    # Відновлення набору страв
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(items_list[i-1][0])
            w -= items_list[i-1][1]["cost"]
    chosen_items.reverse()
    return chosen_items, dp[n][budget]
