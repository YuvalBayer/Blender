# Blender

In order to import a directory use this for one time:

  import bpy
  import sys
  import os

  dir = os.path.dirname(bpy.data.filepath)
  if not dir in sys.path:
    sys.path.append(dir )
    
If you need to update the directory use this one afterward
  
  import imp
  imp.reload("dir name")

Use this one each time:

  from ut import *
  import bmesh

  if str((bpy.context.object))!='None': # Checking if there is activated object
    mode('OBJECT') # if there isn't we are not in active mode for sure  
  delete_all()
