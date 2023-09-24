def file_info(file_way: str):
    """
    Function to demonstrate testing
    >>> way_file = '/Users/timuribatulin/Downloads/images.png'
    >>> print(file_info(way_file))
    ('/Users/timuribatulin/Downloads/images.png', 'images.png', 'png')
    """
    *_, file_name = file_way.split('/')
    *_, file_tape = file_name.split('.') 
    return (file_way, file_name, file_tape)



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)