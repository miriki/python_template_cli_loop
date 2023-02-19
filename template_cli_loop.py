#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

#  ***************************************************************************
# *****************************************************************************
# ***                                                                       ***
# ***   class to get milliseconds as timer                                  ***
# ***   ----------------------------------                                  ***
# ***                                                                       ***
# ***   reset(): resets the timer to 0                                      ***
# ***                                                                       ***
# ***   millis(): gets the milliseconds since last reset()                  ***
# ***                                                                       ***
# *****************************************************************************
#  ***************************************************************************

class cls_timer:

    time_old = 0
    time_new = 0

    # --------------------

    def reset( self ):
        self.time_old = time.time()
        # self.time_new = self.time_old;

    # --------------------

    def millis( self ):
        self.time_new = time.time()
        result = ( self.time_new - self.time_old ) * 1000
        return result

    # --------------------

timer1 = cls_timer()

#  ***************************************************************************
# *****************************************************************************
# ***                                                                       ***
# ***   initial setup of values / states                                    ***
# ***   --------------------------------                                    ***
# ***                                                                       ***
# ***   should be called once at program start-up                           ***
# ***                                                                       ***
# *****************************************************************************
#  ***************************************************************************

def setup():

    print( "  ----- setup() ---------------" )

    # other setup duties ...

    timer1.reset()

#  ***************************************************************************
# *****************************************************************************
# ***                                                                       ***
# ***   working loop for the main program                                   ***
# ***   ---------------------------------                                   ***
# ***                                                                       ***
# ***   should be called repeatedly from the main program                   ***
# ***                                                                       ***
# ***   returns 'true' if finished successfully and can / should be         ***
# ***   called again for the next iteration                                 ***
# ***                                                                       ***
# ***   returns 'false' if conditions are met to stop further calls of      ***
# ***   the loop iterations - a keyboard interrupt for example              ***
# ***                                                                       ***
# *****************************************************************************
#  ***************************************************************************

def loop():

    loop_repeat = True

    try:

        # print( "  ----- loop() ---------------" )

        # loop duties

        interval1 = timer1.millis()
        # print( dur )

        if ( interval1 > 5000 ):

            print( "    ----- loop: 5 seconds interval ---------------" )
            # print( "    " + str( interval ))

            timer1.reset()

        # end loop?
        # if ( xxx ):
        #     loop_repeat = false

    except KeyboardInterrupt:

        print( "  keyboard interrupt in loop()" )
        loop_repeat = False

    return loop_repeat

#  ***************************************************************************
# *****************************************************************************
# ***                                                                       ***
# ***   the main program start-up                                           ***
# ***   -------------------------                                           ***
# ***                                                                       ***
# ***   it has to call:                                                     ***
# ***   * setup() once                                                      ***
# ***   * loop() repeatedly                                                 ***
# ***                                                                       ***
# *****************************************************************************
#  ***************************************************************************

if ( __name__ == '__main__' ):

    try:
        print( "----- main start ---------------" )

        # set up initial values / states
        print( "init via setup()" )
        setup()

        # repeat execution until stop signal
        print( "repeat via loop()" )
        loop_running = True
        while ( loop_running ):
            loop_running = loop()

    except KeyboardInterrupt:
        print( "keyboard interrupt in main()" )

    print( "finished" )
