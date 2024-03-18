items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    items_sorted = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    for item, details in items_sorted:
        if details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]

    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    item_names = list(items.keys())

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']
        item_calories = items[item_name]['calories']

        for w in range(1, budget + 1):
            if item_cost <= w:
                dp_table[i][w] = max(
                    item_calories + dp_table[i - 1][w - item_cost], dp_table[i - 1][w])
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    chosen_items = []
    temp_budget = budget

    for i in range(len(items), 0, -1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']

        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            chosen_items.append(item_name)
            temp_budget -= item_cost

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print(greedy_result, dp_result)
