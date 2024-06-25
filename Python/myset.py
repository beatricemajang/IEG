# set uses {}
# set is modifiable (add, edit and delete)
# set is unordered (the items do not retain its position) 
# set is not indexed (do not have 0, 1, 2, 3, 4...)
# set does not allow duplicates

# in python this is the first time we are using {}
x = {10, 20, 30, 40, 50, 20, 60, 70}
print(x)

# what do you observe
# 1. numbers are not in the same order as it was created
# 2. duplicate numbers are missing

# selection and indexing
# since set is not indexed you cannot retrieve the values using [] syntax
# to retrieve the items inside the set
# the only way is to use for loop
for i in x:
    print(i)

# modifiable
fruits = {"apple", "orange", "mango"}
print(fruits)
fruits.add("durian") # add at a random place
print(fruits)

# to delete an item in the set
fruits.remove("orange")
print(fruits)

# pop => randomly removes an item in the set
fruits.pop()
print(fruits)

# ifyou want to update an item
# 1. remove the item
# 2. add the new item

fruits = {"apple", "orange", "apple", "mango", "banana", "apple"}
uniquefruits = set(fruits)
print(uniquefruits)

overseafruits = {"apple", "orange", "mango", "banana", "grapes"}
localfruits = {"durian", "rambutan", "cempedak", "banana", "mangosteen"}
print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits))
print(localfruits.difference(overseafruits))

favfruits = {"durian", "rambutan", "mangosteen"}
print(favfruits.issubset(localfruits))
print(localfruits.issuperset(favfruits))
print(favfruits.isdisjoint(overseafruits))

emailcontent = '''The examples above highlight how cyber criminals
can find so many ways to trick you into giving information.
To protect against phishing attacks, people need to be aware 
of the various types of phishing attacks and know how phishing happens.
The key to prevention is creating a high level of cyber security 
awareness through training and practice. Phishing simulations are an 
ideal way to train users how to identify and avoid phishing attacks.
They show users different types of phishing emails and test their 
powers of discernment. They give employees first-hand experience of 
phishing scenarios and demonstrate how easy it is to be tricked by what 
looks like authentic communication through a valid email.
When people return to real life scenarios, they're more likely to 
carefully review emails, URLs and the context of communication before acting
on instinct. Phising simulations teach people to pause and analyze 
before automatically clicking Reply, visiting embedded links, or downloading 
unsecure attachments. '''

words = emailcontent.split()
print(len(words))

uniquewords = set(words)
print(len(uniquewords))
print(uniquewords)

cleanwords = []
for word in words:
    # word is instance of string class / word is a string object
    # remove is a method inside the word object
    # remove takes 2 arguments: first argument is used to find
    # second argument is used to replace
    word = word.replace(",", " ")
    word = word.replace(".", " ")
    word = word.lower()
    cleanwords.append(word)

uniquewords = set(cleanwords)
print(len(uniquewords))
print(uniquewords)

commonwords = {"is", "or", "of", "so", "by", "how", "when", "it", "on", "the", "into", "a",
               "to", "is", "are", "what", "be", "i", "you", "more", "and", "can", "an"}

uniquewords = uniquewords.difference(commonwords)
print(len(uniquewords))
print(uniquewords)

spamwords = {"tricked", "trick", "pishing", "security", "criminals"}
total_spamwords = uniquewords.intersection(spamwords)
print(len(total_spamwords))

# here we try to demonstrate the features of set data structure
# however, we have another library called NLTK, this has many other features
# required for NLP (Natural Language Processing)