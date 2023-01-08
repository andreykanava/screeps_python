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
    if creep.memory.building and creep.store[RESOURCE_ENERGY] ==0:
        creep.memory.building = False
    
    
    if not creep.memory.building and creep.store.getFreeCapacity() ==0:
        creep.memory.building = True
        
        
    if creep.memory.building:
        targets = creep.room.find(FIND_CONSTRUCTION_SITES)
        if len(targets) > 0:
            if creep.build(targets[0]) == ERR_NOT_IN_RANGE:
                creep.moveTo(targets[0])
    else:
        sources = creep.room.find(FIND_DROPPED_RESOURCES)
        if creep.pickup(sources[0], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
            creep.moveTo(sources[0])
