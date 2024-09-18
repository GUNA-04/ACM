#project -6 
def sum_of_squares():
    sum=0
    for i in range(1,101):
        sum=sum+(i**2)
    return sum
def square_of_sum():
    sum=0
    square=0
    for i in range(1,101):
        sum=sum+i
    square=(sum**2)
    return square

a=sum_of_squares()
b=square_of_sum()
c=(b-a)
print("the differencw between the sum of the squares and the square of the sum is:",c)
