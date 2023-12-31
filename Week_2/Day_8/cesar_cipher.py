#Alphabet Len = 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#User action, if he wants to encrypt or decrypt
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

#User Message
text = input("Type your message:\n").lower()

#The increases
shift = int(input("Type the shift number:\n"))



def encrypt(plain_text, shift_amount):
    
    #Transforming text in a list, so it get easier to work with also getting the len of this list so we can use a loop
    list_text = list(plain_text)
    len_list_text = len(list_text)

    #For to iterate each letter in the list!
    for i in range(0, len_list_text):
        
        #Getting the specific letter for the iteration
        letter = list_text[i]
        
        #If theres a space in the user input this part serve to get the space into the answers without having a problem
        #since we're checking the alphabet list and theres no space there
        if letter == " ":
            list_text[i] = " "
            continue
        
        #Getting the index where the specific letter is in the alphabet list
        index = alphabet.index(letter)
        
        #We need this part cause if the user chosen shift surpass the alphabet index there's no problem with it. 
        #This servers to keep counting even in this situation!
        if index + shift_amount >=26:
            spare = index + shift_amount
            spare = spare - 26
            list_text[i] = alphabet[spare]
        else:
            index += shift_amount
            list_text[i] = alphabet[index]

    #Transforming it back into a string!
    print("".join(list_text))
    print(list_text)

def decrypt(plain_text, shift_amount):

    #Transforming text in a list, so it get easier to work with also getting the len of this list so we can use a loop
    list_text = list(plain_text)
    len_list_text = len(list_text)
    
    #For to iterate each letter in the list!
    for i in range(0, len_list_text):
        
        #Getting the specific letter for the iteration
        letter = list_text[i]
        
        #If theres a space in the user input this part serve to get the space into the answers without having a problem
        #since we're checking the alphabet list and theres no space there
        if letter == " ":
            list_text[i] = " "
            continue

        #Getting the index where the specific letter is in the alphabet list
        index = alphabet.index(letter)

        #We need this part cause if the user chosen shift surpass the alphabet index there's no problem with it. 
        #This servers to keep counting even in this situation!
        if index + shift_amount >=26 or index < 0:
            spare = index + shift_amount
            spare = spare - 26
            list_text[i] = alphabet[spare]
        else:
            index -= shift_amount
            list_text[i] = alphabet[index]
      
    #Transforming it back into a string!
    print("".join(list_text))
    print(list_text)

if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)

if direction == "decode":
    decrypt(plain_text = text, shift_amount = shift)
