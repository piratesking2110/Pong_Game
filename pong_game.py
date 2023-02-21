import turtle

win = turtle.Screen()
win.title("Game by Piratesking")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0) #tracer stops the screen so we have to manually update it , it makes our game faster

#score
score_a = 0
score_b = 0

# Paddle A (left side)
paddle_a=turtle.Turtle()
paddle_a.speed(0)#speed of animation not speed of paddle
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=8,stretch_len=1) #by default shape is 20px by 20px ,so what we did is we streched its width by 5x and height by 1x
#( width = up and down , length = left and right)
paddle_a.penup()#by default it(turtle) draws a line we dont need a line se we use penup()
paddle_a.goto(-350,0)#starts paddle at x & y coordinates


# Paddle B (right side)
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=8,stretch_len=1) 
paddle_b.penup()
paddle_b.goto(350,0)

# Boll which is in the center
boll=turtle.Turtle()
boll.speed(0)
boll.shape("square")
boll.color('white') 
boll.penup()
boll.goto(0,0)
#its the speed basically
boll.dx = 0.1 # here 2 epresents 2px 
boll.dy = -0.1 # because values of x and y are posiive it goes diagnally (up 2 and horizontal 2)
# all those will be done at below function(mainloop)



#pen
pen=turtle.Turtle()
pen.speed(0)# animation speed not movement speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A : 0 player B : 0",align="center",font=("courier",24,"normal"))


# functions
"""
    cordinates to note{
        x cordinates is left and right 
        y cordinates is up and down 
        center is zero(0,0)

        so from center if i want to go up that is +20 y cordinates 
        for down it would be -20 
        
        for right it would be +20
        for left it would be -20
    }
"""
def paddle_a_up():
    y = paddle_a.ycor()# paddle_a is the object ,ycor is from turtle module , it gives us the y corordinates
    y += 20 # same as y = y + 20(pixels) 
    paddle_a.sety(y) # we set the y or paddle_a to updated Y coordinate

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y) 
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 
    
# keybord binding
win.listen()# it lisen to keybord input
win.onkeypress(paddle_a_up,"w") #when we press W key , we call paddle_a_up function and it increse the y cordinate 
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")


# main game loop
while True:
    win.update()

    #move the ball
    boll.setx(boll.xcor() + boll.dx)
    boll.sety(boll.ycor() + boll.dy)
    
# border checking for boll

    # top border
    if boll.ycor() > 290: # we used 290 because our frame for up and down is 600 so its +300 and -300 as x and y coordinates
        boll.sety(290) #what it does is if ball reaches 290
        boll.dy *= -1 #bounce of to negative cordinates that is current ball cordinates * -1
     
    # bottom border
    if boll.ycor() < -290: 
        boll.sety(-290) 
        boll.dy *= -1 
        
          
    # #   rigth border 
    if boll.xcor() > 390: 
        boll.goto(0,0)
        boll.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player raja : {} player B : {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
            
    # # left border
    if boll.xcor() < -390: 
        boll.goto(0,0)
        boll.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player raja : {} player B : {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
        
    # paddle and boll fight lol
    
    '''
    {
        paddle and boll function doc for b_paddle(right)
        {
            if x-coordinate is > 340 and bolls x-coordinate is less than 350 
            and bolls y-coordinate < our b paddle's co-ordinates 
            and bolls y cordinate + 40 
            and bolls y cordinates > paddle b's (ycordinate is -40)
            then bounce off 
            ----------------------------------------------------------------------------------
            so its basically say width is 400 (-400=left,+400=right)
            if balls cordinates is between 340 and 350 then bounce off 
            
            and if bolls cordinate is less than paddles coordinate and boll goes 40px ahead 
            and bolls cordinate is > paddles cordinate by -40px
            a.k.a if ball touches the paddle then bounce off         
        }

    }
    '''
    if (boll.xcor() > 340 and boll.xcor() <350 ) and (boll.ycor() < paddle_b.ycor() and boll.ycor() + 80 and boll.ycor() > paddle_b.ycor() -80):
        boll.setx(340)
        boll.dx *= -1
        
        
    if (boll.xcor() < -340 and boll.xcor() > -350 ) and (boll.ycor() < paddle_a.ycor() and boll.ycor() + 80 and boll.ycor() > paddle_a.ycor() -80):
        boll.setx(-340)
        boll.dx *= -1
        
