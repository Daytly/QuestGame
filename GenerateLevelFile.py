import random

for i in range(100):
    file = open(f'map{i}.txt', 'w')
    _list = []
    for _ in range(10):
        _str = '#'
        for _ in range(random.randrange(5, 10)):
            _str += random.choice(['.', '#'])
        _str += '#\n'
        _list.append(list(_str))
    _list = [['#'] * len(_list[0])] + _list
    _list += [['#'] * len(_list[-1])]
    indY = random.randrange(1, 10)
    indX = random.randrange(1, len(_list[indY]))
    _list[indY][indX] = "@"
    file.writelines([''.join(i) for i in _list])
    file.close()
