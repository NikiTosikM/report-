from tabulate import tabulate

from src.app.models.person import Person


class CreateReport:
    """Класс для составления отчета"""

    def __init__(self, persons_info: list[Person]):
        self.persons_info = persons_info

    def computing_performance(self, criteria: str):
        post_perf: dict = {}  # должность: эффективность
        for (
            person
        ) in self.persons_info:  # достаем значение эффективности с каждого сотрудника
            value = getattr(person, criteria)  # значение атрибута модели

            if person.position not in post_perf:
                post_perf[person.position] = []
            post_perf[person.position].append(value)

        average_perf_post = {}
        for post, perfs in post_perf.items():
            sum_all_perfs = sum([float(perf) for perf in perfs])
            arithmetic_mean_perf = round(sum_all_perfs / len(perfs), 2)
            average_perf_post[post] = arithmetic_mean_perf

        sorted_post = sorted(
            average_perf_post.items(), key=lambda item: item[1], reverse=True
        )  # сортируем по эффективности

        return sorted_post

    def display(self, data: dict):
        """Отображение результатов в консоли"""

        headers = ["position", "performance"]
        return tabulate(data, headers=headers)
