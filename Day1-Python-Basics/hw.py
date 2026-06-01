houses = []
n = int(input('Enter number of house:'))
for i in range(0,n):
    print("House Number ",i+1)
    house = {}
    size = int(input("Enter area of house:"))
    bed = int(input("Enter Number of Beds:"))
    bathroom = int(input("Enter Number of bathrooms:"))
    cost = int(input('Enter The cost of the house:'))
    house["sqrt"] = size
    house["Bedrooms"] = bed
    house["Bathrooms"] = bathroom
    house["Price"] = cost

    houses.append(house)

print(houses)


