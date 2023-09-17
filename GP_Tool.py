import sympy
# ANSI escape codes for text colors
class TextColor:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

# Example usage
#print(TextColor.RED + "This text is red." + TextColor.RESET)
#print(TextColor.GREEN + "This text is green." + TextColor.RESET)

# Define the Gematria Primus Alphabet
alphabet = ["F", "U", "TH", "O", "R", "C", "G", "W", "H", "N", "I", "J", "EO", "P", "X", "S", "T", "B", "E", "M", "L",
            "ING", "OE", "D", "A", "AE", "Y", "IO", "EA"]

# Map first 29 primes to alphabet
prime_seq = list(sympy.primerange(2, 110))
prime_map = {}
for i, char in enumerate(alphabet):
    if i < len(prime_seq):
        prime_map[char] = prime_seq[i]
    else:
        prime_map[char] = 0

# Function to check which element is at which index
def index_to_char(index):
    if index == 0:
        return "EA"
    else:
        return alphabet[index - 1]

# Function to check prime value of a character
def char_to_prime(char):
    return prime_map[char]

# Function to count the number of elements in a list
def count_elements(char_list):
    count = sum(len(char) > 0 for char in char_list)
    print("There are", count, "elements in the input.")

# Function to remove non-alphabetic characters from a string
def string_cleaner(string):
    return ''.join(char for char in string if char.isalpha())

# Function for Rolling Key decryption
def rolling_key_decryption():
    alphabet_list = ["F", "U", "TH", "O", "R", "C", "G", "W", "H", "N", "I", "J", "EO", "P", "X", "S", "T", "B", "E", "M", "L", "ING", "OE", "D", "A", "AE", "Y", "IO", "EA"]

    index_dict = {char: index + 1 for index, char in enumerate(alphabet_list)}

    key_text = input("Enter the key text: ").replace(',', '').replace(' ', '').upper()
    encrypted_text = input("Enter the encrypted text: ").replace(',', '').replace(' ', '').upper()

    key_text = key_text.replace('V', 'U')  # Replace 'V' with 'U' in the key text
    key_length = len(key_text)
    encrypted_length = len(encrypted_text)

    decrypted_text_all = ""

    # Limit the number of iterations to the length of the encrypted message
    iterations = min(key_length, encrypted_length)

    for i in range(iterations):
        decrypted_text = []

        for j in range(encrypted_length):
            key_char = key_text[(j + i) % key_length]
            encrypted_char = encrypted_text[j]

            if encrypted_char not in alphabet_list:
                decrypted_text.append(encrypted_char)
            else:
                encrypted_index = index_dict[encrypted_char]
                key_index = index_dict[key_char]
                decrypted_index = (encrypted_index + key_index) % len(alphabet_list)
                decrypted_char = alphabet_list[decrypted_index - 1]
                decrypted_text.append(decrypted_char)

        iteration_num = str(i + 1).zfill(4)  # Ensure 4-digit iteration number
        result = ', '.join(decrypted_text)
        print(f"Iteration {iteration_num} : {result}")

        decrypted_text_all += result + "\n"

    export_option = input("Do you want to export all iterations to a file? (y/n) ")
    if export_option.lower() == "y":
        file_name = input("Enter the file name: ")
        try:
            with open(file_name, "w") as file:
                file.write(decrypted_text_all)
            print("All iterations exported to", file_name)
        except IOError:
            print("Error exporting iterations to a file.")

    print("Decryption complete.")

# Function to print the alphabet row with index numbers
def print_alphabet_row():
    first_line = "   ".join([f"[{char} - {index + 1}]" for index, char in enumerate(alphabet[:15])])
    second_line = "  ".join([f"[{char} - {index + 16}]" for index, char in enumerate(alphabet[15:])])
    print(TextColor.RED + first_line+ TextColor.RESET)
    print(TextColor.RED + second_line+ TextColor.RESET)

#print_alphabet_row()  # Print the alphabet row with index numbers

# Main program loop
while True:
    print_alphabet_row()
    print(TextColor.CYAN + "\nWraith's Liber Primus Tool" + TextColor.RESET)
    print(TextColor.GREEN + "\nMain Menu:" + TextColor.RESET)
    print("[1] Key Shift")
    print("[2] Prime Values")
    print("[3] Count Elements")
    print("[4] String Cleaner")
    print("[5] Rolling Key")
    print("[6] Quit\n")

    option = input("Enter the option number: ")

    if option == "1" or option == "character index":
        chars = input("Enter a string to be shifted. (separated by commas): ").replace(" ", "").lower().split(',')
        shifts = input("Enter a shift sequence (characters or numbers, separated by commas): ").replace(" ", "").split(',')

        # Convert shift sequence to a list of integers
        shift_seq = []
        for char in shifts:
            try:
                shift_seq.append(int(char) % 29)
            except ValueError:
                try:
                    shift_seq.append((alphabet.index(char.upper()) + 1) % 29)
                except ValueError:
                    print(f"Invalid shift value: {char}")
                    continue

        print(f"chars: {chars}")
        print(f"shift_seq: {shift_seq}")

        results = []
        for i, char in enumerate(chars):
            char_index = alphabet.index(char.upper()) + 1
            shift = shift_seq[i]
            if shift < 0:
                shift = int(shift)
                shift += 29
            shifted_index = (char_index + shift) % 29
            results.append(str(shifted_index + 0))

        print(f"results: {', '.join([index_to_char(int(r) - 0) for r in results])}")

    elif option == "2":
        chars = input("Enter one or more characters to check (separated by commas): ").split(",")
        chars = [char.strip() for char in chars]
        shift = input("Enter a shift value: ")
        try:
            shift_value = int(shift) % 29
            shift_seq = [shift_value] * len(chars)
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        pre_sum = 0
        post_sum = 0

        for i in range(len(chars)):
            try:
                pre_prime = prime_map[chars[i].upper()]
                shifted_prime = pre_prime + int(shift_seq[i])
                pre_sum += pre_prime
                post_sum += shifted_prime
                print(f"Character: {chars[i]}, Prime: {pre_prime}, Shifted Prime: {shifted_prime}")
            except (KeyError, ValueError):
                print(f"Invalid character or shift sequence: {chars[i]}")

        print("Sum of pre-shifted primes:", pre_sum)
        print("Sum of post-shifted primes:", post_sum)

    elif option == "3":
        chars = input("Enter one or more characters to check (separated by commas): ").split(",")
        chars = [char.strip() for char in chars]
        count_elements(chars)
    elif option == "4":
        string = input("Enter a string: ")
        cleaned_string = string_cleaner(string)
        print("Cleaned String:", cleaned_string)
    elif option == "5":
        rolling_key_decryption()
    elif option == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option.")
    run_again = input("Return to menu? (y/n) ")
    if run_again.lower() != 'y':
        break
