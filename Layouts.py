__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time


#=======================================================

class GridLayout( QtGui.QGridLayout ):
    '''
    Coz we gon lay yo shit out son!
    '''
    def __init__( self, horz_space, ver_space ):
        QtGui.QGridLayout.__init__( self )

        self.setHorizontalSpacing( horz_space )
        self.setVerticalSpacing( ver_space )

    
    