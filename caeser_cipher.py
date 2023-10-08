#This code takes in a text encrypted with caeser cipher and returns the decrypted text (most of the time)

#This dictionary containes relative frequency percentages of various alphabets in generic english texts
letter_frequencies = {
    'E': 13.00,
    'T': 9.10,
    'A': 8.12,
    'O': 7.68,
    'I': 7.31,
    'N': 6.95,
    'S': 6.28,
    'H': 6.09,
    'R': 5.98,
    'D': 4.25,
    'L': 4.03,
    'U': 2.76,
    'C': 2.50,
    'M': 2.23,
    'W': 2.09,
    'F': 2.03,
    'G': 1.82,
    'Y': 1.78,
    'P': 1.49,
    'B': 1.29,
    'V': 0.98,
    'K': 0.77,
    'J': 0.15,
    'X': 0.15,
    'Q': 0.10,
    'Z': 0.07
}




#Below function does the following. Given a string "s", how well does it's letter's frequencies match with the data listed above.
#This is achieved first relative frequencies of letters in the string "s"
#Next we compute how far it is from ideal frequency. Suppose letter 'X' has actual relative frequency 'a' and 'b' in the string 's'.
#Error contributed by this letter is (a-b)**2. Squaring is done make the error positive, so that it can accumulate (not cancel with other errors).
#We repeat this for all alphabets and add them all to get final net error.
#This is similar to variance
def error_value(string):
    n = len(string)
    freq = [0]*26
    for x in string:
        if(65 <= ord(x) <= 90):
            freq[ord(x)-65] += 1
        if(97 <= ord(x) <= 122):
            freq[ord(x)-97] += 1
    for i in range(26):
        freq[i] = freq[i]*(100/n)   #Done calculating relative frequencies

    error = 0
    for i in range(26):
        error += (freq[i]-letter_frequencies[chr(i+65)])**2 #Calculating error contribution by each alphaber.
    return error
    



#Getting the input from user through terminal, if you want you can just directly assign a string here.
input_string = input()



#"possibilities" hold all possilbe strings obtained from input by shifting the letters
possibilities = []
for i in range(26):
    new_string = ""
    for x in input_string:
        if(97 <= ord(x) <= 122):
            new_string += chr(97+((ord(x)-97+i)%26))
        elif(65 <= ord(x) <= 90):
            new_string += chr(65+(ord(x)-65+i)%26)
        else:
            new_string += x
    possibilities.append(new_string)    #Generated all the possible strings and stored them in "possibilites"



error_values = [error_value(x) for x in possibilities]  #Calculating error for each possibility
min_index = 0   #index of minimum error
for i in range(26):
    if(error_values[i] < error_values[min_index]):
        min_index = i



print(possibilities[min_index]) #printing the possiblity with minimum error



