def replacing(list):
    for i in range(len(list)):
        if list[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            list[i] = ord(list[i]) - 55
    return list


def converting(number, base):
    list_number = list()
    list_number.extend(number)
    replacing(list_number)
    list_number = list_number[::-1]
    result = 0
    for i in range(len(list_number)):
        result += int(list_number[i]) * base ** i
    return result


num = input('Input your number to converting: \n')
base = int(input('Input base of your number system (2 = binary) \n'))
print(f'Your number in the decimal system: {converting(num, base)}')
