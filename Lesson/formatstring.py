name = "David"
batch = 101
fee = 8480.6578
# traditionally how we do this
inputstring = f"Hello" + name + ",welcome to python class" + str(batch)
print(inputstring)

# how much of space is required
inputstring = f"Hello {name:40}, welcome to python class {batch}"
print(inputstring)

# align David to center
inputstring = f"Hello {name:^40}, welcome to python class {batch}"
print(inputstring)

# align David to right
inputstring = f"Hello {name:>40}, welcome to python class {batch}"
print(inputstring)

# you can also provide padding characters
inputstring = f"Hello {name:*>40}, welcome to python class {batch}"
print(inputstring)

# truncate to 3 characters
inputstring = f"Hello {name:.3}, welcome to python class {batch}"
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL."
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL."
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL for RM{fee:10.2f}."
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:b} in KL for RM{fee:.2f}."
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:b} in KL for RM{fee:10.2f}."
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:o} in KL for RM{fee:10.2f}."
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:10.2f}."
print(inputstring)

# let us focus on decimal. let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:,.2f}."
print(inputstring)