import maya.OpenMaya as om
import maya.OpenMayaAnim as oma
import pymel.core as pm

sel = pm.ls(sl=True)[0]
selShape = sel.getShape()
sel_skin = selShape.listConnections(type="skinCluster")[0]
selShapeString = selShape.name()
sel_skinString = sel_skin.name()

msl_shape = om.MSelectionList()
msl_shape.add(selShapeString)
mobj_shape = om.MObject()
msl_shape.getDependNode(0,mobj_shape)
mdgp_shape = om.MDagPath()
mobj_cpn = om.MObject()
msl_shape.getDagPath(0,mdgp_shape,mobj_cpn)

msl_skin = om.MSelectionList()
msl_skin.add(sel_skinString)
mobj_skin = om.MObject()
msl_skin.getDependNode(0,mobj_skin)

mfn_skin = oma.MFnSkinCluster(mobj_skin)
infs = om.MDagPathArray()
infCount = mfn_skin.influenceObjects(infs)

weights = om.MFloatArray()

mfn_dn_cpn = om.MFnDagNode(mobj_cpn)
print mfn_dn_cpn.name()
#for i in range(infs.length()):
    #inf = infs.__getitem__(i)
    #mfn_skin.getWeights(mdgp_shape,mobj_cpn,i,weights)
    #print weights
