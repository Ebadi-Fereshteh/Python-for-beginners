from turtle import *
color('black', 'crimson')
begin_fill()
Pen()
shape("turtle")
speed(3)
bgcolor('white')
penup()
pendown()
i, j= 0, 0
side=0
while i < 10:
    left(180-((((i+3-2)*180)/(i+3))/2))
    side=100+side
    while j <= i+2:
        pencolor('black')
        width(2)
        forward(side/(i+3))
        left(180-(((i+3-2)*180)/(i+3)))
        j += 1
        if i==9 and j==12:
            end_fill()
            pencolor('black')
            width(2)
            left(-60-(((i+3-2)*180)/(i+3)))
            forward(side/(i+3))
            # j -= 1
            left(-60-(((i+3-2)*180)/(i+3)))
            backward(side/(i+3))
            # j -= 1
            left(-60-(((i+3-2)*180)/(i+3)))
            forward(side/(i+3))
            # j -= 1
            left(45-(((i+3-2)*180)/(i+3)))
            backward(250)
            forward(145)
            color('black', 'green')
            begin_fill()
            right(45)
            forward(200)
            right(90)
            forward(125)
            right(160)
            forward(100)
            left(60)
            forward(167)   
            end_fill()         

    penup()
    right(180-(((i+3-2)*180)/(i+3)))
    right((((i+3-2)*180)/(i+3))/2)
    forward(17)
    pendown()
    j=0
    i+=1
# end_fill()
done()
