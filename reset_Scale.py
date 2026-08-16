import c4d

def main() -> None:
    settings = c4d.BaseContainer()
    settings[c4d.MDATA_RESETSYSTEM_COMPENSATE] = True
    settings[c4d.MDATA_RESETSYSTEM_RECURSIVE] = True
    
    res = c4d.utils.SendModelingCommand(command=c4d.MCOMMAND_RESETSYSTEM,
                                    list=[op],
                                    mode=c4d.MODELINGCOMMANDMODE_ALL,
                                    bc=settings,
                                    doc=doc)

    c4d.EventAdd()

if __name__ == '__main__':
    main()