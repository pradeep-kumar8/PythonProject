#first we need to take input from user 
l = int(input("Length of Area : "))
w = int(input("Width of Area : "))

#make a function that calculate the area of length and width
def calculate_area(length, width):
    #check condition length and width equal or not
    if length == width:
        return "This is a square!"
    return length*width

#make this func as an object form and give parameter value that user give
area = calculate_area(l, w)
#print function that is an object form
print(area)
