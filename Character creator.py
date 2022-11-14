from graphics import*
from button import*


def main():
    
    win = GraphWin("character creator", 800, 600)
    win.setBackground("green")

    C = Circle(Point(300, 300), 250)
    C.draw(win)

    BigMouth = Oval(Point(200, 500), Point(400, 420))
    SmallMouth = Oval(Point(250, 500), Point(350, 450))

    BigNose = Polygon([Point(230, 400), Point(300, 300), Point(375,400)])
    SmallNose = Polygon([Point(250, 350), Point(300, 300), Point(350, 350)])

    
    BigEye1 = Circle(Point(200, 250), 50)
    BigEye2 = Circle(Point(400, 250), 50)

    smallEye1 = Circle(Point(250, 250), 20)
    smallEye2 = Circle(Point(350, 250), 20)

    B = Button(win, Point(600, 100), Point(700, 150), "tomato", "Big Eyes")
    B2 = Button(win, Point(600, 150), Point(700, 200), "tomato", "Small Eyes")

    N = Button(win, Point(600, 200), Point(700, 250), "coral2", "Big Nose")
    N2 = Button(win, Point(600, 250), Point(700, 300), "coral2", "Small Nose")

    M = Button(win, Point(600, 300), Point(700, 350), "tomato", "Big Mouth")
    M2 = Button(win, Point(600, 350), Point(700, 400), "tomato", "Small Mouth")

    Q = Button(win, Point(600, 400), Point(700, 450), "misty rose", "QUIT")
    

    while True:
        m = win.getMouse()

        if M.isClicked(m):
            BigMouth.undraw()
            SmallMouth.undraw()
            BigMouth.draw(win)

        if M2.isClicked(m):
            BigMouth.undraw()
            SmallMouth.undraw()
            SmallMouth.draw(win)
        
        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            
            BigEye1.draw(win)
            BigEye2.draw(win)
            
        if B2.isClicked(m):
            smallEye1.draw(win)
            smallEye2.draw(win)
            BigEye1.undraw()
            BigEye2.undraw()

        if N.isClicked(m):
            BigNose.undraw()
            SmallNose.undraw()
            BigNose.draw(win)

        if N2.isClicked(m):
            BigNose.undraw()
            SmallNose.undraw()
            SmallNose.draw(win)
            


        if Q.isClicked(m):
            break
        

    win.close()
       

if __name__ == "__main__":
    main()
