#Условие задачи
#На выборах мэра города жители голосуют за одного из трёх кандидатов. Каждый кандидат имеет номер (1, 2, 3). Нужно провести голосование и узнать имя победителя. Голоса могут разделиться!
#Задача:
#Реализуйте функцию vote, которая принимает список голосов и определяет номер победителя (того, кто набрал больше всего голосов):
#Если один кандидат набрал больше голосов, чем остальные, функция должна вернуть его номер.
#Если несколько кандидатов набрали одинаковое максимальное количество голосов, функция должна вернуть строку "Нужен второй тур выборов".
#Пример списка голосов:
#Входные данные:
#votes = [3, 2, 1, 3, 1, 3, 1, 3, 2, 2, 2, 2, 1, 1, 2]
#Результат:
#2

#ходные данные:
#votes = [1, 2, 2, 3, 2, 1, 1, 3, 2, 3, 2, 2, 3, 3, 1, 2, 1, 3, 3, 1]
#Результат:
#Нужен второй тур выборов
# Глобальная переменная для хранения votes_count

votes_count_global = None

def check_votes_count(votes_count):
    """Функция для проверки подсчёта голосов (не изменяйте её)"""
    global votes_count_global
    votes_count_global = votes_count
    return votes_count

# Впишите ваше решение в функцию vote
def vote(votes):
    # используется для проверки корректности словаря
    # не убирайте эти две строки
    global votes_count_global
    votes_count_global = None

    # 1) создайте словарь для подсчёта голосов
    votes_count = dict.fromkeys(votes)
    rivals = set(votes)

    max_votes = 0
    for rival in rivals:
        votes_count[rival] = votes.count(rival)
        if max_votes < votes.count(rival):
            max_votes = votes.count(rival)

    #print(votes_count)

    # проверка словаря, не убирайте строку ниже
    votes_count_global = check_votes_count(votes_count)

    # 3) найдите максимальное количество голосов

    # 4) найдите всех кандидатов с максимальным количеством голосов
    winners = []
    for rival in votes_count:
        if votes_count[rival] == max_votes:
            winners.append(rival)

            # 5) верните результат в зависимости от количества победителей
    if len(winners) == 1:
        return winners[0];
    else:
        return "Нужен второй тур выборов"

if __name__ == '__main__':
    citizens_votes = [
        [3, 2, 3, 2, 1, 1, 1, 3, 1, 1],
        [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 2, 1, 2, 1, 1],
        [1, 2, 2, 3, 2, 1, 1, 3, 2, 3, 2, 2, 3, 3, 1, 2, 1, 3, 3, 1],
        [2, 2, 1, 3, 3, 2, 3, 1, 1, 2, 1, 2, 2, 2, 3],
        [3, 3, 2, 2, 1, 3, 1, 2, 3, 1, 2, 2, 1, 3, 3],
    ]

    print(vote(citizens_votes[0]))
    print(vote(citizens_votes[1]))
    print(vote(citizens_votes[2]))
    print(vote(citizens_votes[3]))
    print(vote(citizens_votes[4]))