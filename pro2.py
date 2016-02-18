
new_dict = {}
f = open('sample1.txt')
for line in f.readlines():
    cell = line.split('     ')
    name = cell[0]
    contact = cell[1]
    new_dict[name] = contact
print new_dict    

    
    
    
    
    


def test(filename):
    new_dict = {}
    for line in open('sample1.txt')
    cell = line.split('     ')
    name = cell[0]
    contact = cell[1]
    new_dict[name] = contact
    return new_dict
    
    
a = test('sample.txt')
print a