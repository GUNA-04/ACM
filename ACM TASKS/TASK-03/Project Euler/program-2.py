a = 0 
b = 1
sum =0  
for i in  range(4000000):
    if i%2==0 :
     sum =a+b 
a = b 
b =sum 
print("the sum of the even-valued terms:",sum )