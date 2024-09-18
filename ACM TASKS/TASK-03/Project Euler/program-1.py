#QUESTION: If we list all the natural numbers below that are multiples of 3 or 5 , we get 3,5,6,9 . The sum of these multiples is .Find the sum of all the multiples of 3 or 5 below 1000.
#project euler question 1 
x=0
for i in range(1000):
    if i%3==0 or i%5==0:
        x+=i
    else:
        pass
print("The sum of the multiples of 3 and 5 below 1000 is ",x)
