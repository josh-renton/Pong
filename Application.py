__author__='Josh Renton'

#------------------------------------------------------
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

import sys
import os
import time

import Windows


#=======================================================

class AppContainer( object ):
    def __init__( self ):
        
        self.qt_app = QtGui.QApplication( sys.argv )


        self.desktop_handle = self.qt_app.desktop()
        self.geo_available = self.findScreenGeo()
        self.randomStyleGen()

        self.main_menu = Windows.MainMenuWindow()
        self.main_menu.setGeometry( self.geo_available )





        self.qt_app.exec_()
        self.exit()



    def findScreenGeo( self ):
        geo_available = self.desktop_handle.availableGeometry()
        return geo_available

    def exit( self ):
        print "Goodbye, I hope you're ponged out!"
        sys.exit(0)

    def randomStyleGen( self ):
        import random

        styles = [  #'macintosh',
                    'plastique',
                    #'windows',
                    #'common',
                    #'cleanlooks',
                    #'gtk' 
                    ]

        x = random.randint( 0, ( len( styles ) - 1 ) )
        y = styles[ x ]

        self.qt_app.setStyle( y )

        style_set = str( self.qt_app.style() )
        #print 'App Style is: ' + style_set[ 15 : style_set.find( "Style" ) ]
        
    
    





