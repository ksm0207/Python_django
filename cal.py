import calendar


class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.day_names = ("월", "화", "수", "목", "금", "토", "일")
        self.months = (
            "1월",
            "2월",
            "3월",
            "4월",
            "5월",
            "6월",
            "7월",
            "8월",
            "9월",
            "10월",
            "11월",
            "12월",
        )

    def get_month(self):
        return self.months[self.month - 1]