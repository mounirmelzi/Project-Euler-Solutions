
def main():
    somme = 0
    for i in range(1, 1001):
        somme += number_letter_count(i)
    print(somme)


NUMBERS_LETTERS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'onehundred',
    1000: 'onethousand',
}



def number_letter_count(num: int) -> int :
    global NUMBERS_LETTERS
    if num in NUMBERS_LETTERS:
        return len(NUMBERS_LETTERS[num])

    number = str(num)
    hundreds, tens, ones = '', '', ''

    for i in range (len(number)):
        digit = int(number[i])
        if digit == 0:
            continue

        if len(number) - i == 3: # hundreds
            hundreds = NUMBERS_LETTERS[digit] + ' hundred and '
        elif len(number) - i == 2: # tens
            if digit != 1:
                tens = NUMBERS_LETTERS[digit * 10] 
            else:
                tens = NUMBERS_LETTERS[digit * 10 + int(number[i+1])]
                break
        elif len(number) - i == 1: # ones
            ones = NUMBERS_LETTERS[digit]

    word = hundreds + tens + ones
    if word[-4:] == 'and ':
        word = word[:-4]
    return len(word) - word.count(' ')
        



if __name__ == '__main__':
    main()
