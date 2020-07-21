# def consecutive_combo(lst1, lst2):

#     lst3 = lst1 + lst2
#     lst3.sort()

#     consecutive = True

#     for i in range(len(lst3) - 1):
#         if lst3[i+1] != lst3[i] + 1:
#             consecutive = False
#     return consecutive


# print(consecutive_combo([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))

# def bonus(days):
#     bonus = 0
#     days = days - 32

#     for day in range(days + 1):
#         if day >= 1 and day <= 8:
#             bonus += 325
#         elif day >= 9 and day <= 16:
#             bonus += 550
#         elif day >= 17:
#             bonus += 600
#     return bonus


# print(bonus(50))


char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def encode_morse(message):
    encoded = ''
    for i in range(len(message)):
        if message[i] in char_to_dots or message[i].upper() in char_to_dots:
            if message[i].upper() in char_to_dots:
                encoded += (char_to_dots[message[i].upper()])
            elif message[i] in char_to_dots:
                encoded += char_to_dots[message[i]]
            if i != len(message) - 1:
                encoded += ' '
    # encoded += '|'
    # print(encoded)
    return encoded


encode_morse('Hello world, this is a test! 333')
