import re
import tkinter as tk

def highlight_duplicates(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Use regular expressions to find duplicate words
    word_list = re.findall(r'\b\w+\b', text)
    word_count = {}
    duplicates = set()

    for word in word_list:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
            duplicates.add(word)
        else:
            word_count[word] = 1

    # Create a GUI window to display the highlighted text
    window = tk.Tk()
    text_widget = tk.Text(window)
    text_widget.pack()

    start = 1.0
    for word in word_list:
        if word.lower() in duplicates:
            text_widget.insert(start, word + ' ', 'highlighted')
        else:
            text_widget.insert(start, word + ' ')
        start = text_widget.index('end')

    text_widget.tag_config('highlighted', background='yellow')

    window.mainloop()

# Replace 'your_file.txt' with the path to your text file
highlight_duplicates('your_file.txt')