#user input n terms
terms = int(input("Type nth terms(Number) -: "))  

#series will start with 0 and 1 so first and second term assign in variable
first = 0
second = 1  

#check user input number is febonacci series work or not
if terms <= 1:
    print("More then 1 number allowed only")
else:
    #print first and second term
    print(first,second,end=" ")
    for x in range(2,terms):
        #make febonachi plus series
        next=first+second 
        #print start third term and will loop till nth term                          
        print(next,end=" ")
        #change first term to second term
        first=second
        #change second term into next term
        second=next