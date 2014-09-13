import sys
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

app = QtGui.QApplication(sys.argv)

grview = QtGui.QGraphicsView()
scene = QtGui.QGraphicsScene()
scene.addPixmap( QtGui.QPixmap( ".", "Resources", "Images", "green_field" ), "PNG" ) )
grview.setScene(scene)

grview.show()

sys.exit(app.exec_())