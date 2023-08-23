import datetime

print(datetime.date.today())                # today date

print(datetime.date.today().strftime("%Y")) #year

print(datetime.date.today().strftime("%B")) #month

print(datetime.date.today().strftime("%d")) #date

print(datetime.date.today().strftime("%W")) #week number

print(datetime.date.today().strftime("%w")) #week day

print(datetime.date.today().strftime("%j")) #day number of year

print(datetime.date.today().strftime("%A")) #day of week

print(datetime.datetime.now())
