import httpx

c = httpx.get('https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt')
print(c.text)

lines = c.text.split('\n')
print(lines[0])