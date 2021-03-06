# Copyright (c) 2015 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.

#Shoopdawoop
from UM.Mesh.MeshData import MeshData
from UM.Mesh.MeshBuilder import MeshBuilder
from UM.Math.Color import Color
from UM.Math.Vector import Vector

import numpy
import math
import copy
import cura
from . import LayerData
from . import Cura_pb2
from . import CuraEngineBackend

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "plugin": {
            "name": catalog.i18nc("@label", "CuraEngine Backend"),
            "author": "Ultimaker",
            "description": catalog.i18nc("@info:whatsthis", "Provides the link to the CuraEngine slicing backend"),
            "api": 2
        }
    }

def register(app):
    return { "backend": CuraEngineBackend.CuraEngineBackend() }

