first_name = 'Allan'
last_name = 'Smith'

# Normal Formating
sentence1 = 'My name is {} {}'.format(first_name, last_name)

# F-Strings
##
sentence2 = f'My name is {first_name} {last_name}'
sentence3 = f'My name is {first_name.upper()} {last_name.upper()}'

print(sentence1)
print(sentence2)
print(sentence3)

##
for n in range(1,3):
    sentence4 = f'The value is {n}'
    sentence5 = f'The value is {n:02}'
    print(sentence4)
    print(sentence5)

##
pi = 3.14159265
sentence6 = f'Pi is equal to {pi:.4f}'
print(sentence6)

##
from datetime import datetime
bday = datetime(1990, 1, 1)
sentence7 = f'Jenn has a birthday on {bday:%B %d, %Y}'
print(sentence7)
