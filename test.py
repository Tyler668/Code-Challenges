

def encrypt(word):
    vowelNum = {
        "a": "0",
        "e": "1",
        "o": "2",
        "u": "3"
    }

    word = word.lower()
    for c in range(len(word)):
        if vowelNum.__contains__(word[c]):
            word = word.replace(word[c], vowelNum[word[c]])

    rev = word[::-1]
    rev += 'aca'

    return(rev)


encrypt("Hello")
encrypt("Banana")
