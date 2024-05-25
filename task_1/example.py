from linked_list import LinkedList


def main():
    # Створення списків
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    # Додавання елементів у перший список
    for data in [3, 1, 5, -5]:
        linked_list1.insert_at_end(data)
    print("Список 1 до реверсування:")
    linked_list1.print_list()

    # Реверсування першого списку
    linked_list1.reverse()
    print("Реверсований список 1:")
    linked_list1.print_list()

    # Сортування першого списку
    linked_list1.insertion_sort()
    print("Відсортований список 1:")
    linked_list1.print_list()

    # Додавання елементів у другий список
    for data in [2, 6, 4, 1, -1]:
        linked_list2.insert_at_end(data)
    print("Список 2 до сортування:")
    linked_list2.print_list()

    # Сортування другого списку
    linked_list2.insertion_sort()
    print("Відсортований список 2:")
    linked_list2.print_list()

    # Об'єднання відсортованих списків у новий відсортований список
    merged_list_head = LinkedList.merge_sorted_lists(linked_list1.head, linked_list2.head)
    merged_linked_list = LinkedList()
    merged_linked_list.head = merged_list_head
    print("Об'єднаний відсортований список:")
    merged_linked_list.print_list()


if __name__ == '__main__':
    main()
