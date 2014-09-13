__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time

import Assets



#=======================================================


class PushButton( QtGui.QPushButton ):
    '''
    An abstract PushButton class. A basis for all PushButtons instantiated.

    '''

    def __init__( self, text, parent=None ):
        #super( PushButton, self ).__init__( self )
        QtGui.QPushButton.__init__( self, text=text, parent=parent )

        self.update()

    def fitToScreenRatio( self, divider, isSquare=False ):
        '''
        Ensuring standardised size, taken from parent window
        '''
        height = self.parent().rect().height() / divider       

        if isSquare:
            width = height
        else:
            height /= 2
            width = ( self.parent().rect().width() / divider ) * 3


        self.setMaximumSize( QtCore.QSize( width, height ) )
        self.setMinimumSize( QtCore.QSize( width, height ) )


class Play( PushButton ):
    '''
    Get cho game onnnnn

    '''

    def __init__( self, text='Play!', parent=None ):
        #super( PushButton, self ).__init__( self )
        QtGui.QPushButton.__init__( self, text=text, parent=parent )

        self.fitToScreenRatio( 4 )

        self.update()



class Quit( PushButton ):
    '''
    A standard exit button.

    '''

    def __init__( self, parent=None ):
        #super( PushButton, self ).__init__( self )
        PushButton.__init__( self, None, parent=parent )

        self.fitToScreenRatio( 12, isSquare=True )

        self.setIcon( Assets.QuitIcon( parent=self ) )

        self.clicked.connect( self.quit )

        self.update()

    def quit( self ):
        sys.exit( 0 )