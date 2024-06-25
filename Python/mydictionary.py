# Python dictionary is also called JSON in other programming languages
# JavaScript Object Notation (JSON)
# Dictionary is also using {}
# the data is ordered
# the data is indexed by key (not by number)
# every single data is associated with a key
# for example firstname is akey and peter is the data
# Key cannot be duplicated, data can be duplicated
# It is modifiable
foreigner = {
    "firstname": "Peter",
    "lastname": "Parker",
    "passportnumber" : "EAG25001600",
    "incometaxnumber": "MYR25001600",
    "pcbamount": 201,
    "lastmonth" : 1,
    "lastyear" : 2024,
    "previous": [(4, 2024, 891), (3, 2024, 895), (2, 2024, 982), (1, 2024, 892)],
    "address": {
        "Office": {
            "street": "Persiaran Multimedia I-City",
            "taman": "Shah Alam"
        },
        "home": {
            "street": "Jalan Tun Hussien Onn",
            "taman": "Bintulu"           
        }
    },
    "contact":"01125001600"
}
print("First Name:", foreigner['firstname'])
print("Last Name:", foreigner['lastname'])
print("Passprt Number:", foreigner['passportnumber'])
print("Income Number:", foreigner['incometaxnumber'])
print("PCB Amount:", foreigner['pcbamount'])
print("Last Month:", foreigner['lastmonth'])
print("Last Year:", foreigner['lastyear'])

# for item in foreigner["previousmonth"]
# item will hold a tuple (4, 2024, 891)
# however we know tuple is auto explodable
# as long as we have 3 variables we can explode and hold the 3 values
for month, year, amount in foreigner["previous"]:
    print(f"Transaction: {month}-{year} RM{amount}")

officeAddress = foreigner["addresses"]["office"]
print("Street:", officeAddress["street"])
print("Taman:", officeAddress["taman"])
homeAddress = foreigner["address"]["home"]
print("Street:", officeAddress["street"])
print("Taman:", officeAddress["taman"])

# you can access the street directly as follows:
foreigner["addresses"]["office"]["street"]

# sometimes we may not know the keys

# when you use method items you will get the key, value
for key

# how can i modify the dictionary
# since the key car does not exist in the dictionary it gets added automatically
foreigner["car"] = {
    "brand": "Proton",
    "model": "SAGA",
    "carplate": "QTD3693"
}
foreigner["salary"] = 4890
print(foreigner)

# if i want to modify the salary
# since the salary is already there it modifies/updates the existing salary
foreigner["salary"] = 5120
print(foreigner)

foreigner.pop('car')
print(foreigner)