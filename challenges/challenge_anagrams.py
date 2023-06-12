def is_anagram(first_string, second_string):
    if not len(first_string) or not len(second_string):
        return (sort_string(first_string), sort_string(second_string), False)
    # Converter as strings para minúsculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Remover espaços em branco das strings
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")

    # Verificar se as strings têm o mesmo tamanho
    if len(first_string) != len(second_string):
        return (sort_string(first_string), sort_string(second_string), False)

    # Ordenar as strings
    sorted_str1 = sort_string(first_string)
    sorted_str2 = sort_string(second_string)

    # Verificar se as strings ordenadas são iguais
    if sorted_str1 == sorted_str2:
        return (sorted_str1, sorted_str2, True)
    else:
        return (sorted_str1, sorted_str2, False)


def sort_string(s):
    # Converter a string em uma lista de caracteres
    chars = list(s)

    # Chamar a função de ordenação (exemplo usando o Merge Sort)
    merge_sort(chars)

    # Converter a lista de caracteres ordenada de volta para string
    sorted_string = "".join(chars)

    return sorted_string


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
