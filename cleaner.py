__author__='Josh Renton'

#------------------------------------------------------
import sys
import os
import shutil

components = ('Application.py',
              'Background.py',
              'CentralDictionaryDatabase.py', 
              'MainWindow.py',
              'Resources', 
              '__init__.py', 
              'cleaner.py',
                  )



if __name__ == '__main__' :

    print '\n'
    root = os.path.join( "." )
    files = os.listdir( root )

    print files

    for f in files :
        if f in components :
            print f, "is in components. Proceeding...."

        else:
            print "\n" + f + " is not in components list."

            try:
                delete_or_not = str( raw_input( "Would you like it removed? y/n\n" ) )
                delete_or_not = delete_or_not.lower()
                print delete_or_not

                if delete_or_not == 'y':
                    print 'y confirmed'
                    
                    deleted = os.remove( f )
                    print 'os.remove?'

                    if deleted == None:
                        print '\nDeleted'

                    else:
                        shutil_ = shutil.rmtree( f )
                        print "shutil.rmtree", shutil_
                  
                    
            except:
                pass