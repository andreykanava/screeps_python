from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run(creep):
    if creep.store.getFreeCapacity() == creep.store.getCapacity():
        if not creep.room.find(FIND_DROPPED_RESOURCES):

            sources = []
            structures = creep.room.find(FIND_STRUCTURES)
            for structure in structures:
                if structure.structureType == STRUCTURE_CONTAINER:
                    sources.append(structure)

            if creep.withdraw(sources[1], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                creep.moveTo(sources[1])
        else:
            sources = creep.pos.findClosestByPath(FIND_DROPPED_RESOURCES)
            if creep.pickup(sources, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                creep.moveTo(sources)
    else:

        targets = []
        structures = creep.room.find(FIND_STRUCTURES)
        for structure in structures:
            if structure.structureType == STRUCTURE_EXTENSION or structure.structureType == STRUCTURE_SPAWN and structure.store.getFreeCapacity(RESOURCE_ENERGY) > 0:
                targets.append(structure)

        if len(targets) > 0:
            if creep.transfer(targets[0], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                creep.moveTo(targets[0])
        else:

            targets = []
            structures = creep.room.find(FIND_STRUCTURES)
            for structure in structures:
                if structure.structureType == STRUCTURE_TOWER and structure.store.getFreeCapacity(RESOURCE_ENERGY) > 0:
                    targets.append(structure)

            if len(targets) > 0:
                if creep.transfer(targets[0], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                    creep.moveTo(targets[0])
