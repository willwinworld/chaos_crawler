#f = open('sample.txt', 'r')
#content = f.read()
#f.close()

new_list = []
for line in open('sample.txt'):  
    if 'WARNING' in line:
        new_list.append(line)
        print new_list
    else:
        pass    
      
 
def test(new_list):
new_list = []
for line in open('sample.txt'):
    if 'WARNING' in line:
        new_list.append(line)
    else:
        pass
        
print test