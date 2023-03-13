from panda3d.core import CollisionTraverser, CollisionHandlerEvent, NodePath
from panda3d.core import CollisionNode, CollisionSphere, CollisionPlane
from panda3d.core import Plane, Vec3, Point3
from panda3d.physics import ActorNode
from panda3d.physics import PhysicsCollisionHandler, PhysicsManager, LinearVectorForce, ForceNode

#creates actor node, adds it to render, puts in physics manager
def createPhysicsNode(name):
    an = ActorNode('physicsNode')
    anP = NodePath(an)
    anP.reparentTo(self.render)
    self.physicsMgr.attachPhysicalNode(an)