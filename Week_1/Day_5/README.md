Today we learned about Loops and Range() function, but we got lots of additional exercises before the project of the day, if i find any off those really good, i'll post my version here also as bonus content

The project for this day is to create a Password generator! I gotta say, i really thought that it would take a lot of time to do that, but i'm surprised by myself, i did it REALLY fast and didn't got stuck at any moment.

The teacher method:

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

Less variables since it didn't need a control variable, but for that i would had to look into random.shuffle, i'm happier with my method cause i made it without needing to search anything at all. Don't now it its failproof but it work.