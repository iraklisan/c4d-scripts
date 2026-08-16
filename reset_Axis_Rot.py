import c4d

def main() -> None:
    # 1. Fetch active selection
    objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not objs:
        return

    doc.StartUndo()
   
    for obj in objs:
        # SAFETY CHECK: Only polygon objects have points to manipulate
        if not isinstance(obj, c4d.PolygonObject):
            continue

        # Save initial global matrix
        mg = obj.GetMg()
    
        # Extract the scale of the current matrix
        scale = c4d.Vector(mg.v1.GetLength(),
                           mg.v2.GetLength(),
                           mg.v3.GetLength())
    
        # Builds a new matrix with zeroed-out rotation
        HPB_rot = c4d.Vector(0, 0, 0)
        m = c4d.utils.HPBToMatrix(HPB_rot)
    
        m.off = mg.off
        m.v1 = m.v1.GetNormalized() * scale.x
        m.v2 = m.v2.GetNormalized() * scale.y
        m.v3 = m.v3.GetNormalized() * scale.z
            
        #
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj) 
        
        # Apply the new orientation matrix to the object axis
        obj.SetMg(m)
    
        # Compute the transformation offset matrix between old and new state
        transform = ~obj.GetMg() * mg
    
        # Transform all points to compensate for the axis rotation change
        all_points = obj.GetAllPoints()
        transformedPoints = [transform * p for p in all_points]
        
        obj.SetAllPoints(transformedPoints)
        obj.Message(c4d.MSG_UPDATE)
    
    # 
    doc.EndUndo()
    c4d.EventAdd()

if __name__ == '__main__':
    main()
