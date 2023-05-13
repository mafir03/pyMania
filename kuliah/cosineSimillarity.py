def counting_array(array):
    dict_result = dict()
    for item in array:
        if item not in dict_result.keys():
            dict_result[item] = 1
        else:
            dict_result[item] += 1
    return dict_result


def combining_array(array_a, array_b):
    dict_result_a = counting_array(array_a)
    dict_result_b = counting_array(array_b)
    dict_result_b_alter = dict_result_b.copy()
    for key in dict_result_a.keys():
        if key not in dict_result_b:
            dict_result_b_alter[key] = 0

    for key in dict_result_b.keys():
        if key not in dict_result_a:
            dict_result_a[key] = 0

    return dict_result_a, dict_result_b_alter


def multipy_and_squared_part(dict_a, dict_b):
    # it's guaranteed for dict_a and dict_b to have equal length
    # and same sets of keys but different items
    top_part_of_equation = int()
    bottom_part_dict_a = int()
    bottom_part_dict_b = int()
    for keys in dict_a:
        top_part_of_equation += dict_a[keys] * dict_b[keys]
        bottom_part_dict_a += dict_a[keys]**2
        bottom_part_dict_b += dict_b[keys]**2

    return top_part_of_equation, bottom_part_dict_a * bottom_part_dict_b


def cosine_simillarity(a, b):
    top, bottom = multipy_and_squared_part(*combining_array(a, b))
    return top / bottom**(1/2)


def main():
    a = ['Julie', 'loves', 'me', 'more', 'than', 'Linda', 'loves', 'me']
    b = ['Jane', 'likes', 'me', 'more', 'than', 'Julie', 'loves', 'me']
    print(cosine_simillarity(a, b))


if __name__ == '__main__':
    main()