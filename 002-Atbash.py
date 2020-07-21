

def atbash(txt):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    translator = {}
    for i in range(len(alphabet) // 2):
        translator[alphabet[i]] = alphabet[-i - 1]

    encoded = ''
    for i in txt:

        if i.lower() in translator.keys():
            if i.isupper():
                encoded += translator[i.lower()].upper()
            else:
                encoded += translator[i]
        elif i.lower() in translator.values():
            for key, value in translator.items():
                if i.lower() == value:
                    if i.isupper():
                        encoded += key.upper()
                    else:
                        encoded += key
        elif i not in translator.items():
            encoded += i

    return encoded


print(atbash(''))
