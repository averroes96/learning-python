# continue // ignore current iteration

numbers = range(15)

for number in numbers:
    if number == 13:
        continue
    print(number)

print("=" * 48)


# break // quit the loop

numbers = range(15)

for number in numbers:
    if number == 13:
        break
    print(number)

print("=" * 48)

# pass // works as a comment to avoid identation error

numbers = range(15)

for number in numbers:
    if number == 13:
        pass
    print(number)

print("=" * 48)