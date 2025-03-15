import requests  # HTTP сұрауларын орындау үшін requests кітапханасын қосамыз

# API-дан деректерді алу үшін функция
def get_data(url):
    response = requests.get(url)  # URL-ге сұрау жібереміз
    if response.status_code == 200:  # Егер жауап коды 200 болса (сәтті жауап)
        return response.json()  # Жауапты JSON форматына айналдырып қайтарамыз
    else:
        print(f"Сұрау қатесі: {response.status_code}")  # Қате туралы хабарлама шығарамыз
        return None  # Қате болған жағдайда бос мән қайтарамыз

# Валюта тізімін алу функциясы
def fetch_currencies():
    url = "https://api.ataix.kz/api/currencies"  # Валюталар API сілтемесі
    currencies = get_data(url)  # Деректерді аламыз
    if currencies:  # Егер жауап бос болмаса
        print("Валюталар тізімі:")
        print("RAW DATA:", currencies)  # Шикі деректерді шығару
        print(f"Жалпы валюталар саны: {len(currencies)}")  # Валюталардың жалпы санын шығару

# Сауда жұптарын алу функциясы
def fetch_symbols():
    url = "https://api.ataix.kz/api/symbols"  # Сауда жұптарының API сілтемесі
    symbols = get_data(url)  # Деректерді аламыз
    if symbols:
        print("Сауда жұптары тізімі:")
        print("RAW DATA:", symbols)  # Шикі деректерді шығару
        print(f"Жалпы сауда жұптары саны: {len(symbols)}")  # Сауда жұптарының жалпы санын шығару

# Бағаларды алу функциясы
def fetch_prices():
    url = "https://api.ataix.kz/api/prices"  # Бағалар API сілтемесі
    prices = get_data(url)  # Деректерді аламыз
    if prices:
        print("Монеталар мен токендердің бағалары:")
        print("RAW DATA:", prices)  # Шикі деректерді шығару

# Бағдарламаның негізгі функциясы
def main():
    fetch_currencies()  # Валюталар туралы деректерді аламыз
    fetch_symbols()  # Сауда жұптары туралы деректерді аламыз
    fetch_prices()  # Бағалар туралы деректерді аламыз

# Егер бұл файл негізгі бағдарлама ретінде орындалса, main() функциясы іске қосылады
if __name__ == "__main__":
    main()
