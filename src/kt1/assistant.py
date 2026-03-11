"""
В этом задании нужно закодить программу-ассистента для помощи в проверке экзаменов:

1. Округление баллов
2. Список лучших результатов
3. Перевод в пятибальную систему
4. Вывод рейтинга
"""


def round_scores(student_scores: list[float | int]) -> list[int]:
    """Округляет все переданные баллы до целых.

    >>> round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45])
    [90, 40, 55, 70, 31, 25, 80]

    :param student_scores: list[float | int] - список исходных оценок.
    :return: list[int] - новый список округленных оценок.
    """
    rounded = []
    for score in student_scores:
        if score - int(score) >= 0.5:
            rounded.append(int(score) + 1)
        else:
            rounded.append(int(score))
    return rounded


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Фильтрует результаты по пороговому баллу.

    Фильтрует результаты, оставляя только те, что превосходят переданный пороговый балл.

    >>> above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
    [90,75,83,96]

    :param student_scores: list[int] - список округленных баллов.
    :param threshold: int - пороговый балл.
    :return: list[int] - новый список с баллами не ниже порогового.
    """
    result = []
    for score in student_scores:
        if score >= threshold:
            result.append(score)
    return result


def letter_grades(highest: int) -> list[int]:
    """Вычисляет минимальные баллы для перевода в оценки.

    Вычисляет минимальные баллы, соответствующие оценкам "3", "4", "5",
    на основе наилучшего результата по всем студентам и минимального балла 40.

    Так, если наивысший полученный балл 100, получим следующую таблицу перевода:

        "Н/А" <= 40
    41 <= "Н/А" <= 55
    56 <=  "3"  <= 70
    71 <=  "4"  <= 85
    86 <=  "5"  <= 100

    >>> letter_grades(highest=100)
    [56, 71, 86]

    Если наивысший балл это 88, таблицы перевода изменятся:
        "Н/А" <= 40
    41 <= "Н/А" <= 52
    53 <=  "3"  <= 64
    65 <=  "4"  <= 76
    77 <=  "5"  <= 88

    >>> letter_grades(highest=88)
    [53, 65, 77]

    :param highest: int - наивысший полученный балл.
    :return: list - наименьшие баллы, с которых начинаются тройка, четверка и пятёрка.
    """
    step = (highest - 40) // 4
    
    grade_3 = 40 + step + 1
    grade_4 = grade_3 + step
    grade_5 = grade_4 + step
    
    return [grade_3, grade_4, grade_5]


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Формирует форматированный рейтинг.

    Формирует форматированный по образцу список студентов
    и их баллов, отсортированный от лучших баллов к худшим,
    добавляя итоговое "место" студента в рейтинге.

    >>> student_scores = [100, 99, 90, 84, 66, 53, 47]
    >>> student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
    >>> student_ranking(student_scores, student_names)
    ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']

    :param student_scores: list[int] - список баллов, расположенных по убыванию.
    :param student_names: list[str] - список имён студентов, расположенных по убыванию оценок.
    :return: list[str] - список строк в формате "<rank>. <student name>: <score>".
    """
    ranking = []
    for i in range(len(student_names)):
        rank = i + 1
        ranking.append(f"{rank}. {student_names[i]}: {student_scores[i]}")
    return ranking
