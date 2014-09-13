__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time



#=======================================================


class TopLevelMenu( QtGui.QMenuBar ):
'''
The top level menu for the game.

'''

    def __init__( self, text ):
        #super( TopLevelMenu, self ).__init__( self )
        QtGui.QMenuBar.__init__( self )
		
        self.update()
