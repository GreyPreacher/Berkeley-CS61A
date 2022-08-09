def total(str_list):
    sum = 0
    for i in str_list:
        sum += len(i)
    return sum

if __name__ == "__main__":
    str_list = ["hi", "heisman"]
    str_list2 = ['yo', 'hi', '']
    p = total(str_list2)
    print(p)
