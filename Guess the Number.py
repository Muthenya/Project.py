# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0
width = 400
height = 300
interval = 10
tick = 0
position = [150,150]
x = 0 #score counter for wins
y = 0 #score counter for total trials

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t > 599:
        if ((t%600)//10) < 9:
            message = str(int(t-t%600) / 600) + ":0" + str(int((t%600) // 10)) + "." +str(int((t%600)%10))
            return message
        else:
            message = str(int(t-t%600) / 600) + ":" + str(int((t%600) // 10)) + "." +str(int((t%600)%10))
            return message
    else:
        if t <= 599 and t > 100:
            message = "0:" + str(int(t//10)) + "." + str(int((t%100)%10))
            return message
        else:
            message = "0:0" + str(int(t//10)) + "." + str(int((t%100)%10))
            return message
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    
    
def Stop():
    global x,y
    if timer.is_running():
        timer.stop()
        if int((t%100)%10) == 0 or int((t%600)%10) == 0:
            x += 1
            y += 1
            return x,y
        else:
            x += 0
            y += 1
            return x,y
    
def Reset():
    global x, y, t
    if timer.is_running:
        timer.stop()
        x,y = 0,0
        t = 0
# define event handler for timer with 0.1 sec interval
def ticker():
    global t
    t += 0.1

# define draw handler

def draw(canvas):
    canvas.draw_text(format(t), position, 48, "White")
    canvas.draw_text(str(x) + "/" + str(y), [300,30], 36 ,"Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch", width, height)
Start_Button = frame.add_button('Start', Start, 100)
Stop_Button = frame.add_button('Stop', Stop, 100)
Reset_Button = frame.add_button('Reset', Reset, 100)


# register event handlers
timer = simplegui.create_timer(10, ticker)
frame.set_draw_handler(draw)

# start frame
frame.start()
# Please remember to review the grading rubric
