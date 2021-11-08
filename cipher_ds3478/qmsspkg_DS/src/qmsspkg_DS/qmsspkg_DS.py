def cipher(text:str, shift:int, encrypt:bool = True) -> str:
    '''
    '''
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
