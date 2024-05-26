import random
import matplotlib.pyplot as plt


def main():

    real_probabilities = [1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36, 5 / 36, 4 / 36, 3 / 36, 2 / 36, 1 / 36]
    num_rolls_list = [100, 1000, 10000, 100000, 1000000]

    fig, axs = plt.subplots(len(num_rolls_list), figsize=(10, 18))
    for i, num_rolls in enumerate(num_rolls_list):
        results = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls)]
        sum_counts = {sum_value: results.count(sum_value) for sum_value in range(2, 13)}
        simulated_probabilities = [count / num_rolls for count in sum_counts.values()]
        axs[i].bar(range(2, 13), simulated_probabilities, color='b', label='Симульовані імовірності')
        axs[i].plot(range(2, 13), real_probabilities, 'r-', linewidth=2, label='Реальні імовірності')
        axs[i].set_title(f'Кількість кидків: {num_rolls}')
        axs[i].set_xticks(range(2, 13))
        axs[i].set_xlabel('Сума')
        axs[i].set_ylabel('Імовірність')
        axs[i].legend()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
