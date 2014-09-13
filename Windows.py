__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time

import Menus
import CentralWidgets
import Timer

#=======================================================

class MainMenuWindow( QtGui.QMainWindow ):
    """ docstring on its way!"""

    def __init__( self ):
        #super( MainWindow, self ).__init__( self )
        QtGui.QMainWindow.__init__( self )
        
        self.setWindowTitle( "Josh's Pong" )

        self.activateWindow()
        print self.isActiveWindow()

        self.setupMenuBar()
        self.setupHomeScreen()


    def setupMenuBar( self ):
        self.menu_bar = Menus.TopLevelMenu()
        self.setMenuBar( self.menu_bar )

    def setupHomeScreen( self ):
        self.home_screen = CentralWidgets.HomeScreen()
        self.setCentralWidget( self.home_screen ) 
        self.update()
        self.show()




        