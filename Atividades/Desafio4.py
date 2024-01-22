anything = input("Type anything: ")

print("The type is: {}".format(type(anything)))
print("Is a num? {}".format(anything.isnumeric()))
print("Is a alpha? {}".format(anything.isalpha()))
print("Is a alphanum? {}".format(anything.isalnum()))
print("Is totally in uppercase? {}".format(anything.isupper()))
print("Is totally in lowercase? {}".format(anything.islower()))
print("Is capitalized? {}".format(anything.istitle()))