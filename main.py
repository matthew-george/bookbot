def main():
    text = get_book_text("books/frankenstein.txt")
    # print(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document")
    char_counts = get_char_counts(text)
    sortable_char_counts = []
    for char in char_counts:
        if char.isalpha():
            sortable_char_counts.append({"name": char, "num": char_counts[char]})

    sortable_char_counts.sort(reverse=True, key=sort_on)

    for char in sortable_char_counts:
        print(f"The '{char["name"]}' character was found {char["num"]} times")
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

def word_count(text):
    words = text.split()
    count = len(words)
    return count

def sort_on(dict):
    return dict["num"]

main()