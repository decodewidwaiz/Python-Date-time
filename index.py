###pip install DateTime
import datetime

##without format
today = datetime.date.today()
print("Today's date is:", today)

###standard date 
formatted_date = today.strftime("%d-%m-%Y")
print("Today's date is:", formatted_date)