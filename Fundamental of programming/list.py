my_list = [1,2,3,4]
print(len(my_list))

my_dictionary = {
    "name": "Anuj",
    "age": "30",
    "course": "Software and system engineering"
}

from per import Person

anuj = Person("Anuj",34)

anuj.introduction()

import random
int1 = random.randint(10,20)

from datetime import datetime

date = "22-03-2005"

date_py = datetime.strptime(date,"%d-%M-%Y")
date_now = datetime.now()
diff = date_now - date_py
print(date_py)