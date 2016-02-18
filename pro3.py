def test(filename):
    new_dict = {}
    for line in open('sample1.txt'):
        line = line.rstrip('\n')
        cell = line.split('     ')
        name = cell[0]
        contact = cell[1]
        new_dict.update({cell[0]:cell[1]})
        
       
    return new_dict
    
    
a = test('sample.txt')
print a