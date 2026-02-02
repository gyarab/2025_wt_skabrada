import httpx

odkaz = httpx.get('https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt')
lines = odkaz.text.splitlines()

kurz = None
for line in lines:
    if line.startswith("EMU|"):
        kurz = float(line.split("|")[-1])
        break

if kurz is None:
    print("Kurz nebyl nalezen")
    exit()

zadana_mena = input("Z jaké měny převádíme: EUR nebo CZK >").strip().upper()
prevod = input("Do jaké měny převádíme: EUR nebo CZK >").strip().upper()

if zadana_mena not in ("EUR", "CZK") or prevod not in ("EUR", "CZK"):
    print("Neznámá informace pro systém.")
    exit()

if zadana_mena == prevod:
    print("To potom není převod...")
    exit()

try:
    mnozstvi = float(input("Zadejte množství: "))
    if mnozstvi <= 0:
        print("Měna má být pozitivní.")
        exit()
except ValueError:
    print("Neplatná částka.")
    exit()


if zadana_mena == 'EUR' and prevod == 'CZK':
    vysledek = mnozstvi * kurz

elif zadana_mena == 'CZK' and prevod == 'EUR':
    vysledek = mnozstvi / kurz

print(f" {mnozstvi:.2f} {zadana_mena} = {vysledek:.2f} {prevod}")