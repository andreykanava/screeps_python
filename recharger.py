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
    if creep.memory.recharging and creep.store[RESOURCE_ENERGY] == 0:
        creep.memory.recharging = False
    
    if not creep.memory.recharging and creep.store.getFreeCapacity() == 0:
        creep.memory.recharging = True

    if creep.memory.recharging:

        targets = []
        structures = creep.room.find(FIND_STRUCTURES)
        for structure in structures:
            if structure.structureType == STRUCTURE_EXTENSION or structure.structureType == STRUCTURE_SPAWN and structure.store.getFreeCapacity(RESOURCE_ENERGY) > 0:
                targets.append(structure)
        
        if len(targets) > 0:
            if creep.transfer(targets[0], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                creep.moveTo(targets[0])
        
        else:
            
            sources = []
            structures = creep.room.find(FIND_STRUCTURES)
            for structure in structures:
                if structure.structureType == STRUCTURE_CONTAINER:
                    sources.append(structure)
            
            if creep.withdraw(sources[1], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                creep.moveTo(sources[1])

            