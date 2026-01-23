import httpx

c = httpx.get('https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt')
print(c.text)

lines = c.text.split('\n')
print(lines[0])

line_euro = ""

for line in lines:
    if "EUR" in line:
        line_euro = line
        break

rare_str = line_euro.split('|')[-1].replace(',' , ',')
rate = float(rare_str)

print("kurz eura je" , rate)

value_in = float(input("kolik mas eur?"))
value_out = value_in * rate

print(f"tak to je {value_out:.2f} korun")