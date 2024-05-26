from heap_plot import create_heap_from_list, draw_heap_as_tree


def main():
    # Example heap as a list
    lst = [3, 1, 14, 7, 1, 9, 2, 6, 23]
    heap = create_heap_from_list(lst)
    draw_heap_as_tree(heap)


if __name__ == '__main__':
    main()
