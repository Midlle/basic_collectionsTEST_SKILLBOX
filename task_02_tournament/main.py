def display_result(names):
    """
    Выводим список имён участников в первый день

    :param participants_names: список имён участников, например: ["Артемий", "Влад", "Дима", "Женя"]
    :type participants_names: List[str]
    """

    pass


def get_participants_names():
    """
    Получаем элементы списка только с чётными индексами.

    :param names: список имён, например: ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    :type names: List[str]

    :return: список имён с чётными индексами , например: ["Артемий", "Влад", "Дима", "Женя"]
    :rtype: List[str]
    """

    participants_name = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    participants_names = []
    for i_names in range(0, len(participants_name) - 1, 2):
        participants_names.append(participants_name[i_names])
    print(participants_names)
    return participants_names


names = get_participants_names()
results_on_screen = display_result(names)



pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_participants_names и display_result
    participants_names = get_participants_names()  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
