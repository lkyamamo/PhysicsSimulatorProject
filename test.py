from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from panda3d.core import CollisionTraverser, CollisionHandlerEvent, NodePath
from panda3d.core import CollisionNode, CollisionSphere, CollisionPlane
from panda3d.core import Plane, Vec3, Point3
from panda3d.physics import ActorNode
from panda3d.physics import PhysicsCollisionHandler, PhysicsManager, LinearVectorForce, ForceNode



class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()
        self.enableParticles()

        #create actorNode and attach to render
        an = ActorNode('physicsNode')
        anP = NodePath(an)
        anP.reparentTo(self.render)
        anP.setPos(0,0,20)
        self.physicsMgr.attachPhysicalNode(an)

        #creating spher emodel
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
        gravityVector = LinearVectorForce(0,0,-9.816)
        gravity = ForceNode('gravity')
        gravityFNP = self.render.attachNewNode(gravity)
        gravity.addForce(gravityVector)

        self.physicsMgr.addLinearForce(gravityVector)

        #put camera in location
        self.camera.setPos(0,-100,0)

app = MyApp()
app.run()