import bpy

def select_all():
    bpy.ops.object.select_all(action='SELECT')


def select(objName, additive=False):
    # By default, clear other selections
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')

    # Set the 'select_set' function (2.8+) of the datablock to True
    bpy.data.objects[objName].select_set(True)

# Delete an object by name
def delete(objName):
    select(objName)
    bpy.ops.object.delete(use_global=False)


# Delete all objects
def delete_all():
    if (len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

def activate(objName):
    # Pass bpy.data.objects datablock to scene class
    bpy.context.view_layer.objects.active = bpy.data.objects[objName]


def specify(objName):
    # Return the datablock
    return bpy.data.objects[objName]


# Function for entering Edit Mode with no vertices selected,
# or entering Object Mode with no additional processes

def mode(mode_name):
    bpy.ops.object.mode_set(mode=mode_name)
    if mode_name == "EDIT":
        bpy.ops.mesh.select_all(action="DESELECT")


class sel:
    """Function Class for operating on SELECTED objects"""

    '''
    Differential location translate
    input: float array of 3 items
    '''

    def translate(v):
        bpy.ops.transform.translate(
            value=v, constraint_axis=(True, True, True))

    '''
    Differential scale
    input: float array of 3 items
    '''

    def scale(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))

    '''
    Differential X rotation
    input: float 
    '''

    def rotate_x(v):
        bpy.ops.transform.rotate(value=v, orient_axis='X')

    '''
    Differential Y rotation
    input: float 
    '''

    def rotate_y(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Y')

    '''
    Differential Z rotation
    input: float 
    '''

    def rotate_z(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Z')


class act:
    """Function Class for operating on ACTIVE objects"""

    '''
    Declarative location
    input: float array of 3 items
    '''

    def location(v):
        bpy.context.object.location = v

    '''
    Declarative scale
    input: float array of 3 items
    '''

    def scale(v):
        bpy.context.object.scale = v

    '''
    Declarative rotation
    input: float array of 3 items  
    '''

    def rotation(v):
        bpy.context.object.rotation_euler = v

    '''
    Rename active object
    input: string
    '''

    def rename(objName):
        bpy.context.object.name = objName


class spec:
    """Function Class for operating on SPECIFIED objects"""

    '''
    Declarative scale
    input: float array of 3 items
    '''

    def scale(objName, v):
        bpy.data.objects[objName].scale = v

    '''
    Declarative location
    input: float array of 3 items
    '''

    def location(objName, v):
        bpy.data.objects[objName].location = v

    '''
    Declarative rotation
    input: float array of 3 items
    '''

    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v


class create:
    """Function Class for CREATING Objects"""
    '''Every object which is created is also selected'''

    def cube(objName):
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
        act.rename(objName)

    def sphere(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0))
        act.rename(objName)

    def cone(objName):
        bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0))
        act.rename(objName)

