def append_letters(string_to_append):
    print("APPEND")


def delete_last_chars(del_range):
    print("DELETE")


def print_chars(char_to_print):
    print("PRINT")


def undo():
    print("UNDO")


ops = []
theString = ""

no_of_ops = int(input())
assert 1 <= no_of_ops <= 10 ** 6

for i in range(no_of_ops):
    ops.append(list(input().rstrip().split()))

for k in range(no_of_ops):
    assert ops[k][0] in ['1', '2', '3', '4'], 'Unkown operation!'

    if ops[k][0] == "1":
        append_letters(ops[k][1])
    elif ops[k][0] == "2":
        delete_last_chars(ops[k][1])
    elif ops[k][0] == "3":
        print_chars(ops[k][1])
    elif ops[k][0] == "4":
        undo()
