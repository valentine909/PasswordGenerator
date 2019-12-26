from time import sleep
from datetime import date, datetime
DELAY = 0.01  # In minutes

current_date = str(date.today())
c = 0
while c < 5:
    if str(date.today()) == current_date:
        with open(current_date + ".txt", "a+") as f:
            f.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n")
    else:
        current_date = str(date.today())
        with open(current_date + ".txt", "w") as f:
            f.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n")
    sleep(60 * DELAY)
    c += 1
