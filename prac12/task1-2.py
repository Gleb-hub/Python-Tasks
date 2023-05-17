def find_word(string: str, word: str):
    """Find word index in string.
    
    Examples:
    >>> find_word('qwe qwe qwe', 'qwe')
    [0, 4, 8]
    >>> find_word('zxc qwe zxc', 'qwe')
    [4]
    >>> find_word('qw qw qwe', 'z')
    []
    
    """
    res = []
    index = string.find(word)
    while index != -1:
        res.append(index)
        index = string.find(word, index + 1)
    
    return res
