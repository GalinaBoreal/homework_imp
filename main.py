from datetime import datetime

from colorama import init, Fore, Back, Style

from application.db.people import get_employees
from application.salary import calculate_salary


init(autoreset=True)  # Initializes Colorama


class Accountant:
    def __init__(self, name):
        self.name = name

    def payment(self):
        emploer = get_employees()
        current_datetime = datetime.now().date()
        print(
            Style.BRIGHT + Back.YELLOW + Fore.BLACK + emploer
        )
        calculate_salary()
        print(Style.NORMAL + Fore.LIGHTMAGENTA_EX + f'Бухгалтер: {self.name}, {current_datetime}')


def accountant(name):
    accountant = Accountant(name)
    accountant.payment()

if __name__ == '__main__':
    accountant('Петрова Надежда')
