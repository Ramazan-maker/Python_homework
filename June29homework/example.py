def demonstrate_string_methods():
    # Example string
    my_string = "Hello, World!"

    # center()
    centered_string = my_string.center(20, '-')
    print("centered_string:", centered_string)

    # count()
    count_e = my_string.count('l')
    print("count_e:", count_e)

    # find()
    index_o = my_string.find('o')
    print("index_o:", index_o)

    # swapcase()
    swapped_string = my_string.swapcase()
    print("swapped_string:", swapped_string)

    # startswith() and endswith()
    starts_with_hello = my_string.startswith('Hello')
    print("starts_with_hello:", starts_with_hello)

    ends_with_world = my_string.endswith('World!')
    print("ends_with_world:", ends_with_world)

    # split()
    words = my_string.split(', ')
    print("words:", words)

    # capitalize()
    capitalized_string = my_string.capitalize()
    print("capitalized_string:", capitalized_string)

    # upper()
    uppercased_string = my_string.upper()
    print("uppercased_string:", uppercased_string)

    # title()
    title_string = my_string.title()
    print("title_string:", title_string)

    # ljust() and rjust()
    left_justified = my_string.ljust(20, '-')
    print("left_justified:", left_justified)

    right_justified = my_string.rjust(20, '-')
    print("right_justified:", right_justified)

    # strip()
    stripped_string = "   Some text with spaces    "
    stripped_result = stripped_string.strip()
    print("stripped_result:", stripped_result)

    # zfill()
    number_string = "42"
    zfilled_string = number_string.zfill(6)
    print("zfilled_string:", zfilled_string)

if __name__ == "__main__":
    demonstrate_string_methods()