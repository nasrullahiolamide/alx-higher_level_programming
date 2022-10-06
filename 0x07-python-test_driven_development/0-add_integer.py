# #!/usr/bin/python3
# """
# No module imported
# """


# def add_integer(a, b=98):
#     """
#     A funtion that adds two integers and return their sum
#     """
#     try:
#         assert isinstance(a, (int, float))
#     except BaseException:
#         raise TypeError("a must be an integer")
#     try:
#         assert isinstance(b, (int, float))
#     except BaseException:
#         raise TypeError("b must be an integer")
#     if type(a) == float:
#         a = int(a)
#     if type(b) == float:
#         b = int(b)
#     return a + b


#!/usr/bin/python3
"""
No module importation allowed for this task
"""


def add_integer(a, b=98):
    """
        Adds two integers
    """
    try:
        assert type(a) in (float, int)
    except BaseException:
        raise TypeError("a must be an integer")
    try:
        assert type(b) in (float, int)
    except BaseException:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
