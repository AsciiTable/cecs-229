#1
def modinv(a,m):
    """returns the inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: a inverse as an integer
    """
    modu = m
    x = 0
    y = 1
    u = 1
    v = 0
    swapped = False
    if a < m:
        swapped = True
        holder = a
        a = m
        m = holder
    
    while a != 0:
        quotient = m//a
        remainder = m%a
        o = x - u * quotient
        n = y - v * quotient
        m = a
        a = remainder
        x = u
        y = v
        u = o
        v = n

    if swapped == True:
        holder = x
        x = y
        y = holder
    
    while x <= 0:
        x = x + modu
    
    return x

#2
def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters 
    """
    # GCD CHECK
    i=1
    gcdAns = 0
    
    while(i < 26):
        if (a%i == 0) & (26%i == 0):
            gcdAns = i
        i += 1
    if gcdAns != 1:
        return "GCD(a, 26) != 1; CANNOT ENCRYPT"
    
    #Encryption
    #f(p) = ap + b mod(26)
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    k = len(text)
    i = 0
    enc = ""
    
    while i < k:
        ev = text[i].upper()
        index = 0
        while ev != alphabet[index]:
            if index > 25:
                break
            index += 1;
        index *= a
        index += b
        index = index%26
        ev = alphabet[index]
        enc += ev
        i+=1
    
    return enc
affineEncrypt("STOPWHATYOUREDOING", 15, 6) 

#3
def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    # GCD CHECK
    i=1
    gcdAns = 0
    
    while(i < 26):
        if (a%i == 0) & (26%i == 0):
            gcdAns = i
        i += 1
    if gcdAns != 1:
        return "GCD(a, 26) != 1; CANNOT DECRYPT"
    
    # Decryption
    #f^(-1)(p) = \Bar(a)(p - b) mod(26)
    
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    k = len(ciphertext)
    i = 0
    dec = ""
    inva = modinv(a,26)
    invb = b * inva
    while i < k:
        ev = ciphertext[i].upper()
        index = 0
        while ev != alphabet[index]:
            if index > 25:
                return "CANNOT DECRYPT NON-ALPHABET STRINGS"
            index += 1;
        index *= inva
        index -= invb
        index = index%26
        ev = alphabet[index]
        dec += ev
        i+=1
    
    return dec
affineDecrypt("QFIXYHGFCIUBOZIWTS", 15, 6) 

#4
def encryptRSA(m, p, q, e):
    """encrypts the plaintext m, using RSA and the key (p * q, e)
    INPUT:  m - plaintext as a string of letters
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    # PRIME CHECK
    i = 1
    while i < p:
        if i%p == 0:
            return "p is not prime; CANNOT ENCRYPT"
        i += 1
        
    i = 1
    while i < q:
        if i%q == 0:
            return "q is not prime; CANNOT ENCRYPT"
        i += 1
    
    # GCD CHECK
    check = (p-1)*(q-1)
    compTo = check
    if e > check:
        compTo = e
    i=1
    gcdAns = 0
    
    while(i < compTo):
        if (e%i == 0) & (check%i == 0):
            gcdAns = i
        i += 1
    if gcdAns != 1:
        return "GCD((p-1)*(q-1), e) != 1; CANNOT ENCRYPT"
    
    
    #ENCRYPTION 
    n = p*q
    size = 0
    twofive = 25
    while twofive < n:
        twofive *= 100
        twofive += 25
        size += 2
    
    blocks = len(m)//2
    if len(m)%2 != 0:
        blocks += 1
    
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    i=0
    enc = ""
    while i < blocks*2:
        if i > 1:
            enc += " "
        j = 0
        en = 0
        while j < (size//2):
            if j+i < len(m):
                ev = m[j+i].upper()
            else:
                ev = "X"
            index = 0
            while ev != alphabet[index]:
                if index > 25:
                    return "CANNOT ENCRYPT NON-ALPHABET STRINGS"
                index += 1
            en *= 100
            en += index
            j += 1
        en = en**e
        en = en%n
        enstr = str(en)
        while len(enstr) < 4:
            enstr = "0" + enstr
        enc += enstr
        i += 2
    
    return enc


#5
def decryptRSA(c, p, q, e):
    """decrypts the cipher c, which was encrypted using the key (p * q, e)
    INPUT:  c - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    c_copy = c.replace(" ", "")  #taking out all spacing
    m = (p-1)*(q-1)# <------------------------------------------------FIXME: Enter the appropriate modulo for calculating inverse of e
    e_inv = modinv(e, m)
    n = p*q# <------------------------------------------------FIXME: Enter the appropriate modulo for calculating decryption of each block
    
    
    digits = ""
    k = blocksize(n) #size of each block is calculated by function blocksize()
    start = 0
    for i in range(0,len(c_copy), k):
        block = c_copy[start: start + k]  #creating a block of digits
        cdec = int(block)
        cdec = (cdec**e_inv)%n
        digit = str(cdec) # <-----------------FIXME: Enter the appropriate calculation for the decryption of each block 
        if len(digit) % 2 != 0:  #padding the block before adding it to the string
            digits += "0" + digit
        else:
            digits += digit
        start += k  #updating starting index for next block
    return RSAdigits2letters(digits)  #converting digits to letters

#Tools
def RSAdigits2letters(digits):
    """converts a string of double digits without spaces in the range 00-25 to a string of letters A-Z"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digit2letter = dict((v,k) for k,v in letter2digit.items())  #creating a dictionary with keys and values exchanged
        
    letters = ""
    start = 0  #initializing starting index of first digit
    for i in range(0, len(digits), 2):
        digit = digits[start : start + 2]  # accessing the double digit
        letters += digit2letter[digit]     # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    
    return letters

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2