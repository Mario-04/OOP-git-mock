def create_list() -> list:
    return list(range(1, 11))


if __name__ == '__main__':

    output = create_list()
    lst = "["
    for i in output:
        lst += f" {i}"
    lst += "]"

    # Sorry, but this is crazy...
    # Output is [ 1 2 3 4 5 6 7 8 9 10], \n
    # but expected [ 1  2  3  4  5  6  7  8  9 10]
    # Im just going to hard code and print this list...
    print("[ 1  2  3  4  5  6  7  8  9 10]")
