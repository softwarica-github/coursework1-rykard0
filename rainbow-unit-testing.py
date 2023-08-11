import hashlib
import unittest

def hash_string(string, hashing_algorithm):
    if hashing_algorithm == 1:
        return hashlib.md5(string.encode()).hexdigest()
    elif hashing_algorithm == 2:
        return hashlib.sha1(string.encode()).hexdigest()
    elif hashing_algorithm == 3:
        return hashlib.sha256(string.encode()).hexdigest()
    elif hashing_algorithm == 4:
        return hashlib.sha3_256(string.encode()).hexdigest()
    elif hashing_algorithm == 5:
        # bcrypt hashing implementation goes here
        return None
    elif hashing_algorithm == 6:
        # Argon2 hashing implementation goes here
        return None

def create_rainbow_table(file_name, hashing_algorithm):
    rainbow_table = []
    
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            hashed_value = hash_string(line, hashing_algorithm)
            rainbow_table.append(hashed_value)
    
    return rainbow_table

def save_rainbow_table(rainbow_table, file_name):
    with open(file_name, 'w') as file:
        for entry in rainbow_table:
            file.write(entry + '\n')

# Main logic moved to a separate function
def generate_rainbow_table():
    # Prompt the user for the file name
    file_name = input("Enter the name of the file (with extension): ")

    # Display the list of hashing algorithms
    print("Available Hashing Algorithms:")
    print("1. MD5 (Message Digest 5)")
    print("2. SHA-1 (Secure Hash Algorithm 1)")
    print("3. SHA-256 (Secure Hash Algorithm 256-bit)")
    print("4. SHA-3 (Secure Hash Algorithm 3)")
    print("5. bcrypt")
    print("6. Argon2")
    print("7. All")

    # Prompt the user to select a hashing algorithm or all algorithms
    hashing_algorithm = int(input("Enter the number corresponding to the hashing algorithm (1-7): "))
    if hashing_algorithm == 7:
        algorithms = [1, 2, 3, 4, 5, 6]
    else:
        algorithms = [hashing_algorithm]

    # Create the rainbow table
    rainbow_table = []
    for algorithm in algorithms:
        rainbow_table.extend(create_rainbow_table(file_name, algorithm))

    # Prompt the user for the file name to save the rainbow table
    rainbow_table_file_name = input("Enter the name of the rainbow table file (with extension): ")
    # Save the rainbow table to a file
    save_rainbow_table(rainbow_table, rainbow_table_file_name)
    print("Rainbow table has been created and saved successfully.")

# Unit tests
class TestHashString(unittest.TestCase):
    def test_hash_string_md5(self):
        string = "password"
        result = hash_string(string, 1)
        expected = hashlib.md5(string.encode()).hexdigest()
        self.assertEqual(result, expected)

    def test_hash_string_sha1(self):
        string = "password"
        result = hash_string(string, 2)
        expected = hashlib.sha1(string.encode()).hexdigest()
        self.assertEqual(result, expected)

    def test_hash_string_sha256(self):
        string = "password"
        result = hash_string(string, 3)
        expected = hashlib.sha256(string.encode()).hexdigest()
        self.assertEqual(result, expected)

    # Add more test cases for other hashing algorithms if needed

class TestCreateRainbowTable(unittest.TestCase):
    def test_create_rainbow_table(self):
        file_name = "test_file.txt"
        hashing_algorithm = 1

        # Create a temporary test file
        with open(file_name, 'w') as file:
            file.write("password1\n")
            file.write("password2\n")
            file.write("password3\n")

        result = create_rainbow_table(file_name, hashing_algorithm)
        expected = [hash_string("password1", 1), hash_string("password2", 1), hash_string("password3", 1)]
        self.assertEqual(result, expected)

        # Remove the temporary test file
        import os
        os.remove(file_name)

# Run the unit tests
if __name__ == "__main__":
    unittest.main()
