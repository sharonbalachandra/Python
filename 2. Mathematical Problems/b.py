# Print the following pattern
#  1
#  2 2
#  3 3 3
#  4 4 4 4
#  5 5 5 5 5

# First attempt
string1 = "1"
string2 = "2"
string3 = "3"
string4 = "4"
string5 = "5"
print("\n",string1*1,"\n",string2*2,"\n",string3*3,"\n",string4*4,"\n",string5*5)


# Improved way
list = ["1", "2", "3", "4", "5"]
for x in list:
    print(x*int(x))

# Or...
list = [1, 2, 3, 4, 5]
for x in list:
    print(x*str(x))