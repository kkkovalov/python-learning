def count_vowels(word: str):
    """
    Given a single word, returns a total count of vowels in that word
    
    :param word: str
    :return: int
    
    >>> count_vowels('Camila')
    3
    >>> count_vowels('Llrt')
    0
    >>> count_vowels('Aora')
    3
    
    """
    from re import search as regex
    total_count = len([x for x in str(word).lower() if regex("[aeuio]", x)])
    return total_count

# print(count_vowels('aeyuio'))

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    doctest.testfile("testdoc.txt")
