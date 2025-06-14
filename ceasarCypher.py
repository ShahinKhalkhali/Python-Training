alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

# TODO-1: Create function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs
# TODO-2: In encrypt() shift each letter forwards by a shift amount and print
# TODO-3: Call encrypt() and pass in the user inputs. You should be able to test the code and encrypt message
# TODO-4: What happens if you try to shift z by 9? Can you shift the code?

# Primitive encryption function (Longer)
def encrypt_prim(original_text, shift_amount):
    for i in range(len(original_text)):
        for j in range(len(alphabet)):
            if original_text[i].lower() == alphabet[j]:
                if (j + shift_amount) > 26:
                    shift_rem = shift_amount % 26
                    original_text[i] = alphabet[(j - 27) + shift_rem]
                    break
                original_text[i] = alphabet[j + shift_amount]
                break

    print("The Encrypted message is: " + display(original_text))

def display(modified_list):
    modified_text = ""
    for i in range(len(modified_list)):
        modified_text += str(modified_list[i])
    return modified_text

# Advanced encryption function (Shorter)
def encrypt_adv(original_text, shift_amount):
    modified_text = ""

    for i in original_text:                                 # i indexes along each character of original_text

        shifted_position = alphabet.index(i) + shift_amount # i will be equal to the indexed character and 
                                                            # alphabet.index(i) will look for the letter
                                                            # associated to i then shift by shift_amount
        
        shifted_position = shifted_position % len(alphabet) # Assures that the index is within bounds of  
                                                            # alphabet's list

        modified_text += alphabet[shifted_position]         # Constructs string
    
    print(f"The encrypted message is: {modified_text}")

# TODO-1: Create a function called decrypt() that takes original_text and shift_amount as 2 inputs
# TODO-2: Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text
# TODO-3:   1) Combine the encrypt() and decrypt() functions into a single function called caesar()
#           2) Use the value of the user chosen direction variable to determine which functionality to use
#           3) Call the caesar function instead of encrypt/decrypt and pass in all three variables (ie: direction/text/shift)

def decrypt(original_text, shift_amount):
    modified_text = ""

    for i in original_text:
        shifted_position = alphabet.index(i) - shift_amount
        shifted_position = shifted_position % len(alphabet)
        modified_text += alphabet[shifted_position]

    print(f"The decrypted message is: {modified_text}")

def caesar(direction, original_text, shift_amount):
    if direction.lower() == "encrypt":
        encrypt_adv(original_text, shift_amount)
    elif direction.lower() == "decrypt":
        decrypt(original_text, shift_amount)
    else:
        direction = input("Please choose to either 'Encrypt' or 'Decrypt': ")
        caesar(direction, original_text, shift_amount)

chars_text = list(text) # Transforming text into a list of characters

caesar(direction, text, shift)