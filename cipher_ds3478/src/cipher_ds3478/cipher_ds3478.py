def cipher(text:str, shift:int, encrypt:bool = True) -> str:
    """
    Encrypts or decrypts supplied text. Each letter is replaced by a letter
    some fixed number of positions down the alphabet. Apparently, Julius Caesar
    used it in his private correspondence.
    
    Parameters
    ----------
    text: str
        the string to be encrypted or decrypted
    shift: int
        parameterizes the encryption / decryption
    encrypt: bool, optional
        if true then encrypt; otherwise descrypt. Default value is True

    Returns
    -------
    str
        a string that is encrypted or decrypted
        
    Raises
    ------
    TypeError
        when 'shift' parameter is not an int
        
    Examples
    --------
    >>> from qmsspkg_DS import qmsspkg_DS
    >>> cipher(text = 'absent', shift = 1, encrypt = True)
    bctfou
    >>> cipher(text = 'absent', shift = 10, encrypt = True)
    klCoxD
    >>> cipher(text = 'klCoxD', shift = 10, encrypt = False)
    absent
    """
    # https://docs.python.org/3/library/exceptions.html#TypeError
    if not type(shift) is int:
        raise TypeError('expected type of int for ''shift'' parameter')

        
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
