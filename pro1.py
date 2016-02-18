
def test(filename):
    new_list = []
    for line in open(filename):
        if 'WARNING' in line:
            new_list.append(line)
            
        else:
            pass
    return new_list       




a = test('sample.txt')
print a




