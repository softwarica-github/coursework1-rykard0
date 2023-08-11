import hashlib
import tkinter as tk
from tkinter import filedialog

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

def browse_input_file():
    file_name = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_name)

def browse_output_file():
    rainbow_table_file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(tk.END, rainbow_table_file_name)

def generate_rainbow_table():
    file_name = file_entry.get().strip()
    hashing_algorithm = int(algorithm_choice.get())
    if hashing_algorithm == 7:
        algorithms = [1, 2, 3, 4, 5, 6]
    else:
        algorithms = [hashing_algorithm]

    # Create the rainbow table
    rainbow_table = []
    for algorithm in algorithms:
        rainbow_table.extend(create_rainbow_table(file_name, algorithm))

    # Prompt the user for the file name to save the rainbow table
    rainbow_table_file_name = output_file_entry.get().strip()
    # Save the rainbow table to a file
    save_rainbow_table(rainbow_table, rainbow_table_file_name)
    result_label.config(text="Rainbow table has been created and saved successfully.", fg="green")

# Create the main window
root = tk.Tk()
root.title("Rainbow Table Generator")
root.geometry("600x250")
root.resizable(False, False)

# Create and configure frames
input_frame = tk.Frame(root, padx=20, pady=20)
output_frame = tk.Frame(root, padx=20, pady=10)
input_frame.pack(pady=10)
output_frame.pack(pady=10)

# Input elements
file_label = tk.Label(input_frame, text="Select the input file:")
file_entry = tk.Entry(input_frame, width=40)
browse_file_button = tk.Button(input_frame, text="Browse", command=browse_input_file)

algorithm_label = tk.Label(input_frame, text="Select the hashing algorithm:")
algorithm_choice = tk.StringVar()
algorithm_choices = ["MD5 (Message Digest 5)", "SHA-1 (Secure Hash Algorithm 1)", "SHA-256 (Secure Hash Algorithm 256-bit)",
                     "SHA-3 (Secure Hash Algorithm 3)", "bcrypt", "Argon2", "All"]
algorithm_choice.set(algorithm_choices[0])
algorithm_menu = tk.OptionMenu(input_frame, algorithm_choice, *algorithm_choices)

# Output element
output_file_label = tk.Label(output_frame, text="Select the output file:")
output_file_entry = tk.Entry(output_frame, width=40)
browse_output_file_button = tk.Button(output_frame, text="Browse", command=browse_output_file)

generate_button = tk.Button(root, text="Generate Rainbow Table", command=generate_rainbow_table)
save_button = tk.Button(root, text="Save Rainbow Table", command=lambda: save_rainbow_table([], "rainbow_table.txt"))

# Result element
result_label = tk.Label(root, text="", fg="green")

# Grid layout for input elements
file_label.grid(row=0, column=0, columnspan=2)
file_entry.grid(row=1, column=0, columnspan=2)
browse_file_button.grid(row=1, column=2)

algorithm_label.grid(row=2, column=0, columnspan=2)
algorithm_menu.grid(row=2, column=2)

# Grid layout for output elements
output_file_label.grid(row=0, column=0, columnspan=2)
output_file_entry.grid(row=1, column=0, columnspan=2)
browse_output_file_button.grid(row=1, column=2)

generate_button.pack(side=tk.LEFT, pady=10, padx=5)
save_button.pack(side=tk.LEFT, pady=10, padx=5)
result_label.pack()

# Run the GUI main loop
root.mainloop()
