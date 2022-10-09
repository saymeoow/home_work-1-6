slovar = {'1': 'a',
          '2': 'b',
          '3': 'c',
          '4': 'd'}
new_slovar=dict( {val: key for key, val in slovar.items()})
assert new_slovar == {'a': '1',
                      'b': '2',
                      'c': '3',
                      'd': '4'}