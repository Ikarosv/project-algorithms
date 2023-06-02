def study_schedule(permanence_period: list[tuple[int, int]], target_time: int):
    if not str(target_time).isnumeric():
        return None
    count = 0
    for student in permanence_period:
        if not str(student[0]).isnumeric() or not str(student[1]).isnumeric():
            return None
        if int(student[0]) <= target_time <= student[1]:
            count += 1
    return count
