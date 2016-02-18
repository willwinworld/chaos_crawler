def anything(filename , content):
    o = open(filename , 'w')
    o.write(content)
    o = open(filename ,'r')                   
    o.read()
    
anything('goodmorning.txt' , 'what\'s up') #要注意对‘进行转义

#or


#filename = 'goodmorning.txt'
#content = 'what's up'
#anything = (filename , content)


#需要注意的事，变量也是字符串的一种，可以在最后一行将变量直接往函数里代入，但是先要对变量进行赋值
#问题：为什么不能写进一个式子里？
#def anything(filename , content):
    #o = open(filename , 'w' , 'r')
    #o = write(content)
    #o = read()
    
    "it's a dog"
    
   