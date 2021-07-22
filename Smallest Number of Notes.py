if __name__ == '__main__':
    currencies = [100, 50, 10, 5, 2, 1]
    for i in range(int(input())):
        exchange_currency = int(input())
        notes = 0
        for currency in currencies:
            rem = exchange_currency % currency
            div = int(exchange_currency / currency)
            if div != 0:
                notes += div
                exchange_currency = rem
                rem = 0
                div = 0
        print(notes)
