# O(N**2) ----------------- Insertion Sort -----------------------------------
def insertion_sort(a_list: list) -> None:
    """
    Sorting by insertion
    :param a_list: list
    :return: None
    """
    N = len(a_list)
    for n in range(1, N):
        key = n
        while key > 0 and a_list[key - 1] > a_list[key]:
            a_list[key], a_list[key - 1] = a_list[key - 1], a_list[key]
            key -= 1








# O(N**2) ----------------- Choice Sort --------------------------------------
def choice_sort(a_list: list) -> None:
    """
    Sorting by choice method
    :param a_list: list
    :return: None
    """
    N = len(a_list)
    for pos in range(0, N-1):
        for i in range(pos+1, N):
            if a_list[i] < a_list[pos]:
                a_list[i], a_list[pos] = a_list[pos], a_list[i]







# O(N**2) ----------------- Bubble Sort --------------------------------------
def bubble_sort(a_list: list) -> None:
    """
    Sorting by bubble method
    :param a_list: list
    :return: None
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swapped = True