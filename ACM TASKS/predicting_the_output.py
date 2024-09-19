from csv import *
def loading_data():
    with open("data.csv", "w", newline='') as file1:  
        write = writer(file1)
        data = [
            [0.0, 0.0, 0.0], [0.5, 1.5, 23.4], [1.2, 2.3, 45.6], [1.8, 3.7, 12.1],
            [2.4, 4.2, 78.9], [2.9, 5.1, 34.5], [3.5, 6.4, 56.7], [4.1, 7.8, 67.8],
            [4.7, 8.5, 89.0], [5.2, 9.1, 12.3], [5.8, 1.0, 45.6], [6.3, 2.4, 78.9],
            [6.9, 3.1, 34.5], [7.4, 4.6, 56.7], [8.0, 5.2, 67.8], [8.6, 6.8, 89.0],
            [9.1, 7.3, 12.3], [9.7, 8.9, 45.6], [10.0, 9.0, 78.9], [10.5, 0.5, 34.5]
        ]
        write.writerows(data)
        file1.close()
def search():
    a = float(input("Please enter the first number "))
    b = float(input("Please enter the second number "))
    with open("data.csv", "r") as file1:
        data = reader(file1)
        for row in data:
            if float(row[0]) == a and float(row[1]) == b:
                return float(row[2])
        else:    
            return None  

loading_data()
while True:
    result = search()  
    if result is  None:
        print("No match found for the given inputs.")
    else:
        print("The value corresponding to a and b is: ",result)
    
    ch = input("Do you want to search again? (yes/no): ")
    if ch.lower() == "no":
        print("thank you")
        break