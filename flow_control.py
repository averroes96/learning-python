### if elif else

name = "Ada"
country = "Algeria"
coursePrice = 1200
status = "Student"

if country == "Algeria" :
    print(f"Course price is: {coursePrice:,.2f} DA")
elif country == "France" :
    print(f"Course price is: {coursePrice / 150:,.2f} euro")
else:
    print(f"Course price is: {coursePrice / 130:.2f} $")

print("=" * 48)

### Nested condition
if country == "Algeria" :
    if status == "Student":
        print(f"Course price is: {coursePrice - 300:,.2f} DA")
    else:
        print(f"Course price is: {coursePrice:,.2f} DA")
elif country == "France" :
    if status == "Student":
        print(f"Course price is: {(coursePrice - 300) / 150:,.2f} Euro")
    else:
        print(f"Course price is: {coursePrice:,.2f} Euro")
else:
    if status == "Student":
        print(f"Course price is: {(coursePrice - 300) / 130:,.2f} $")
    else:
        print(f"Course price is: {(coursePrice - 300) / 130:,.2f} $")

print("=" * 48)
### Ternary conditional operator

print(f"Course price is: {coursePrice - 300:,.2f} DA" 
        if status == "Student"
        else f"Course price is: {coursePrice:,.2f} DA")