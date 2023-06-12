def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return (sort_string(first_string), sort_string(second_string), False)

    # Ordena as duas strings usando a função sort_string
    sorted_str1 = sort_string(first_string)
    sorted_str2 = sort_string(second_string)
    # Verifica se as strings ordenadas são iguais
    return (sorted_str1, sorted_str2, sorted_str1 == sorted_str2)


def sort_string(string):
    # Converte a string para minúsculas
    string = string.lower()
    # Converte a string em uma lista de caracteres
    chars = list(string)
    # Ordena a lista de caracteres usando o algoritmo de merge sort
    merge_sort(chars)
    # Retorna a string ordenada como uma única string
    return "".join(chars)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
