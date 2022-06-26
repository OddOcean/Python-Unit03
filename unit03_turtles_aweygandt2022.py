############################################################################
#     Aidan Weygandt                        3.4.2021                      #
#     Unit 3 Problems                                                      #
#.    ASCII Characters, payroll application, random uppercase letter,      #
#     String Methods, Turtle Olympic Rings                                 #
############################################################################
import turtle

t1 = turtle
t1.width(5)
t1.pendown()
t1.color("#ff0000")
t1.circle(50) #red circle
t1.penup()

t1.right(180)  #positions turtle for next ring
t1.forward(10) #^
t1.left(90)    #^
t1.forward(10) #^
t1.right(180)  #^
t1.pendown()
t1.color("#008800")
t1.circle(50) #green ring

t1.penup()
t1.forward(10)     #positions turtle for fixing overlap
t1.right(90)       #^
t1.forward(10)     #^
t1.circle(50, 330) #^
t1.pendown()
t1.color("#ff0000")
t1.circle(50, 30) #covers up red overlap

t1.penup()
t1.right(180)      #positions turtle for next ring
t1.forward(10)     #^
t1.left(90)        #^
t1.forward(10)     #^
t1.right(180)      #^
t1.circle(50, 180) #^
t1.right(90)       #^
t1.forward(10)     #^
t1.right(90)       #^
t1.forward(10)     #^
t1.right(90)       #^
t1.pendown()
t1.color("#000000")
t1.circle(50) #black ring

t1.penup()     #positions turtle for fixing overlap
t1.forward(10) #^
t1.right(90)   #^
t1.forward(10) #^
t1.right(180)  #^
t1.pendown()
t1.color("#008800")
t1.circle(-50, 30) #fixes green overlap
t1.right(180)      #^
t1.circle(50, 30)  #^

t1.penup()
t1.right(90)
t1.forward(20)
t1.right(90)
t1.pendown()
t1.color("#FFFF00")
t1.circle(50) #yellow ring

t1.penup()
t1.forward(10) #positions turtle for fixing overlap
t1.right(90)   #^
t1.forward(10) #^
t1.right(180)  #^
t1.pendown()
t1.color("#000000")
t1.circle(-50, 30) #fixes black overlap
t1.right(180)      #^
t1.circle(50, 30)  #^

t1.penup()      #positions turtle for blue ring
t1.right(180)   #^
t1.forward(120) #^
t1.right(180)   #^
t1.pendown()
t1.color("#0000FF")
t1.circle(50) #blue ring

t1.penup()
t1.forward(10) #positions turtle for fixing overlap
t1.right(90)   #^
t1.forward(10) #^
t1.right(180)  #^
t1.pendown()
t1.color("#FFFF00")
t1.circle(-50, 30) #fixes black overlap
t1.right(180)      #^
t1.circle(50, 30)  #^
t1.penup()
t1.forward(75)
while 1 == 1 :
    turtle.right(1)