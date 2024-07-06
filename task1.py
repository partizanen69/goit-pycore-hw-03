from datetime import datetime

def get_days_from_today(date: str):
  try:
    date = datetime.strptime(date, '%Y-%m-%d').date() 
  except Exception as e:
    print(f"Could not parse {date} as date object because of error: {e}")
    return None
  
  current_date = datetime.now().date()

  return (current_date - date).days
  
print(
  get_days_from_today('2024-01-01')
)
