from stats import word_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    # print(text)
    print(f"--- Begin report of {sys.argv[1]} ---")
    print(f"{word_count(text)} words found in the document")
    char_counts = get_char_counts(text)
    sortable_char_counts = []
    for char in char_counts:
        if char.isalpha():
            sortable_char_counts.append({"name": char, "num": char_counts[char]})

    sortable_char_counts.sort(reverse=True, key=sort_on)

    for char in sortable_char_counts:
        # print(f"The '{char["name"]}' character was found {char["num"]} times")
        print(f"{char["name"]}: {char["num"]}")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_counts(text):
    alphabet = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in alphabet:
            alphabet[char] = alphabet[char] + 1
        else:
            alphabet[char] = 1
    return alphabet

def sort_on(dict):
    return dict["num"]

main()