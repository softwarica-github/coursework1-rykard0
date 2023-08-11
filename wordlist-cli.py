import itertools

def generate_wordlist(words, numbers, symbols, pattern):
    combinations = itertools.product(words, numbers, symbols)
    wordlist = [''.join(combination) for combination in combinations]
    return wordlist

def prompt_user_input(message):
    user_input = input(message).strip().split(',')
    return [item.strip() for item in user_input]

# Prompt the user to enter words, numbers, and symbols
words = prompt_user_input("Enter words separated by commas: ")
numbers = prompt_user_input("Enter numbers separated by commas: ")
symbols = prompt_user_input("Enter symbols separated by commas: ")


filenames = input("Enter filename for wordlists: ").strip().split(',')
filenames = [filename.strip() for filename in filenames]

# Define the patterns
patterns = [
    "WNS", "WSN",
    "NWS", "NSW",
    "SNW", "SWN"
]

# Generate wordlists for each pattern and append to the specified files
for pattern in patterns:
    wordlist = generate_wordlist(words, numbers, symbols, pattern)
    
    for filename in filenames:
        with open(filename, 'a') as file:
            file.write('\n'.join(wordlist) + '\n')
    
    print(f"Custom wordlist for pattern '{pattern}' has been appended to the specified files.")

print("Wordlists have been updated with all patterns.")
