
#variables
name="why" 
height=4.5
weight=50

# def
def abc(name, height1, weight2):
    test = weight2 / (height1 ** 2)
    
    if test < 25:
        return "skinny"
    else:
        return "overweight"
        
response = abc(name, height, weight)
test = weight / (height ** 2)


# message
print(response)
print(test)
