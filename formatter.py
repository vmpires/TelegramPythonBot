import requests
import json

class Formatter:
    def get_br():
        urlbr = "https://covid19-brazil-api.now.sh/api/report/v1/brazil"
        responsebr = requests.get(urlbr)
        contentbr = responsebr.json()
        return (f"Atualmente o Brasil conta com {contentbr['data']['confirmed']} casos confirmados de Covid-19, totalizando {contentbr['data']['deaths']} mortes e {contentbr['data']['recovered']} recuperados.")

    def get_uf(uf):
        urluf = (f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{uf}")
        responseuf = requests.get(urluf)
        contentuf = responseuf.json()
        return (f"Atualmente o estado de {contentuf['state']} conta com {contentuf['cases']} casos confirmados de Covid-19, totalizando {contentuf['deaths']} mortes.")

print(Formatter.get_br())
print(Formatter.get_uf("SP"))
