# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# method with if else statement
def test(num):
    if num >= 2:
        print('number entered is greater than or equal to 2')
    else:
        print('number entered is less than 2')


# set up variable and execute method
age = 3
test(age)


# method using return method
def helper(gender):
    if gender == "male":
        return "Helper is a man"
    if gender == "female":
        return "Helper is a female"
    return "Helper is other"


# print method value
print(helper('mother'))


# method using if else
def dif_test(x):
    if x == 0:
        print('value is zero')
    elif x > -10:
        print('value is greater than -10')


# print method value
dif_test(0)


# method with no parameters
def what():
    print("hi")


# print method value
what()

# examples of establishing and converting variables
sample = "danielle"
print(sample)
# printing value of string at a certain index
print(sample[0])
sample = 45
print(sample)

# switch statement
calling = "feather"
match calling:
    case "hi":
        print("hi is the calling")
    case "random":
        print("random is the calling")
    case _:
        print("other is the calling")

# loop a string
for item in calling:
    if item == "e":
        print("e is here")
    else:
        print("other letter")

# length of string
print(len(calling))

# is value present or not in string
print(calling)
print("r" in calling)
print("r" not in calling)

cast_test = str('danielle')
print(cast_test)
cast_test = 4
print(cast_test)


        test.assert_equals(commas(1), "1")
        test.assert_equals(commas(1000), "1,000")
        test.assert_equals(commas(100.2346), "100.235")
        test.assert_equals(commas(1000000000.23), "1,000,000,000.23")
        test.assert_equals(commas(9123.212), "9,123.212")
        test.assert_equals(commas(-1), "-1")
        test.assert_equals(commas(-1000000.123), "-1,000,000.123")
        test.assert_equals(commas(-2000.0), "-2,000")
        test.assert_equals(commas(-999.9999), "-1,000")
        test.assert_equals(commas(-1234567.0001236), "-1,234,567")
"""

def commas(num):
    no_decimal = str(num)
    decimal = ""
    negative = False
    if '.' in no_decimal:
        decimal = no_decimal[no_decimal.index('.') : len(no_decimal)]
        no_decimal = no_decimal[0 : no_decimal.index('.')]
        if decimal[1] == '0':
            decimal = ""
        if no_decimal[0] == '-':
            no_decimal = no_decimal[1 : len(no_decimal)]
            negative = True
        if len(decimal) > 4:
            core = decimal[0 : 3]
            if int(decimal[4]) >= 5:
                core += str(int(decimal[3]) + 1)
            else:
                core += decimal[4]
            decimal = core
    if len(no_decimal) > 3:
        rev = no_decimal[::-1]
        temp = ""
        count = 1
        for x in rev:
            temp += x
            if count % 3 == 0:
                temp += ','
            count += 1
        no_decimal = temp[::-1]
    if negative:
        no_decimal = '-' + no_decimal
    if len(decimal) > 0:
        return no_decimal + decimal
    return no_decimal


def luck_check(string):
    if any(x.isalpha() for x in string):
        return False
    left = ""
    right = ""
    import math
    mid = math.floor(len(string) / 2)
    left = string[0: mid]
    if len(string) % 2 == 0:
        right = string[mid: len(string)]
    else:
        right = string[mid + 1: len(string)]

    num_left = 0
    for x in left:
        num_left = num_left + int(x)
    num_right = 0
    for x in right:
        num_right = num_right + int(x)

    if num_left == num_right:
        return True
    return False


def mix_words(string):
    space = string.split()
    random = ""
    for x in space:
        if len(x) < 4:
            random += x + " "
        else:
            from random import shuffle
            first = x[0]
            last = x[len(x) - 1]
            middle = x[1:]
            if last.isalnum():
                middle = middle[:-1]
                temp = list(middle)
                shuffle(temp)
                middle = ''.join(temp)
            else:
                last = ""
                temp = middle[::-1]
                for x in temp:
                    if x.isalnum():
                        break
                    else:
                        last += x
                        middle = middle[:-1]
                if len(last) + len(middle) > 3:
                    last += middle[len(middle) - 1]
                    middle = middle[:-1]
                    temp = list(middle)
                    shuffle(temp)
                    middle = ''.join(temp)
                last = last[::-1]
            random += first + middle + last + " "
    return random[:-1]

def decoder(encoded, marker):
    forward = ""
    backward = ""
    final = ""
    replaced = encoded.replace(marker, '@')
    print(replaced)
    flip = False
    for x in replaced:
        if x == '@':
            if flip:
                flip = False
                if len(backward) > 0:
                    final += backward[::-1]
                    backward = ""
            else:
                flip = True
                if len(forward) > 0:
                    final += forward
                    forward = ""
        else:
            if flip:
                backward += x
            else:
                forward += x
    if len(forward) > 0:
        final += forward
    if len(backward) > 0:
        final += backward[::-1]
    return final

def solve(input_string):
    split = input_string.split('\n')
    carries = ""
    for x in split:
        nums = x[::-1].split()
        counter = 0
        add = "0"
        if len(nums[0]) != len(nums[1]):
            zeros = ''.join('0' for z in range(abs(len(nums[0]) - len(nums[1]))))
            if len(nums[0]) > len(nums[1]):
                nums[1] = nums[1] + zeros
            else:
                nums[0] = nums[0] + zeros
        for i in range(len(nums[0])):
            if int(add) + int(nums[0][i]) + int(nums[1][i]) > 9:
                counter += 1
                add = "1"
            else:
                add = "0"
        if counter == 0:
            carries += "No carry operation\n"
        else:
            carries += str(counter) + " carry operations\n"
    return carries[:-1]


def segment_display(num):
    zero = ["  ###  ", " #   # ", " #   # ", " #   # ", "       ", " #   # ", " #   # ", " #   # ", "  ###  "]
    one = ["       ", "     # ", "     # ", "     # ", "       ", "     # ", "     # ", "     # ", "       "]
    two = ["  ###  ", "     # ", "     # ", "     # ", "  ###  ", " #     ", " #     ", " #     ", "  ###  "]
    three = ["  ###  ", "     # ", "     # ", "     # ", "  ###  ", "     # ", "     # ", "     # ", "  ###  "]
    four = ["       ", " #   # ", " #   # ", " #   # ", "  ###  ", "     # ", "     # ", "     # ", "       "]
    five = ["  ###  ", " #     ", " #     ", " #     ", "  ###  ", "     # ", "     # ", "     # ", "  ###  "]
    six = ["  ###  ", " #     ", " #     ", " #     ", "  ###  ", " #   # ", " #   # ", " #   # ", "  ###  "]
    seven = ["  ###  ", "     # ", "     # ", "     # ", "       ", "     # ", "     # ", "     # ", "       "]
    eight = ["  ###  ", " #   # ", " #   # ", " #   # ", "  ###  ", " #   # ", " #   # ", " #   # ", "  ###  "]
    nine = ["  ###  ", " #   # ", " #   # ", " #   # ", "  ###  ", "     # ", "     # ", "     # ", "  ###  "]
    space = ["       ", "       ", "       ", "       ", "       ", "       ", "       ", "       ", "       "]

    number = str(num).rjust(6, ' ')
    display = ""
    for x in range(9):
        for y in number:
            if y == '0':
                display += '|' + zero[x]
            if y == '1':
                display += '|' + one[x]
            if y == '2':
                display += '|' + two[x]
            if y == '3':
                display += '|' + three[x]
            if y == '4':
                display += '|' + four[x]
            if y == '5':
                display += '|' + five[x]
            if y == '6':
                display += '|' + six[x]
            if y == '7':
                display += '|' + seven[x]
            if y == '8':
                display += '|' + eight[x]
            if y == '9':
                display += '|' + nine[x]
            if y == ' ':
                display += '|' + space[x]
        display += "|\n"
    return display


def phone_words(string_of_nums):
    if string_of_nums == "":
        return ""
    two = "abc"
    three = "def"
    four = "ghi"
    five = "jkl"
    six = "mno"
    seven = "pqrs"
    eight = "tuv"
    nine = "wxyz"
    count = 0
    current = ""
    word = ""
    for x in string_of_nums:
        if x == "0" or x == "1":
            if count > 0:
                if current == "2":
                    word += two[count - 1]
                if current == "3":
                    word += three[count - 1]
                if current == "4":
                    word += four[count - 1]
                if current == "5":
                    word += five[count - 1]
                if current == "6":
                    word += six[count - 1]
                if current == "7":
                    word += seven[count - 1]
                if current == "8":
                    word += eight[count - 1]
                if current == "9":
                    word += nine[count - 1]
            current = ""
            count = 0
            if x == "0":
                word += " "
            continue
        elif len(current) == 0:
            current = x
            count = 1
        elif x == current:
            count += 1
        elif x != current:
            if current == "2":
                word += two[count - 1]
            if current == "3":
                word += three[count - 1]
            if current == "4":
                word += four[count - 1]
            if current == "5":
                word += five[count - 1]
            if current == "6":
                word += six[count - 1]
            if current == "7":
                word += seven[count - 1]
            if current == "8":
                word += eight[count - 1]
            if current == "9":
                word += nine[count - 1]
            current = x
            count = 1
        if count >= 3:
            if count == 3 and current in "234568":
                if current == "2":
                    word += two[count - 1]
                if current == "3":
                    word += three[count - 1]
                if current == "4":
                    word += four[count - 1]
                if current == "5":
                    word += five[count - 1]
                if current == "6":
                    word += six[count - 1]
                if current == "8":
                    word += eight[count - 1]
                current = ""
                count = 0
            if count == 4 and current in "79":
                if current == "7":
                    word += seven[count - 1]
                if current == "9":
                    word += nine[count - 1]
                current = ""
                count = 0
    if count > 0:
        if current == "2":
            word += two[count - 1]
        if current == "3":
            word += three[count - 1]
        if current == "4":
            word += four[count - 1]
        if current == "5":
            word += five[count - 1]
        if current == "6":
            word += six[count - 1]
        if current == "7":
            word += seven[count - 1]
        if current == "8":
            word += eight[count - 1]
        if current == "9":
            word += nine[count - 1]
    return word


def name_in_str(str, name):
    remaining = str.lower()
    for x in range(len(name)):
        if name[x].lower() in remaining:
            remaining = remaining[remaining.index(name[x].lower()) + 1:]
        else:
            return False
    return True


def buy_tofu(cost, box):
    coin_list = box.split(' ')

    mon_1 = len([x for x in coin_list if x == 'mon'])
    monme_60 = len([x for x in coin_list if x == 'monme'])
    total = (mon_1 * 1) + (monme_60 * 60)

    amount = cost
    one = mon_1
    sixty = monme_60

    while amount > 0:
        if amount >= 60:
            if sixty > 0:
                sixty -= 1
                amount -= 60
            elif one > 0:
                one -= 1
                amount -= 1
            else:
                return 'leaving the market'
        else:
            if one > 0:
                one -= 1
                amount -= 1
            else:
                return 'leaving the market'

    return [mon_1, monme_60, total, (mon_1 - one) + (monme_60 - sixty)]


def unusual_sort(array):
    all_strings = [x for x in array if type(x) == str]
    letters = [x for x in all_strings if x.isalpha()]
    numbers = [x for x in array if type(x) != str]
    alpha_numbers = [x for x in all_strings if x.isnumeric()]
    combine = []
    if len(letters) > 0:
        letters.sort()
        combine += letters
    for x in range(10):
        if len(numbers) > 0:
            num_temp = [y for y in numbers if y == x]
            if len(num_temp) > 0:
                num_temp.sort()
                combine += num_temp
        if len(alpha_numbers) > 0:
            alpha_temp = [y for y in alpha_numbers if y == str(x)]
            if len(alpha_temp) > 0:
                alpha_temp.sort()
                combine += alpha_temp
    return combine


def string_expansion(s):
    if len([x for x in s if x.isalpha()]) > 0:
        if len([x for x in s if x.isnumeric()]) > 0:
            last_num = 1
            expand = ""
            for x in s:
                if x.isalpha():
                    for y in range(last_num):
                        expand += x
                else:
                    last_num = int(x)
            return expand
        else:
            return s
    return ""


print(string_expansion('3D2a5d2f'))
