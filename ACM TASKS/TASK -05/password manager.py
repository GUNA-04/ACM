def length(password):
    return len(password) == 8

def special(password):
    spe = ["$", "@", "#", "%", "!", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "~", "`"]
    return any(char in spe for char in password)

def num_char(password): 
    if password[0].isdigit() or password[0] in ["$", "@", "#", "%", "!", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "~", "`"]:
        return False
    return True

def capital_small(password):
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_upper and has_lower

def validity(password):
    
    a = length(password)
    b = not_allowed(password)
    c = special(password)
    d = num_char(password)
    e = capital_small(password)

    if a and b and c and d and e:
        print("Password is accepted")           
    else:
        print("Sorry, your password is not accepted")
       
       
def not_allowed(password):
    notallowed = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]
    return password not in notallowed


while True:
    password = input("Enter your password: ")
    validity(password)
    x = input("Do you want to retry (yes/no): ")
    if x.lower() == "no":
        break
