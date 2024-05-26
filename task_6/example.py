from algorithms import greedy_algorithm, dynamic_programming


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    chosen_items, total_calories = greedy_algorithm(items, 80)
    print(f"Обрані продукти: {chosen_items}, Загальна кількість калорій: {total_calories}")

    chosen_items, total_calories = dynamic_programming(items, 80)
    print(f"Обрані продукти: {chosen_items}, Загальна кількість калорій: {total_calories}")


if __name__ == '__main__':
    main()
