
openLibrary = ['(', '[', '{', '|']
closeLibrary = [')', ']', '}', '|']

correspondence = {
    '|': '|',
    ')': '(',
    ']': '[',
    '}': '{',
}


def balancedBrackets(string):
    stack = []
    hasBrackets = False

    if len(string) == 0 or len(string) == 1:
        return 0

    lineCount = 0
    for i in range(len(string)):
        # if string[i] not in correspondence.keys() and string[i] not in correspondence.values():
        #     continue
        # else:
        wasValue = False
        if string[i] in correspondence.values():
            hasBrackets = True

            if string[i] == '|':
                lineCount += 1
                # print('Linecount % 2', lineCount % 2)
                if lineCount % 2 != 0:
                    stack.append(string[i])
                    wasValue = True
                    # i += 1
            else:
                stack.append(string[i])

        if string[i] in correspondence.keys() and wasValue == False:
            hasBrackets = True
            # toMatch = stack.pop()
            if stack.pop() != correspondence[string[i]]:
                # stack.pop()
                return 0

    if hasBrackets == False:
        return 1

    # print('Got here brh')
    if len(stack) == 0:
        return 1
    else:
        return 0


print(balancedBrackets(
    "testing(||||)"))
# listy = [1, 2, 3]
# if listy[len(listy) - 1] == 3:
#     print('yo')

# print('listry', listy)
# openParenCount = 0
# closeParenCount = 0

# openSquareCount = 0
# closeSquareCount = 0

# openCurlyCount = 0
# closeCurlyCount = 0

# lineCount = 0

# for i in range(len(string)):
#     if string[i] == '(':
#         openParenCount += 1
#     elif string[i] == ')':
#         closeParenCount += 1
#     elif string[i] == '[':
#         openSquareCount += 1
#     elif string[i] == ']':
#         closeSquareCount += 1
#     elif string[i] == '{':
#         openCurlyCount += 1
#     elif string[i] == '}':
#         closeCurlyCount += 1
#     elif string[i] == '|':
#         lineCount += 1
