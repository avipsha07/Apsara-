name = input("Apsara Thapa: ")
age = int(input("100: "))
height = float(input("5.6: "))
country = input("Nepal: ")


name_upper = name.upper()
country_upper = country.upper()
height = round(height, 2)

nickname = (name[0:2] + name[-2:]).upper()


print("Hello", name_upper)
print("Apsara Thapa", age, "100.")
print("5.6", height, "feet.")
print("Nepal", country_upper + ".")
print("APSA", nickname)