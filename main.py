import random
from datetime import datetime

def arrToBday(arr):
    for i in range(len(arr)):
        day_num = str(arr[i])
        # adjusting day num
        day_num.rjust(3 + len(day_num), '0')
        # Initialize year
        year = "2021" # a non leap year, so 365 days in the year
        # converting to date
        res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%b-%d-%Y")

        arr[i] = res

    return arr


N = 10000 #number of trials
# n = input("number of babies to compare: ")
n = 75
count = 0

for x in range(N):
# every cycle in this loop represents taking a sample and testing it
    babies_bday = []
    # giving birth to 50 babies with random bday
    for i in range(int(n)):
        bday = random.randint(1,365)
        babies_bday.append(bday)

    # comparing the bdays to find if there are 2 babies with same bday
    report = False # report = 1 means the sample has 2 babies with same bday. 
    for i in range(len(babies_bday)):
        for j in range(len(babies_bday)):
            if j!=i:
                if babies_bday[i] == babies_bday[j]:
                    report = True

    if report == True:
        count = count + 1

    print("taking", n, "random babies from the population.... \n their birthdays are: ")
    print(arrToBday(babies_bday))
    print("2 baby has same birthday? ", report, "\n")


print('\n total no of trials: ', N)
print('\n no of success: ', count)
print('\n probability of 2 babies having same birthday among a random sample on', n, 'babies=  ' , count, '/', N, '=', count/N)