import c4d

# Show_Hide toggle with Undo

def state():
    objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)

    if objs: return c4d.CMD_ENABLED

    return False

def main():

    objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    obj1 = objs[0]

    if obj1[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] < 2:
          vis = 2
    else: vis = 1

    for obj in objs:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, obj1)# AddUndo
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = vis
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = vis

if __name__=='__main__':
    doc.StartUndo();# StartUndo
    main()
    c4d.EventAdd()
    doc.EndUndo();# EndUndo