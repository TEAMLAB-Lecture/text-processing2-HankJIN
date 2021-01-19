#######################
# Test Processing II  #
#######################
import re


def digits_to_words(input_string):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    #temp = re.findall("[0-9]", input_string)
    digit_string = ' '.join(map(lambda item: number[int(item)], re.findall("[0-9]", input_string)))
    return digit_string


def to_camel_case(underscore_str):
    if underscore_str.find('_') == -1:
        return underscore_str

    temp = underscore_str.split('_')

    for idx, val in enumerate(temp):
        temp[idx] = val.capitalize()

    if len(''.join(temp)) == 0:
        return ''

    camelcase_str = ''.join(temp)[0].lower() + ''.join(temp)[1:]
#    camelcase_str[0] = camelcase_str[0].lower()
# 실패한이유정리하기
    return camelcase_str
