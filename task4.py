from datetime import datetime, timedelta

date_format = "%Y.%m.%d"

def get_upcoming_birthdays(users):
  result = []
  
  current_date = datetime.today().date()
  current_year = current_date.year
  
  for user in users:
    birthdate = datetime.strptime(user['birthday'], date_format).date().replace(current_year)
    if birthdate < current_date:
      birthdate = birthdate.replace(year=current_year + 1)

    if (birthdate - current_date).days > 7:
      continue
    
    congratulation_date = birthdate

    weekday = birthdate.weekday()
    if weekday == 5:
      congratulation_date = congratulation_date + timedelta(days=2)
    elif weekday == 6:
      congratulation_date = congratulation_date + timedelta(days=1)
    
    result.append({
      "name": user["name"],
      "congratulation_date": datetime.strftime(congratulation_date, date_format) 
    })
  
  return result
    

users = [
    {"name": "Kosta", "birthday": "1985.07.06"},
    {"name": "Moshka", "birthday": "1985.07.07"},
    {"name": "Nichka", "birthday": "1985.07.08"},
    {"name": "Jane Smith", "birthday": "1990.07.10"},
    {"name": "Nazar", "birthday": "1990.07.30"},
    {"name": "Ostap", "birthday": "1990.01.30"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

