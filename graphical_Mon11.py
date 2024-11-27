from layover import layover
from oversold import  oversold
from daily_data import daily_data
from fleet_data import fleet_data
from passenger_data import passenger_data
from overweight import overweight
import turtle
def graphical_Mon11(oversold, overweight, layover):
    '''Accepts 2-D lists oversold, overweight, layover and time delay. Displays flight and passenger 
    information organized by flight model. '''
    turtle.setup(1000, 450)
    t = turtle.Turtle()
    screen = turtle.Screen()
    x = -450
    t.pu()
    
    for os_b in oversold[0]: # oversold business list
        t.goto(x,60)
        t.color("lightpink")
        t.begin_fill()
        t.pd()
		# Draw background square
        for i in range (4):
            t.forward(120)
            t.right(90)
        t.end_fill()
        # draws header rectangle
        t.color("lightblue")
        t.pu()
        t.begin_fill()
        t.forward(120)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(120)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.end_fill()
        t.color("black")
        t.goto(x+60,40)
        # Writes flight model in header
        t.write(os_b[0], align = 'center')
        
        t.goto(x+60,20)
        t.write(f"Oversold business:{os_b[1]}", align = 'center') # oversold business seats
        for os_e in oversold[1]: # oversold economy list
            if os_e[0] == os_b[0]:
                t.goto(x+60,0)
                t.write(f"Oversold economy:{os_e[1]}", align = 'center') # oversold economy seats
        for overweight_list in overweight[0]: # plane overweight list
            if overweight_list[0] == os_b[0]:
                t.goto(x+60,-20)
                t.write(f"Overweight bags:{overweight_list[1]}", align = 'center') 
        for layover_list in layover[1]: # plane layover list
            if layover_list[0] == os_b[0]:
                t.goto(x+60,-40)
                t.write(f"Late Layover:{layover_list[1]}", align = 'center') # amount of passengers that have late layover
        # x-coordinate for next rectangle
        x += 130
    t.hideturtle()
    screen.exitonclick()
    turtle.done()

Daily_data = daily_data(passenger_data())
Oversold = oversold(fleet_data(), Daily_data)
Overweight = overweight(fleet_data(), passenger_data())
Layover = layover(fleet_data(), passenger_data())
graphical_Mon11(Oversold,Overweight,Layover)