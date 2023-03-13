from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from panda3d.core import CollisionTraverser, CollisionHandlerEvent, NodePath, WindowProperties
from panda3d.core import CollisionNode, CollisionSphere, CollisionPlane
from panda3d.core import Plane, Vec3, Point3
from panda3d.physics import ActorNode
from panda3d.physics import PhysicsCollisionHandler, ForceNode, LinearVectorForce



class MyApp(ShowBase):

    #getting basics of having two physics nodes interacting with each other
    def createPhysicsNode(name):
        an = ActorNode('physicsNode')
        anP = NodePath(an)
        anP.reparentTo(self.render)
        self.physicsMgr.attachPhysicalNode(an)

    def __init__(self):
        ShowBase.__init__(self)

        wp = WindowProperties()
        wp.setSize(2048,1024)
        self.win.requestProperties(wp)

        self.cTrav = CollisionTraverser()
        self.disableMouse()
        self.enableParticles()

        #create earth and attach to render
        earth = ActorNode('earth')
        earthPath = NodePath(earth)
        earthPath.reparent(self.render)
        earthPath.setPos(20, 0, 0)
        self.physicsMgr.attachPhysicalNode(earth)
        


        #create moon