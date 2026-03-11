def round_scores(student_scores: list[float | int]) -> list[int]:
    rounded_scores = []
    for score in student_scores:
        integer_part = int(score)
        fractional_part = score - integer_part
        
        if fractional_part > 0.5:
            rounded_score = integer_part + 1
        else:
            rounded_score = integer_part
            
        rounded_scores.append(rounded_score)
    return rounded_scores


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    result = []
    for score in student_scores:
        if score >= threshold:
            result.append(score)
    return result


def letter_grades(highest: int) -> list[int]:
    interval = (highest - 40) / 4
    
    grade_3_min = int(40 + interval) + 1
    grade_4_min = int(40 + 2 * interval) + 1
    grade_5_min = int(40 + 3 * interval) + 1
    
    return [grade_3_min, grade_4_min, grade_5_min]


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    ranking = []
    for i in range(len(student_scores)):
        rank = i + 1 
        name = student_names[i]
        score = student_scores[i]
        ranking.append(f"{rank}. {name}: {score}")
    return ranking