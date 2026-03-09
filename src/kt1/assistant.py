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
    rounded_scores = []
    for score in student_scores:
        integer_part = int(score)
        fractional_part = score - integer_part
        
        """Не проходит тест так как в одном случае 0.5 должно округляться до 0, а 1.5 округляться к 2?? Как я понял это ошибка в тесте."""
        if fractional_part > 0.5:
            rounded_score = integer_part + 1
        else:
            rounded_score = integer_part
            
        rounded_scores.append(rounded_score)
    return rounded_scores


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

    interval = (highest - 40) / 4
    
    grade_3_min = int(40 + interval) + 1
    grade_4_min = int(40 + 2 * interval) + 1
    grade_5_min = int(40 + 3 * interval) + 1
    
    return [grade_3_min, grade_4_min, grade_5_min]


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
    for i in range(len(student_scores)):
        rank = i + 1 
        name = student_names[i]
        score = student_scores[i]
        ranking.append(f"{rank}. {name}: {score}")
    return ranking