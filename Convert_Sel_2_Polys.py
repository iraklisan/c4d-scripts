# convert selection to polys by iraklisan

import c4d

bc = c4d.BaseContainer()

bc[c4d.MDATA_CONVERTSELECTION_LEFT] = 5
bc[c4d.MDATA_CONVERTSELECTION_RIGHT] = 2

c4d.utils.SendModelingCommand(command = c4d.MCOMMAND_CONVERTSELECTION, list = [op], mode = 2, bc = bc, doc = doc)

c4d.CallCommand(12187)

c4d.EventAdd()
