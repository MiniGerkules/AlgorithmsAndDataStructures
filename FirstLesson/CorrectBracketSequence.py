from turtle import pos
from Stack import Stack


bracket = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
}


def checkBracketSeq(strToCheck: str) -> bool:
    stack = Stack()
    for char in strToCheck:
        if stack.back() != 'error':            
            if (char in bracket) and (stack.back() == bracket[char]):
                stack.pop()
                continue

        stack.push(char)

    return True if stack.back() == 'error' else False


def isInputCorrect(string: str, possible: list) -> bool:
    for char in string:
        if char not in possible:
            return False

    return True


def main():
    possible = list(zip(bracket.values(), bracket.keys()))
    possible = [val for tup in possible for val in tup]

    print(f'The program can process this parentheses:\n {possible}')
    sequence = input('Enter bracket sequence:\n')

    if not isInputCorrect(sequence, possible):
        print('Your input is incorrect!')
        return

    if checkBracketSeq(sequence):
        print('Right bracket sequence!')
    else:
        print('Wrong bracket sequence!')


if __name__ == '__main__':
    main()
