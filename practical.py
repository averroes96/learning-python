### email slicing

email = "addavigner@gmail.com"  # the email

arobazIndex = email.index("@") # get the position of the arobaz

print(email[0: arobazIndex].strip()) # get the first part of the email
print(email[arobazIndex + 1 :].strip()) # get the second part

print("=" * 48)

### Your age full details

age = int(input("Enter your age: ").strip())

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("Your age full details : ")
print(f"{months:,} Month(s)")
print(f"{weeks:,} Week(s)")
print(f"{days:,} Day(s)")
print(f"{hours:,} Hour(s)")
print(f"{minutes:,} Minute(s)")
print(f"{seconds:,} Second(s)")

print("=" * 48)