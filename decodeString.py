# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid
# No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].


# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:

# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"


def doDecode(s):
    intStrings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    subs = []

    def decodeString(s: str) -> str:
        openCount = 0
        closeCount = 0
        openLocations = {}
        closeLocations = {}

        for i in range(len(s)):
            if s[i] == '[':
                openCount += 1
                openLocations[openCount] = i
                print('Open dict', openLocations)
            if s[i] == ']':
                closeCount += 1
                closeLocations[closeCount] = i
            if openCount == closeCount and openCount != 0:
                # print('o2', openLocations)
                subStr = s[openLocations[1]: closeLocations[openCount] + 1]
                print('Substr!!', subStr)
                subStr = subStr[1:len(subStr) - 1]

                subs.append(subStr)
                decodeString(subStr)
                # print('Fixed Substr', subStr)
                # decodeString(subStr)

    decodeString(s)
    subs.reverse()

    for i in range(len(subs)):
        subs[i] = '[' + subs[i] + ']'

    solution = ''
    # translations = {}

    # def translateSubstr(subStr):
    #     multiplierIndex = s.find(subStr) - 1
    #     print('MI', s[multiplierIndex])
    #     multBy = int(s[multiplierIndex])
    #     composition = multBy * (subStr)
    #     composition = composition.replace('[', '')
    #     composition = composition.replace(']', '')
    #     return composition

    # originalFinalSub = subs[len(subs)-1]
    # print(originalFinalSub)
    # OGmultiplierIndex = s[s.find(originalFinalSub) - 1]
    # print('og to translate', OGmultiplierIndex)
    # # print('Translated:', translateSubstr("[a2[c]]"))

    # # print('Translating:', translate("3[a2[c]]"))

    # for i in range(len(subs)):
    #     for j in subs:
    #         if j in subs[i] and j != subs[i]:
    #             # print('Trans j', translations[j])
    #             print('translatesubstr j', translateSubstr(j))
    #             subs[i] = subs[i].replace(j, translateSubstr(j))
    #             for num in intStrings:
    #                 if num in subs[i]:
    #                     # print('its in der')
    #                     subs[i] = subs[i].replace(num, '')
    #             print('sub i ', subs[i])

    # finalTranslation = int(OGmultiplierIndex) * subs[len(subs) - 1]
    # finalTranslation = finalTranslation.replace('[', '')
    # finalTranslation = finalTranslation.replace(']', '')
    # finalTranslation = translateSubstr(finalTranslation)
    # print('Final trans', finalTranslation)

    #     # translations[sub] = composition

    print('Subs', subs)
    print('Solution', solution)

    return finalTranslation


s = "4[3[a2[c]]]"


doDecode(s)


def decodeString2(s: str) -> str:
    intStrings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    print('S:', s)
    i = 0
    while i < len(s):
        if i+1 < len(s) - 1 and s[i+1] in intStrings:
            s = s[:i+1] + '+' + s[i+1:]
            i += 2
        elif i+1 < len(s) - 1 and s[i] == ']' and s[i+1] not in intStrings:
            s = s[:i+1] + '+' + s[i+1:]
            i += 2
        else:
            i += 1
    print('Pluses added:', s)

    s = s.replace('[', '')
    s = s.replace(']', '')

    s = s.split('+')
    result = ''
    for i in range(len(s)):
        if s[i][0] in intStrings:
            multiplier = int(s[i][0])
            s[i] = s[i][1:]
            result += multiplier * (s[i])
        else:
            result += s[i]
    print('Res', result)
    return result


s2 = "3[a]2[bc]"

print(decodeString2(s2))
