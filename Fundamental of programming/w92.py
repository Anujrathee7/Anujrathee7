import csv
with open("titanic.csv","r") as csvfile:
    information = csv.DictReader(csvfile)
    age = 0
    male = 0
    female = 0
    oldest = 0
    total = 0
    for dictionary in information:
        if(dictionary['Sex'] == "male"):
            male = male + 1
            total = total + 1
        else:
            female = female + 1
            total = total + 1
        csv_age = dictionary['Age']
        if(csv_age != ""):
            age = age + float(csv_age)

            if(oldest < float(csv_age)):
                oldest = float(csv_age)
        
        else:
            total = total - 1
    
    print(f"The number of male passengers: {male}")
    print(f"The number of female passengers: {female}")
    print(f"The average age of passengers: {int(round(float(age)/float(total),0))}")
    print(f"The age of the oldest passenger: {int(oldest)}")