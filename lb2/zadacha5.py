day:int = int(input())

if day < 1 and day > 7:
    exit

day_name:string

if day == 1:
    day_name = "Понеделник"

if day == 2:
    day_name = "Вторник"
    
if day == 3:
    day_name = "Сряда"
    
if day == 4:
    day_name = "Четвъртък"

if day == 5:
    day_name = "Петък"

if day == 6:
    day_name = "Събота"

if day == 7:
    day_name = "Неделя"

print(str(day) + "->" + day_name)