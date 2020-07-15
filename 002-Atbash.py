alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def atbash(txt):
    translator = {}
    for i in range(len(alphabet) // 2):
        translator[alphabet[i]] = alphabet[-i - 1]

    print(translator)


atbash('hey')
