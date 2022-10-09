list_with_int = [1, 2, 3, 4, 5]

list_with_str = list(map(lambda x:str(x), list_with_int))
assert list_with_str == ['1','2','3','4','5']
