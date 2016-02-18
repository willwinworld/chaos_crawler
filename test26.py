def test(filename , content):
    o = open (filename , 'w')
    o.write(content)
    o = open (filename , 'r')
    o.read()
 

test('hi.txt' , 'dream')