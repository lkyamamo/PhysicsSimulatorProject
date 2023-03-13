from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from panda3d.core import CollisionTraverser, CollisionHandlerEvent, NodePath, WindowProperties
from panda3d.core import CollisionNode, CollisionSphere, CollisionPlane
from panda3d.core import Plane, Vec3, Point3
from panda3d.physics import ActorNode
from panda3d.physics import PhysicsCollisionHandler, ForceNode, LinearVectorForce

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        wp = WindowProperties()
        wp.setSize(2048,1024)
        self.win.requestProperties(wp)

        self.cTrav = CollisionTraverser()
        self.disableMouse()
        self.enableParticles()

        #create actorNode and attach to render
        an = ActorNode('physicsNode')
        anP = NodePath(an)
        anP.reparentTo(self.render)
        anP.setPos(0,0,20)
        self.physicsMgr.attachPhysicalNode(an)
        an.getPhysicsObject().setMass(12)
        

        #creating sphere model
        sphere = self.loader.loadModel("models/misc/sphere")
        sphere.reparentTo(anP)
        sphere.setPos(0,0,0)

        #creating collision object
        cs = CollisionSphere(0,0,0,1)
        cnodePath = NodePath(CollisionNode('cnode'))
        cnodePath.node().addSolid(cs)
        cnodePath.reparentTo(anP)

        #adding to collision handler
        pusher = PhysicsCollisionHandler()
        pusher.addCollider(cnodePath, anP)
        
        #creating gravity force node
        gravityVector = LinearVectorForce(0,0,-20)
        gravity = ForceNode('gravity')
        gravityFNP = self.render.attachNewNode(gravity)
        gravity.addForce(gravityVector)

        self.physicsMgr.addLinearForce(gravityVector)

        #make collision plane aka the floor
        cf = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, 0)))
        floorNP = NodePath(CollisionNode('floor'))
        floorNP.node().addSolid(cf)
        floorNP.reparentTo(self.render)
        floorNP.setPos(0,0,0)
        
        #add collision interaction to traverser
        self.cTrav.addCollider(cnodePath, pusher)


        #put camera in location
        self.camera.setPos(0,-100,0)


app = MyApp()
app.run()