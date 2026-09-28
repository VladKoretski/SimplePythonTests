def same_name(courses_list:list) -> list:
    mentors_names = []
    for course in courses_list:
        course_names = []
        mentors_list = course["mentors"] # Получаем список полных имён текущего курса
        for mentor in mentors_list:
            first_name = mentor.split()[0] # Берём первое слово (имя)
            course_names.append(first_name) # Сохраняем имя в список имён курса
        mentors_names.append(course_names) # Добавляем список имён в общий список

    result = []
    for names, course in zip(mentors_names, courses_list):
        unique_names = set(names) # Получаем множество уникальных имён
        same_name_list = [] # Пустой список для тёзок текущего курса

        for name in unique_names: # Проходим по уникальным именам
            if names.count(name) > 1: # Если имя встречается больше 1 раза -> есть тёзки
                for full_name in course["mentors"]: # Ищем всех преподавателей с таким именем
                    if full_name.split()[0] == name:
                        same_name_list.append(full_name)

        result.append(sorted(same_name_list)) # Сортируем и добавляем в результат

    return result