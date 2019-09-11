def binaryAdd(a, u):
    """
    INPUT: a, u strings of 0's and 1's which are the binary reps of a and u
    OUTPUT: string representation of the binary sum
    """
    
    first_char_a = a[len(a)-1]    #this returns the last character of the string a
    first_char_u = u[len(u)-1]    #this returns the last character of the string u
    
    longest = 0
    if len(a) >= len(u):
        longest = len(a)
    else:
        longest = len(u)
    
    x = int(first_char_a)  #converts from string type to integer type
    y = int(first_char_u)  #converts from string type to integer type
    
    binSum = ""
    c = 0 #carry
    currSum = 0
    i = 0
    while i < longest + 1:
        if i > len (a)-1:
            x = 0
        else:
            char_a = a[len(a)-1-i]
            x = int(char_a)
            
        if i > len(u)-1:
            y = 0
        else:
            char_u = u[len(u)-1-i]
            y = int(char_u) 
            
        currSum = x + y + c
        if currSum > 1:
            c = 1
            currSum = 0
        else:
            c = 0
        binSum = str(currSum) + binSum
        i = i + 1
    if binSum[0] == '0':
        binSum = binSum[1:]
    print("Sum: ", binSum)
