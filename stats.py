
def get_book_text(String):
    with open(String) as f:
        file_contents = f.read()
    return file_contents

def num_words(String):
    with open(String) as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)
    
def unique_characters(String):
    with open(String) as f:
        file_contents = f.read()
    lowered=file_contents.lower()
    stripped=lowered.replace(" ", "")
    
    unique_characters={

    }
    for char in stripped:
        if unique_characters.__contains__(char):
            unique_characters[char]+=1
        else:
            unique_characters[char]=1
    return unique_characters

def sorted_list(Dict):
    sorted_dict=sorted(Dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict
