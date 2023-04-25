def example_func(pram1, pram2):
    '''ドキュメントの例
    Aegs:
        pram1(int): ~~~
        pram2(str): ~~~

    Returns:
        bool: ~~~
    '''
    print(pram1)
    print(pram2)
    return True

print(example_func.__doc__)