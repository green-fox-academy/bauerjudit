def is_complete(numbers):
    try:
        if sorted(numbers) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    except TypeError:
        return False
    return True
