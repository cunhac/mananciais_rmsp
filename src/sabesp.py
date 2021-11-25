import requests
from datetime import date


def api_sabesp():

  date_today = date.today()

  url = f"http://mananciais.sabesp.com.br/api/Mananciais/ResumoSistemas/{date_today}"
  header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive'}
  response = requests.get(url, headers = header, verify=False)
  response_json = response.json()
  volume_total = (str(response_json['ReturnObj']['total']['VolumePorcentagemAR']))

  return volume_total

