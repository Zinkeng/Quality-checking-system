
Weight = float(input("Enter weight "))
print(Weight)
unit = input("(L)bs or Kg? ")
print(unit)

if unit.upper() == 'L':
    weight_kg = 0.45 * Weight
    print(f"your weight in kilograms is {weight_kg}: " )


elif unit.upper() == 'KG':
    weight_lbs = float(Weight)/0.45
    print(f"your weight in pounds is {weight_lbs}: " )
#Trying something...
 