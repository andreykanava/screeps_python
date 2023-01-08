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
    if creep.memory.upgrading and creep.store[RESOURCE_ENERGY] == 0:
        creep.memory.upgrading = False
    
    if not creep.memory.upgrading and creep.store.getFreeCapacity(RESOURCE_ENERGY) == 0:
        creep.memory.upgrading = True

    if creep.memory.upgrading:
        if creep.upgradeController(creep.room.controller) == ERR_NOT_IN_RANGE:
            creep.moveTo(creep.room.controller)
    else:

        #sources = []
        #structures = creep.room.find(FIND_STRUCTURES)
        #for structure in structures:
        #    if structure.structureType == STRUCTURE_CONTAINER:
        #        sources.append(structure)
        
        #if creep.withdraw(sources[0], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
        #    creep.moveTo(sources[0], {visualizePathStyle: {stroke: '#ffaa00'}})

        sources = creep.pos.findClosestByPath(FIND_DROPPED_RESOURCES)
        if creep.pickup(sources, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
            creep.moveTo(sources)