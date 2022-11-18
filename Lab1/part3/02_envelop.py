import doctest


def test(paper_x, paper_y):
    """
    >>> test(8, 9)
    No!
    >>> test(9, 9)
    No!
    >>> test(9, 8)
    No!
    >>> test(6, 8)
    Yes!
    >>> test(8, 6)
    Yes!
    >>> test(3, 4)
    Yes!
    >>> test(11, 9)
    No!
    >>> test(9, 11)
    No!
    """
    envelop_x, envelop_y = 10, 7
    if (paper_x < envelop_x) and (paper_y < envelop_y):
        print("Yes!")
    elif (paper_x < envelop_y) and (paper_y < envelop_x):
        print("Yes!")
    else:
        print("No!")


if __name__ == '__main__':
    doctest.testmod()
