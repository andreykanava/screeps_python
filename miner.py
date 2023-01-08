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
    creep_source = creep.room.find(FIND_SOURCES)
    if creep.store[RESOURCE_ENERGY] == 0:
        if creep.harvest(creep_source[0]) == ERR_NOT_IN_RANGE:
            creep.moveTo(creep_source[0], {visualizePathStyle: {stroke: '#ffffff'}})
    else:
        creep.drop(RESOURCE_ENERGY)
