def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    total_character = text.lower()
    char_count = {}

    for c in total_character:
        if c in char_count:
            char_count[c] += 1
        else: 
            char_count[c] = 1

    return char_count

def sort_on(d):
    return d["num"]

def sorted_dict(char_count):
    new_dict = []

    for char in char_count:
        new_dict.append({"char" : char, "num" : char_count[char]})
    
    new_dict.sort(reverse=True, key=sort_on)
    
    return new_dict




