# Python dictionary is also called JSON in other programming languages
# JavaScript Object Notation (JSON)
# Dictionary is also using {}
# The data is ordered
# The data is indexed by key (not by number)
# Every single data is associated with a key
# For example firstname is a key and Peter is the data
# Key cannot be duplicated, Data can be duplicated
# It is modifiable
foreigner = {
    "firstname": "Peter",
    "lastname": "Parker",
    "passportnumber": "E4837589",
    "incometaxnumber": "SG834934",
    "pcbamount": 892,
    "lastmonth": 5,
    "lastyear": 2024,
    "previousmonth":[(4, 2024, 891), (3, 2024, 895), (2, 2024, 893), (1, 2024, 892)],
    "addresses": {
        "office": {
            "street": "15, Lorong 8/10",
            "taman": "Puchong"
        },
        "home": {
            "street": "215, Jalan SS 8/10",
            "taman": "Subang"
        }
    },
    "contact":"0169652347"
}

print("First Name:", foreigner["firstname"])
print("Last Name:", foreigner["lastname"])
print("Passport Number:", foreigner["passportnumber"])
print("Income Number:", foreigner["incometaxnumber"])
print("PCB Amount:", foreigner["pcbamount"])
print("Last Month:", foreigner["lastmonth"])
print("Last Year:", foreigner["lastyear"])

# for item in foreigner["previousmonth"]:
# item will hold a tuple (4, 2024, 891)
# however we know tuple is auto explodable
# as long as we have 3 variables we can explode and hold the 3 values
for month, year, amount in foreigner["previousmonth"]:
    print(f"Transaction: {month}-{year}  RM{amount}")

officeAddress = foreigner["addresses"]["office"]
print("Street:", officeAddress["street"])
print("Taman:", officeAddress["taman"])
homeAddress = foreigner["addresses"]["home"]
print("Street:", homeAddress["street"])
print("Taman:", homeAddress["taman"])

# you can access the street directly as follows
foreigner["addresses"]["office"]["street"]

# sometimes we may not know the keys
print(foreigner.keys())
for key in foreigner.keys():
    # isinstance is a built in function to determine the type of the variable
    if (isinstance(foreigner[key], list)):
        for item in foreigner[key]:
            print(item)
    else:
        print(foreigner[key])

# when you use the method items you will get the key, value
for key, value in foreigner.items():
    print(key, value)

# how can i modify the dictionary
# since the key car does not exists in the dictionary it gets added automatically
foreigner["car"] = {
    "brand": "Proton",
    "model": "SAGA",
    "carplate": "JXY7843"
}
foreigner["salary"] = 4890
print(foreigner)

# If I want to modify the salary
# Since the salary is already there it modifies/updates the existing salary
foreigner["salary"] = 5120
print(foreigner)

foreigner.pop('car')
print(foreigner)
