from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

wall_repair_limit = 300000

def heal(room):

    towers = []
    structures = room.find(FIND_STRUCTURES)
    for structure in structures:
        if structure.structureType == STRUCTURE_TOWER:
            towers.append(structure)

    targets = []
    structures = room.find(FIND_STRUCTURES)
    for structure in structures:
        if structure.structureType == STRUCTURE_WALL and structure.hits < wall_repair_limit:
            targets.append(structure)
        
        if len(targets) > 0:
            for i in towers:
                i.repair(targets[0])

def defend(room, mode):
    hostiles = room.find(FIND_HOSTILE_CREEPS)
    if hostiles.length > 0:

        towers = []
        structures = room.find(FIND_STRUCTURES)
        for structure in structures:
            if structure.structureType == STRUCTURE_TOWER:
                towers.append(structure)
        
        if mode:
            for i in towers:
                i.attack(i.pos.findClosestByRange(FIND_HOSTILE_CREEPS))
        else:
            for i in towers:
                i.attack(hostiles[0])