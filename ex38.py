ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') #分割成列表
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff)  !=10:
    next_one = more_stuff.pop() #默认移除最后列表最后一项，并返回这个值
    print "Adding: ", next_one
    stuff.append(next_one) #追加元素
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] 
print stuff.pop()
print ' '.join(stuff)   #以空格连接起来
print '#'.join(stuff[3:5]) #从3到4