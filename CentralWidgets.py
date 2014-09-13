__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time

import Assets
import Buttons
import Layouts
import Timer


#=======================================================

class HomeScreen( QtGui.QGraphicsView ):
    '''
    The starting point for the game. Where you begin/quit from,
    adjust player profiles and settings etc. 
    '''

    def __init__( self, parent=None ):
        QtGui.QGraphicsView.__init__( self, parent=parent )
       


        

        self.main_layout = Layouts.GridLayout( 1, 1 )

        # GUI setup

        # self.setupPaintTools()



        # self.respray_timer = Timer.Dur100()
        #self.respray_timer.timeout.connect( self.paintEvent )




        self.setupButtons()

        self.setupLayout()


        self.update()



    # def setupPaintTools( self ):

    #     self.red = QtGui.QColor( 255, 0, 0 )
    #     self.blue = QtGui.QColor( 0, 0, 255 ) 

    #     self.red_brush = QtGui.QBrush( self.red )
    #     self.blue_brush = QtGui.QBrush( self.blue )


    #     self.scene = QtGui.QGraphicsScene()
    #     self.setScene( self.scene )

        
    #    # self.painter.setPen( QtGui.QPen )

        


    # def paintEvent( self, e ):
    #     p = QtGui.QPainter( self )
    #     p.begin( self )

    #     self.fillBackground( event, p )

    # def fillBackground( self, event, painter ):

    #     painter.setBrush( self.red_brush )
    #     painter.setColour( self.red )
    #     painter.drawRect( event.rect(), self.rect() )

    def setupButtons( self ):

        self.play_button = Buttons.Play( parent=self )
        self.profile_button = Buttons.PushButton( 'User Profiles', parent=self )
        self.settings_button = Buttons.PushButton( 'Settings', parent=self )
        self.quit_button = Buttons.Quit( parent=self )

          

    def setupLayout( self ):

        #self.main_layout.setSpacing( 1 )

        # Temporary placeholder to give the frame shape
        #self.main_layout.addWidget( QtGui.QFrame(), 0, 99 )
        self.main_layout.addWidget( QtGui.QFrame(), 0, 0 )

        # Big Pong Logo
        self.pong_logo  = Assets.PongLogo()
        self.main_layout.addWidget( self.pong_logo, 1, 1 )                #row , column
        #self.main_layout.setRowMinimumHeight( 50, 5 )                 #row stretch, column stretch          
        #self.main_layout.setColumnMinimumWidth( 51, 5 )     
        #self.main_layout.setRowStretch( 1, 0 )
        #self.main_layout.setColumnStretch( 1, 0 )   

        self.main_layout.addWidget( self.play_button, 2, 1,) 
        #self.main_layout.setRowMinimumHeight( 55, 30 )                         
        #self.main_layout.setColumnMinimumWidth( 45, 40 )     
        #self.main_layout.setRowStretch( 60, 2 )
        #self.main_layout.setColumnStretch( 45, 0 )                     

        self.main_layout.addWidget( self.profile_button, 3, 3,) 
        #self.main_layout.setRowMinimumHeight( 95, 0 )                         
        #self.main_layout.setColumnMinimumWidth( 98, 0 )     
        #self.main_layout.setRowStretch( 0, 0 )
        #self.main_layout.setColumnStretch( 100, 0 )                 

        self.main_layout.addWidget( self.settings_button, 4, 3, )
        #self.main_layout.setRowMinimumHeight( 95, 10 )                         
        #self.main_layout.setColumnMinimumWidth( 99, 0 )     
        #self.main_layout.setRowStretch( 0, 0 )
        #self.main_layout.setColumnStretch( 100, 0 )                  

        self.main_layout.addWidget( self.quit_button, 0, 3 )
        self.main_layout.setRowMinimumHeight( 0, 1 )                         
        self.main_layout.setColumnMinimumWidth( 3, 1 )     
        #self.main_layout.setRowStretch( 0, 1 )
        #self.main_layout.setColumnStretch( 1, 1 )
        self.main_layout.setAlignment( self.quit_button, 0x0002 ) # Hex value for AlignRight


        self.main_layout.update()
        self.setLayout( self.main_layout )

        #print self.main_layout.verticalSpacing()
        #print self.main_layout.horizontalSpacing()
        #print self.main_layout.spacing()
        #print self.main_layout.columnCount()
        #print self.main_layout.rowCount()
        #print self.main_layout.columnMinimumWidth( 51 )
        #print self.main_layout.rowMinimumHeight( 50 )

    
    