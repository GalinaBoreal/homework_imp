from colorama import Fore, Style

def calculate_salary():
    print(Style.NORMAL + Fore.LIGHTYELLOW_EX + f'Расчет оплаты труда: рабочих часов 100')
    print(
        Style.NORMAL + Fore.LIGHTGREEN_EX +
        'Начислено 100 000. Удержано 13 000. К оплате 87 000'
    )

