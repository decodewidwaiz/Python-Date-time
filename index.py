###pip install DateTime
import datetime

###default format
today = datetime.date.today()
print("Today's date is:", today)

formatted_date = today.strftime("%d-%m-%Y")
print("Today's date is:", formatted_date)
