'''
Created on 2014/1/20

@author: hgy

mayaNode
'''
import math, sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeTypeName = "TDtrigonometricNode"

TDtrigonometricNodeId = OpenMaya.MTypeId(0x1001112)
#Node definition
class TDtrigonometricNode(OpenMayaMPx.MPxNode):
    #class variables
    input = OpenMaya.MObject()
    output = OpenMaya.MObject()
    
    def __init__(self):
        super(TDtrigonometricNode,self).__init__()
        
    def compute(self,plug,dataBlock):
        
        if(plug == TDtrigonometricNode.output):
        
            dataHandle = dataBlock.inputValue( TDtrigonometricNode.input )
            inputValue = dataHandle.asFloat()
            
            result = math.sin( inputValue )
            
            try:
                outputHandle = dataBlock.outputValue( TDtrigonometricNode.output )
                outputHandle.setFloat( result )
                
            except:
                sys.stderr.write("Failed to get dataHandle outputValue output")
                raise
                        
            dataBlock.setClean( plug )
        
        else:
            return OpenMaya.kUnknownParameter
        
#creator
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( TDtrigonometricNode() )

#initializer
def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    
    #input
    TDtrigonometricNode.input = nAttr.create("input", "in", OpenMaya.MFnNumericData.kFloat, 0.0)
    nAttr.setStorable(1)
    TDtrigonometricNode.addAttribute(TDtrigonometricNode.input)
    
    #output
    TDtrigonometricNode.output = nAttr.create("output", "out", OpenMaya.MFnNumericData.kFloat, 0.0)
    nAttr.setStorable(0)
    nAttr.setWritable(0)
    TDtrigonometricNode.addAttribute(TDtrigonometricNode.output)
    
    TDtrigonometricNode.attributeAffects( TDtrigonometricNode.input, TDtrigonometricNode.output )
    
#initialize the scriput plug-in
def initializePlugin(mobject):
    
    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    try:
        mplugin.registerNode( kPluginNodeTypeName, TDtrigonometricNodeId, nodeCreator, nodeInitializer )

    except:
        sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )
        raise 
    
#uninitialize the script plug-in
def uninitializePlugin(mobject):
    
    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    try:
        mplugin.deregisterNode( TDtrigonometricNodeId )

    except:
        sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )
        raise            
            