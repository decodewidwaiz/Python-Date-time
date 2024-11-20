###pip install DateTime
import datetime

today = datetime.date.today()
print("Today's date:", today)

###standard date 
formatted_date = today.strftime("%d-%m-%Y")
print("Today's date:", formatted_date)