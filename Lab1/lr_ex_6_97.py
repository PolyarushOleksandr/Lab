#This program calculates the ages of a father and his son based on\
    # the given relationship between their ages.
#The user is prompted to input two integers: the first integer (n)\
    # represents the total age of the father and son combined,
#and the second integer (m) represents the ratio of the father's\
    # age to the son's age.
n, m = map(int, input("Enter two integers separated by a space: ").split())
son_age = n // (m - 1)
father_age = m * son_age

print(father_age, son_age)
