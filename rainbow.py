import hashlib

def create_rainbow_table(file_name, hashing_algorithm):
    rainbow_table = []
    
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            hashed_value = hash_string(line, hashing_algorithm)
            rainbow_table.append(hashed_value)
    
    return rainbow_table

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

def save_rainbow_table(rainbow_table, file_name):
    with open(file_name, 'w') as file:
        for entry in rainbow_table:
            file.write(entry + '\n')

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
