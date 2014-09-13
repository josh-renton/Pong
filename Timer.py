__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time



#=======================================================

class Dur3( QtCore.QTimer ):
    '''
    Keeping everything ticking over
    '''

    def __init__( self ):
        #super( Background, self ).__init__( self )
        QtCore.QTimer.__init__( self )

        self.start( 3 )

class Dur100( QtCore.QTimer ):
    '''
    Keeping everything ticking over
    '''

    def __init__( self ):
        #super( Background, self ).__init__( self )
        QtCore.QTimer.__init__( self )

        self.start( 100 )

class TimeLine100( QtCore.QTimeLine ):
    '''
    Keeping everything ticking over
    '''

    def __init__( self ):
        #super( Background, self ).__init__( self )
        QtCore.QTimeLine.__init__( self )

        self.start( 100 )