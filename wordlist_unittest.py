import itertools
import unittest

def generate_wordlist(words, numbers, symbols, pattern):
    combinations = itertools.product(words, numbers, symbols)
    wordlist = [''.join(combination) for combination in combinations]
    return wordlist

def prompt_user_input(message):
    user_input = input(message).strip().split(',')
    return [item.strip() for item in user_input]

def create_and_append_wordlists(words, numbers, symbols, filenames):
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

# Unit tests
class TestWordlistGenerator(unittest.TestCase):
    def test_generate_wordlist(self):
        words = ['apple', 'banana']
        numbers = ['123', '456']
        symbols = ['!', '@']
        pattern = "WNS"

        result = generate_wordlist(words, numbers, symbols, pattern)
        expected = ['apple123!', 'apple123@', 'apple456!', 'apple456@', 'banana123!', 'banana123@', 'banana456!', 'banana456@']
        self.assertEqual(result, expected)

    def test_prompt_user_input(self):
        # Simulate user input for the test
        def mock_input(message):
            if message == "Enter words separated by commas: ":
                return "apple, banana"
            elif message == "Enter numbers separated by commas: ":
                return "123, 456"
            elif message == "Enter symbols separated by commas: ":
                return "!, @"
            elif message == "Enter filename for wordlists: ":
                return "output.txt"
            else:
                return ""

        # Replace input() with the mock_input function during testing
        original_input = __builtins__.input
        __builtins__.input = mock_input

        # Test the function
        words = prompt_user_input("Enter words separated by commas: ")
        numbers = prompt_user_input("Enter numbers separated by commas: ")
        symbols = prompt_user_input("Enter symbols separated by commas: ")

        # Restore input() to its original function after testing
        __builtins__.input = original_input

        self.assertEqual(words, ['apple', 'banana'])
        self.assertEqual(numbers, ['123', '456'])
        self.assertEqual(symbols, ['!', '@'])

if __name__ == "__main__":
    unittest.main()
