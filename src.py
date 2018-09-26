def append_letters(string_to_append, temp):
    assert string_to_append.islower(), "Characters must be all lowercase!"
    return temp + string_to_append


def delete_last_chars(del_range, temp):
    assert del_range <= len(temp)
    return temp[:len(temp) - del_range]


def print_chars(no_of_char, temp):
    assert 0 < no_of_char <= len(temp)
    print(temp[no_of_char-1])


ops = []
final_string = ""
temp_string = ""
previous_strings = []

no_of_ops = int(input())
assert 1 <= no_of_ops <= 10 ** 6

for i in range(no_of_ops):
    ops.append(list(input().rstrip().split()))

delete_sum = 0
append_sum = 0
undo_counter = 1

for k in range(no_of_ops):

    assert append_sum <= 10 ** 6
    assert delete_sum <= 2 * 10 ** 6
    assert ops[k][0] in ['1', '2', '3', '4'], 'Unknown operation!'

    if ops[k][0] == "1" or ops[k][0] == "2":
        previous_strings.append(final_string)

        if ops[k][0] == "1":
            temp_string = append_letters(ops[k][1], final_string)
            append_sum += len(ops[k][1])
        elif ops[k][0] == "2":
            temp_string = delete_last_chars(int(ops[k][1]), final_string)
            delete_sum += int(ops[k][1])

        final_string = temp_string

    elif ops[k][0] == "3":
        print_chars(int(ops[k][1]), final_string)

    elif ops[k][0] == "4":
        final_string = previous_strings[undo_counter * -1]
        undo_counter += 1
