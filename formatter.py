import requests
import json


class Formatter:

    def format_amount(amount):

        if amount < 10**6:
            # Thousands
            return f"{'{:,}'.format(amount)}".replace(',', '.')
        elif amount < 10**9:
            # Millions
            return f"{'{:,}'.format(amount)}".replace(',', '.')
        elif amount < 10**12:
                # Billions
            return f"{'{:,}'.format(amount)}".replace(',', '.')
        else:
            # Trillions
            return f"{'{:,}'.format(amount)}".replace(',', '.')

    def get_br():
        urlbr = "https://covid19-brazil-api.now.sh/api/report/v1/brazil"
        responsebr = requests.get(urlbr)
        contentbr = responsebr.json()
        return (f"País: Brasil\nCasos confirmados: {Formatter.format_amount(contentbr['data']['confirmed'])}\nMortes: {Formatter.format_amount(contentbr['data']['deaths'])}\nRecuperados: {Formatter.format_amount(contentbr['data']['recovered'])}")

    def get_uf(uf):
        urluf = (f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{uf}")
        responseuf = requests.get(urluf)
        contentuf = responseuf.json()
        return (f"Estado: {contentuf['state']}\nCasos: {Formatter.format_amount(contentuf['cases'])}\nMortes: {Formatter.format_amount(contentuf['deaths'])}")


#print(Formatter.format_amount(1000))
print(Formatter.get_br())
print(Formatter.get_uf("SP"))

