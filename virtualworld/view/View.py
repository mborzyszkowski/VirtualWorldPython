import wx
import wx.lib.ogl as ogl
from model.animals.Human import Human
from model.DirectionEnum import DirectionEnum
from model.SpeciesEnum import  SpeciesEnum
from model.Position import Position
import math


class View(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Maciej Borzyszkowski 165407")
        # ogl.OGLInitialize()
        self.controller = None
        self.pref_size_w = 800
        self.pref_size_h = 600
        self.sideMapLenght = 20
        self.beforeStart=True
        self.saveFileName = "saveWorld.pck"
        self.worldMap = None


        self.panel = wx.Panel(self, wx.ID_ANY)
        self.logger = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(270, 400))

        self.canvas = ogl.ShapeCanvas(self.panel)
        self.canvas.SetBackgroundColour("white")
        self.diagram = ogl.Diagram()
        self.canvas.SetDiagram(self.diagram)
        self.diagram.SetCanvas(self.canvas)
        self.canvas.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)

        glownySizer = wx.BoxSizer(wx.VERTICAL)
        outputSizer = wx.BoxSizer(wx.HORIZONTAL)
        outStaticBoxSizer = wx.BoxSizer(wx.VERTICAL)
        drawBoxSizer = wx.BoxSizer(wx.VERTICAL)
        labelSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        glownySizer.AddStretchSpacer(1)
        outputSizer.AddStretchSpacer(1)
        labelSizer.AddStretchSpacer(1)

        drawBoxSizer.Add(self.canvas, proportion = 1, flag=wx.EXPAND|wx.GROW )
        outputSizer.Add(drawBoxSizer, proportion = 60, flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALIGN_TOP )

        outStaticBoxSizer.Add(self.logger, proportion = 1, flag=wx.EXPAND|wx.ALIGN_TOP)
        outputSizer.Add(outStaticBoxSizer, proportion = 30, flag=wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_TOP)
        outputSizer.AddStretchSpacer(1)

        self.nextTurn = wx.Button(self.panel, -1, "Start")
        self.nextTurn.Bind(wx.EVT_BUTTON, self.nextTurnOnClicked)

        self.saveBtn = wx.Button(self.panel, -1, "Save")
        self.saveBtn.Bind(wx.EVT_BUTTON, self.saveOnClick)
        self.loadBtn = wx.Button(self.panel, -1, "Load")
        self.loadBtn.Bind(wx.EVT_BUTTON, self.loadOnClick)
        self.humanAbilityBtn = wx.Button(self.panel, -1, "Human ability: 0")
        self.humanAbilityBtn.Bind(wx.EVT_BUTTON, self.humanAbilityClick)

        self.labelOrgStatus = wx.StaticText(self.panel, wx.ID_ANY, 'Info:')
        self.labelHumanStatus = wx.StaticText(self.panel, wx.ID_ANY, 'Human status: Start')
        self.labelTurnNum = wx.StaticText(self.panel, wx.ID_ANY, 'Turn number: 0')

        buttonSizer.Add(self.nextTurn, proportion=0 ,flag=wx.ALL|wx.ALIGN_LEFT)
        buttonSizer.Add(self.saveBtn, proportion=0 ,flag=wx.ALL|wx.ALIGN_LEFT)
        buttonSizer.Add(self.loadBtn, proportion=0, flag=wx.ALL | wx.ALIGN_LEFT)
        buttonSizer.Add(self.humanAbilityBtn, proportion=0, flag=wx.ALL | wx.ALIGN_LEFT)
        buttonSizer.AddStretchSpacer(1)
        buttonSizer.Add(self.labelHumanStatus, proportion=0, flag=wx.ALL | wx.ALIGN_LEFT)
        buttonSizer.AddStretchSpacer(1)
        buttonSizer.Add(self.labelTurnNum, proportion=0, flag=wx.ALL | wx.ALIGN_LEFT)
        buttonSizer.AddStretchSpacer(5)

        labelSizer.Add(self.labelOrgStatus, proportion=0, flag=wx.ALL|wx.EXPAND|wx.ALIGN_LEFT)
        labelSizer.AddStretchSpacer(10)

        glownySizer.Add(outputSizer, proportion = 70, flag=wx.ALL|wx.EXPAND)
        glownySizer.AddStretchSpacer(1)
        glownySizer.Add(labelSizer, proportion = 10, flag=wx.ALL | wx.EXPAND|wx.ALIGN_LEFT)
        glownySizer.Add(buttonSizer, proportion = 10, flag=wx.ALL | wx.EXPAND)
        self.panel.SetSizer(glownySizer)
        glownySizer.Fit(self)

        self.panel.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)
        self.Centre()
        self.Show(1)

    def setController(self, controller):
        self.controller = controller

    def getSideMapLenght(self):
        return self.sideMapLenght

    def set_ogranisms_to_canvas(self):
        self.canvas.GetDiagram().RemoveAllShapes()
        cellsList = self.controller.getWorldMap()
        self.worldMap = cellsList
        for cells in cellsList:
            for cell in cells:
                cell.shape.SetBrush(wx.Brush(cell.color))
                self.canvas.AddShape(cell.shape)
        self.diagram.ShowAll(1)
        dc = wx.ClientDC(self.canvas)
        self.canvas.PrepareDC(dc)
        self.canvas.Redraw(dc)

    def nextTurnOnClicked(self, event):
        if not self.beforeStart:
            self.controller.performNextTurn()
        else:
            self.beforeStart = False
            self.nextTurn.SetLabelText("Next turn")
        self.logger.WriteText("\nTurn: {0}\n".format(str(self.controller.getTurnNumber())))
        self.logger.WriteText(self.controller.getActionLoggerReport())
        self.set_ogranisms_to_canvas()
        humanSkillCnt = self.controller.getHumanCounterTurnOfSkill()
        if humanSkillCnt >= 0:
            self.humanAbilityBtn.SetLabelText("Human ability: {0}".format(str(humanSkillCnt)))
        else:
            self.humanAbilityBtn.SetLabelText("No Human")
        if self.controller.canTurnHumanSkillOn():
            self.humanAbilityBtn.Enable()
        else:
            self.humanAbilityBtn.Disable()
        self.labelTurnNum.SetLabel("Turn number: {0}".format(str(self.controller.getTurnNumber())))
        self.labelHumanStatus.SetLabel(self.controller.getHumanStatus())


    def saveOnClick(self, event):
        self.controller.saveModel(self.saveFileName)

    def loadOnClick(self, event):
        self.controller.loadModel(self.saveFileName)

    def humanAbilityClick(self, event):
        self.controller.turnHumanSkillOn()

    def onKeyPress(self, event):
        print("keyevent")
        org = self.controller.model.getHuman()
        if org is not None:
            if type(org) == Human:
                keyCode = event.GetKeyCode()
                if self.controller.model.compasRose == 8:
                    if keyCode == wx.WXK_UP:
                        org.direction = DirectionEnum.FOUR_DIR_UP
                    elif keyCode == wx.WXK_DOWN:
                        org.direction = DirectionEnum.FOUR_DIR_DOWN
                    elif keyCode == wx.WXK_RIGHT:
                        org.direction = DirectionEnum.FOUR_DIR_RIGHT
                    elif keyCode == wx.WXK_LEFT:
                        org.direction = DirectionEnum.FOUR_DIR_LEFT
                elif self.controller.model.compasRose == 6:
                    if keyCode == wx.WXK_UP:
                        org.direction = DirectionEnum.SIX_DIR_UP
                    elif keyCode == wx.WXK_DOWN:
                        org.direction = DirectionEnum.SIX_DIR_DOWN
                    elif keyCode == wx.WXK_RIGHT:
                        if event.ShiftDown():
                            org.direction = DirectionEnum.SIX_DIR_UP_RIGHT
                        else:
                            org.direction = DirectionEnum.SIX_DIR_DOWN_RIGHT
                    elif keyCode == wx.WXK_LEFT:
                        if event.ShiftDown():
                            org.direction = DirectionEnum.SIX_DIR_UP_LEFT
                        else:
                            org.direction = DirectionEnum.SIX_DIR_DOWN_LEFT

    def onLeftDown(self, event):
        # print (event.GetPosition() )
        clickedCell = None
        minDistannce = 1000
        for cells in self.worldMap:
            for cell in cells:
                pom = Position(xpos=cell.shape.GetX(), ypos=cell.shape.GetY())\
                            .distance(Position(xpos=event.GetX(), ypos=event.GetY()))
                if pom < minDistannce:
                    clickedCell = cell
                    minDistannce = pom
        # print (clickedCell)
        if minDistannce <= self.sideMapLenght:
            if clickedCell.is_empty:
                specNames = [sp.name for sp in SpeciesEnum if not sp.name == "HUMAN"]
                dlg = wx.SingleChoiceDialog( self, "Choose organism:", "Choose",  specNames, wx.CHOICEDLG_STYLE )
                if dlg.ShowModal() == wx.ID_OK:
                    # print ("You selected: %s\n" % dlg.GetStringSelection())
                    if self.controller.addOrganism(
                            SpeciesEnum[dlg.GetStringSelection()],
                            Position(xpos=clickedCell.x, ypos=clickedCell.y)):
                        self.set_ogranisms_to_canvas()
                dlg.Destroy()
            else:
                self.labelOrgStatus.SetLabelText("Info: {0}"\
                                             .format(self.controller\
                                                     .model\
                                                     .getOrganismFromPosition(Position(xpos=clickedCell.x, ypos=clickedCell.y))
                                                     )
                                             )

