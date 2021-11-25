from sabesp import api_sabesp
from audio import produzir_audio
from datetime import date
from workadays import workdays


date_today = date.today()
year = date_today.year
date_workday=workdays.is_workday(date_today, country='BR', years=(year))

if date_workday == True:
  print("Hoje é dia útil")
  volume_total = api_sabesp()
  produzir_audio(volume_total)
  
else:
  print("Hoje não é dia útil.")
