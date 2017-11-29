"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Matthew De Clerck.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

john = rg.SimpleTurtle('turtle')
john.pen = rg.Pen('cyan', 10)
john.speed = 10

for k in range(10):
    john.pen_down()
    john.forward(30)
    john.left(10)
    john.right(70)
    john.pen_up()
    john.backward(50)
    john.pen_up()
    john.left(20)
    john.pen_up()

john.pen = rg.Pen('blue', 5)

for k in range(12):
    john.pen_down()
    john.forward(30)
    john.left(10)
    john.right(70)
    john.pen_up()
    john.backward(50)
    john.pen_up()
    john.left(30)
    john.pen_up()

john.pen = rg.Pen('green', 3)

for k in range(20):
    john.pen_down()
    john.forward(30)
    john.left(10)
    john.right(70)
    john.pen_up()
    john.backward(50)
    john.pen_up()
    john.left(40)
    john.pen_up()