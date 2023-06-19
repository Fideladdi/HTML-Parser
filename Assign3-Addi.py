from bs4 import BeautifulSoup
table_tag = None

filename = 'xe_dot_com.html'
fd = open(filename, 'r', encoding='utf-8')

soup = BeautifulSoup(fd, 'html.parser')

table_tag = soup.find('table', class_='table__TableBase-sc-1j0jd5l-0 pTERB')


rates = {}

tr_div = table_tag.tbody.find_all('tr')
for div in tr_div:
    currency = div.td.a.text.strip()
    rate = float(div.find_all('td')[1].text.strip())
    rates[currency] = rate

valid_currencies = ['EUR', 'GBP', 'USD', 'CAD']

sell_currency = input("Enter the base/sell currency(eg.EUR,GBP,USD): ").upper()
while sell_currency not in valid_currencies:
    print("Invalid currency. Please try again.")
    sell_currency = input("Enter the base/sell currency (e.g., EUR, GBP, USD): ").upper()

exchange_amount = float(input("Enter the amount to exchange: "))

buy_currency = input("Enter the quote/buy currency(eg.USD,EUR,USD,CAD): ").upper()
while buy_currency not in valid_currencies:
    print("Invalid currency. Please try again.")
    buy_currency = input("Enter the quote/buy currency (e.g., USD, EUR, USD, CAD): ").upper()

conversion_rate = None

match (sell_currency, buy_currency):
    case ('EUR', 'USD'):
        conversion_rate = float(rates['EUR / USD'])
    case ('GBP', 'EUR'):
        conversion_rate = float(rates['GBP / EUR'])
    case ('GBP', 'USD'):
        conversion_rate = float(rates['GBP / USD'])
    case ('USD', 'CAD'):
        conversion_rate = float(rates['USD / CAD'])
    case _:
        print("Unsupported conversion.")
        exit()

converted_amount = exchange_amount * conversion_rate

currency_symbols = {
    'GBP': chr(0x00A3),
    'EUR': chr(0x20AC),
    'USD': chr(0x0024),
    'CAD': 'C' + chr(0x0024)
}
print(f"{currency_symbols[sell_currency]}{exchange_amount:.2f} is equivalent to "
      f"{currency_symbols[buy_currency]}{converted_amount:.2f}")

fd.close()

if __name__ == '__main__':
   print('Successful')
