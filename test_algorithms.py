import import_ipynb
import algorithms as algs


def return_sort_array(function_sort, array, *args):
    array_for_sort = array.copy()
    function_sort(array_for_sort, *args)
    return array_for_sort


def test_sorts():
    functions_sort = (
        algs.choice_sort,
        algs.insert_sort,
        algs.bubble_sort,
        algs.merge_sort,
    )

    for function in functions_sort:
        assert return_sort_array(function,
                                 [5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert return_sort_array(function,
                                 [5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
        assert return_sort_array(function, [1]) == [1]
        assert return_sort_array(function, []) == []


def test_count_sort():
    assert return_sort_array(algs.count_sort, [5, 4, 3, 2, 1],
                             [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert return_sort_array(algs.count_sort, [], [1, 2, 3, 4, 5]) == []
    assert return_sort_array(algs.count_sort, [3, 4, 1],
                             [1, 2, 3, 4, 5]) == [1, 3, 4]
    assert return_sort_array(algs.count_sort,
                             [5]*10 + [3]*5 + [9]*9 + [1]*3 + [5]*3,
                             [1, 3, 5, 9]) == ([1]*3 + [3]*5 + [5]*13
                                               + [9]*9)
