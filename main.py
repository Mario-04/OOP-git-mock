def create_list() -> list:
    return list(range(1, 11))


if __name__ == '__main__':
    output = create_list()
    lst = "["
    for i in output:
        lst += f" {i}"
    lst += "]"
    print(lst)
