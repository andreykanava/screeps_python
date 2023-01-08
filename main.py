import harvester
import upgrader
import miner
import miner2
import builder
import tower
import recharger

from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def main():
    if Game.cpu.bucket >= 10000:
        Game.cpu.generatePixel()
    
    hostiles = Game.spawns['Spawn1'].room.find(FIND_HOSTILE_CREEPS)
    
    if len(hostiles) > 0:
        tower.defend(Game.spawns["Spawn1"].room, 1)
    else:
        tower.heal(Game.spawns["Spawn1"].room)
    
    harvesters = []
    upgraders = []
    miners = []
    builders = []
    rechargers = []
    miners2 = []

    for creep in Game.creeps:
        if creep.memory.role == 'harvester':
            harvesters.append(creep)
            
        elif creep.memory.role == 'upgrader':
            upgraders.append(creep)
            
        elif creep.memory.role == 'miner':
            miners.append(creep)
        
        elif creep.memory.role == 'builder':
            builders.append(creep)
            
        elif creep.memory.role == 'recharger':
            rechargers.append(creep)
        
        elif creep.memory.role == 'miners2':
            miners2.append(creep)
            
    if len(harvesters) < 0:
        newName = "Harvester" + Game.time
        Game.spawns['Spawn1'].spawnCreep([WORK, MOVE, CARRY], newName, {memory: {role: 'harvester'}})
    
    if len(upgraders) < 0:
        newName = "Upgrader" + Game.time
        Game.spawns['Spawn1'].spawnCreep([WORK, MOVE, CARRY], newName, {memory: {role: 'upgrader'}})
    
    if len(miners) < 0:
        newName = "Miner" + Game.time
        Game.spawns['Spawn1'].spawnCreep([WORK, MOVE, WORK], newName, {memory: {role: 'miner'}})
    
    if len(miners2) < 0:
        newName = "Miner2" + Game.time
        Game.spawns['Spawn1'].spawnCreep([WORK, MOVE, WORK], newName, {memory: {role: 'miner2'}})
        
    if len(builders) < 0:
        newName = "Builder" + Game.time
        Game.spawns['Spawn1'].spawnCreep([WORK, MOVE, CARRY], newName, {memory: {role: 'builder'}})
        
    if len(rechargers) < 0:
        newName = "Recharger" + Game.time
        Game.spawns['Spawn1'].spawnCreep([WORK, MOVE, CARRY], newName, {memory: {role: 'recharger'}})
    
    for name in Game.creeps:
        creep = Game.creeps[name]
        
        if creep.memory.role == "harvester":
            harvester.run(creep)
        
        if creep.memory.role == "upgrader" and len(miners) > 0:
            upgrader.run(creep)
        
        if creep.memory.role == 'miner':
            miner.run(creep)
        
        if creep.memory.role == 'miner2':
            miner2.run(creep)
        
        if creep.memory.role == "builder" and len(miners) > 0:
            builder.run(creep)
            
        if creep.memory.role == 'recharger' and len(miners2) > 0:
            recharger.run(creep)