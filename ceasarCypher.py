alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

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
    
    print(f"The Encrypted message is: {modified_text}")

# TODO - Decryption
def decrypt(encrypted_text):
    return 0


chars_text = list(text) # Transforming text into a list of characters
encrypt_prim(chars_text, shift) # My method
encrypt_adv(text, shift) # Angela's method