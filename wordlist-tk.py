import itertools
import tkinter as tk
from tkinter import filedialog

def generate_wordlist(words, numbers, symbols, pattern):
    combinations = itertools.product(words, numbers, symbols)
    wordlist = [''.join(combination) for combination in combinations]
    return wordlist

def create_rainbow_table(words, numbers, symbols, filenames, patterns):
    for pattern in patterns:
        wordlist = generate_wordlist(words, numbers, symbols, pattern)
        for filename in filenames:
            with open(filename, 'a') as file:
                file.write('\n'.join(wordlist) + '\n')

def browse_files():
    file_names = filedialog.askopenfilenames()
    file_list.delete(0, tk.END)
    for file_name in file_names:
        file_list.insert(tk.END, file_name)

def generate_wordlists():
    words = word_entry.get().strip().split(',')
    numbers = number_entry.get().strip().split(',')
    symbols = symbol_entry.get().strip().split(',')
    filenames = file_list.get(0, tk.END)
    patterns = [
        "WNS", "WSN",
        "NWS", "NSW",
        "SNW", "SWN"
    ]
    create_rainbow_table(words, numbers, symbols, filenames, patterns)
    result_label.config(text="Wordlists have been updated with all patterns.", fg="green")

# Create the main window
root = tk.Tk()
root.title("Rainbow Table Generator")
root.geometry("600x650")
root.resizable(False, False)

# Create and configure frames
input_frame = tk.Frame(root, padx=20, pady=20)
output_frame = tk.Frame(root, padx=20, pady=10)
input_frame.pack(pady=20)
output_frame.pack(pady=10)

# Input elements
word_label = tk.Label(input_frame, text="Enter words separated by commas:")
word_entry = tk.Entry(input_frame, width=40)
number_label = tk.Label(input_frame, text="Enter numbers separated by commas:")
number_entry = tk.Entry(input_frame, width=40)
symbol_label = tk.Label(input_frame, text="Enter symbols separated by commas:")
symbol_entry = tk.Entry(input_frame, width=40)
file_list_label = tk.Label(input_frame, text="Selected Files:")
file_list = tk.Listbox(input_frame, selectmode=tk.MULTIPLE, width=45)
browse_button = tk.Button(input_frame, text="Browse", command=browse_files)
generate_button = tk.Button(input_frame, text="Generate Wordlists", command=generate_wordlists)

# Output element
result_label = tk.Label(output_frame, text="", fg="green")

# Grid layout for input elements
word_label.grid(row=0, column=0, columnspan=2)
word_entry.grid(row=1, column=0, columnspan=2)
number_label.grid(row=2, column=0, columnspan=2)
number_entry.grid(row=3, column=0, columnspan=2)
symbol_label.grid(row=4, column=0, columnspan=2)
symbol_entry.grid(row=5, column=0, columnspan=2)
file_list_label.grid(row=6, column=0, columnspan=2)
file_list.grid(row=7, column=0, columnspan=2)
browse_button.grid(row=8, column=0)
generate_button.grid(row=8, column=1)

# Pack the output element
result_label.pack()

# Run the GUI main loop
root.mainloop()
