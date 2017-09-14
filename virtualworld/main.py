from app_init import *
from model.World import World
from model.OrganismFactory import OrganismFactory
from model.SpeciesEnum import SpeciesEnum
import wx
import wx.lib.ogl as ogl
from controller.Controller import Controller
from view.View import View

if __name__ == "__main__":
    model = World(world_size_x, world_size_y, compasRose)
    factory = OrganismFactory()

    # add one human
    org = factory.createOrganism(SpeciesEnum.HUMAN, model.getFreePositionInWorld())
    org.world = model
    model.addOrganism(org)
    # add the rest
    for sp in SpeciesEnum:
        propName = "number_of_{0}".format(sp.name.lower())
        if propName in globals():
            propValInt = globals()[propName]
            # print(propValInt)
            if propName and not propName == "number_of_human":
                for i in range(0, propValInt):
                    org = factory.createOrganism(sp, model.getFreePositionInWorld())
                    if org:
                        org.world = model
                        model.addOrganism(org)

    # --------------
    #   Simple MVC
    # --------------
    app = wx.App(False)
    ogl.OGLInitialize()
    view = View(None)
    controller = Controller(app, model, view)


    app.MainLoop()

