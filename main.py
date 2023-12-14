def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    

    character_collection = get_num_characters(text)

    sorted_list = list(character_collection.items())
    sorted_list = sorted(sorted_list, key=lambda x: x[1], reverse=True)

    for char in sorted_list:
        if char[0].isalpha():
            print(f"the '{char[0]}' character was found {char[1]} times")





def get_book_text(path):
    with open (path) as file:
        return file.read()
    
def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characters = {}
    for i in text.lower():
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters


main()