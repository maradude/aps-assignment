def get_range(arr, lbound, ubound):
    return (element for element in arr if lbound <= element <= ubound)


def main():
    for lower, upper in test_object.ranges:
        result = get_range(test_object.elements, lower, upper)
        print(' '.join(map(str, result)))


if __name__ == '__main__':
    from sanitize_input import get_input
    test_object = get_input()
    main()
