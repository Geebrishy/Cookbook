print('Hello\nenter your name')  # asks for a name
name = input()
print('hello, ' + name)

print('Type 1, 2, or 3 as of choice to the following\n1 for a cheeseburger\n2 for a soda\n3 for the fries')
order = input()

if order == "1":
    print('Here is your cheeseburger, ' + name)

if order == "2":
    print('Here is your soda, ' + name)

if order == "3":
    print('Here is your fries, ' + name)
