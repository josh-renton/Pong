__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time



#=======================================================

class PongLogo( QtGui.QLabel ):
    """ docstring on its way!"""

    def __init__( self, parent=None ):
        #super( Background, self ).__init__( self )
        QtGui.QLabel.__init__( self, parent=parent )


        self.image = QtGui.QPixmap()
        self.image.load( os.path.join( ".", "Resources", "Images", "pong" ), "PNG" )

        self.setPixmap( self.image )
        self.update()

class QuitIcon( QtGui.QIcon ):
    def __init__( self, parent=None ):
        QtGui.QIcon.__init__( self, parent=parent )

        self.exit_icon = QtGui.QPixmap( os.path.join( ".", "Resources", "Images", "blue_cross_icon.png" ) )
        self.addPixmap( self.exit_icon )