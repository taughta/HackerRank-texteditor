def append_letters(string_to_append, temp):
    assert string_to_append.islower(), "Characters must be all lowercase!"
    print(temp + string_to_append)
    return temp + string_to_append


def delete_last_chars(del_range, temp):
    assert del_range <= len(temp)
    print(temp[:len(temp) - del_range])
    return temp[:len(temp) - del_range]


def print_chars(no_of_char, temp):
    assert 0 < no_of_char <= len(temp)
    print(temp[no_of_char-1])


ops = []
final_string = ""
temp_string = ""

no_of_ops = int(input())
assert 1 <= no_of_ops <= 10 ** 6

for i in range(no_of_ops):
    ops.append(list(input().rstrip().split()))

delete_sum = 0
append_sum = 0

for k in range(no_of_ops):

    if ops[k][0] != "4" and k > 0:
        final_string = temp_string
    elif ops[k][0] == "4" and k > 0:
        temp_string = final_string

    assert append_sum <= 10**6
    assert delete_sum <= 2*10**6
    assert ops[k][0] in ['1', '2', '3', '4'], 'Unknown operation!'

    if ops[k][0] == "1":
        temp_string = append_letters(ops[k][1], final_string)
    elif ops[k][0] == "2":
        temp_string = delete_last_chars(int(ops[k][1]), final_string)
    elif ops[k][0] == "3":
        print_chars(int(ops[k][1]), final_string)
