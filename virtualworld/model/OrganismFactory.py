from .SpeciesEnum import *
from .animals.Antelope import Antelope
from .animals.Fox import Fox
from .animals.Human import Human
from .animals.Sheep import Sheep
from .animals.Turtle import Turtle
from .animals.Wolf import Wolf
from .plants.Dandelion import Dandelion
from .plants.DeadlyNightshade import DeadlyNightshade
from .plants.Grass import Grass
from .plants.Guarana import Guarana
from .plants.SosnowskiHogweed import SosnowskiHogweed
from .animals.CyberSheep import CyberSheep

class OrganismFactory(object):

    def createOrganism(self, species, position):
        colorMapping = {Antelope: "ORANGE",
                        SosnowskiHogweed: "CYAN",
                        Human: "BLACK",
                        Guarana: "BLUE",
                        Fox: "RED",
                        Dandelion: "YELLOW",
                        Sheep: "LIGHT GREY",
                        Grass: "GREEN",
                        DeadlyNightshade: "MAGENTA",
                        Wolf: "GREY",
                        Turtle: "PINK",
                        CyberSheep: "BLUE VIOLET"
                        }
        organism = None
        wybor = {}
        if not (position.x == -1) and not (position.y == -1):
            wybor = {
                SpeciesEnum.ANTELOPE: {"type" : Antelope, "position": position},
                SpeciesEnum.SOSNOWSKIHOGWEED: {"type" : SosnowskiHogweed, "position": position},
                SpeciesEnum.HUMAN: {"type" : Human, "position": position},
                SpeciesEnum.GUARANA: {"type" : Guarana, "position": position},
                SpeciesEnum.FOX: {"type" : Fox, "position": position},
                SpeciesEnum.DANDELION: {"type" : Dandelion, "position": position},
                SpeciesEnum.SHEEP: {"type" : Sheep, "position": position},
                SpeciesEnum.GRASS: {"type" : Grass, "position": position},
                SpeciesEnum.DEADLYNIGHTSHADE: {"type" : DeadlyNightshade, "position": position},
                SpeciesEnum.WOLF: {"type" : Wolf, "position": position},
                SpeciesEnum.TURTLE: {"type" : Turtle, "position": position},
                SpeciesEnum.CYBERSHEEP: {"type": CyberSheep, "position": position},
                }
            organism = wybor[species]["type"](position=wybor[species]["position"])
            organism.color = colorMapping[type(organism)]
            organism.initParam()
        return organism
