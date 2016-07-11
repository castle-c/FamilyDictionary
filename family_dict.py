#Define a dictionary that contains information about several members of your family.

family = { 'sister': { 'name': 'Krista', 'age': 42 }, 'mother': { 'name': 'Cathie', 'age': 70 } }

  #Using a dictionary comprehension, produce output that looks like the following example.

#Krista is my sister and is 42 years old

my_family = [ str(v['name']) + ' is my ' + (k) + ' and is ' + str(v['age']) + ' years old' for (k,v) in family.iteritems()]

for fam in my_family:
  print fam



  #Helpful hint: To convert an integer into a string in Python, it's str(integer_value)
