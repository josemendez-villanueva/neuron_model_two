from neuron import specs, sim

netParams = specs.NetParams()
cfg = specs.SimConfig()

# Defining the space of the network
netParams.sizeX = 100
netParams.sizeY = 1000
netParams.sizeZ = 100

# Creating the populations

netParams.popParams['P1'] = {'cellType': 'PYR', 'numCells': cfg.P1_pop,'yRange': [100, 300]}
netParams.popParams['P2'] = {'cellType': 'PYR', 'numCells': cfg.P2_pop, 'yRange': [250, 700]}
netParams.popParams['P3'] = {'cellType': 'PYR', 'numCells': cfg.P3_pop, 'yRange': [600, 900]}
netParams.popParams['Golgi'] = {'cellModel': 'GoC_Solinas','cellType': 'GoC', 'numCells': cfg.G_pop, 'yRange': [100, 900]}

# Importing of the morphology

CellRule = netParams.importCellParams(
        label='Golgi_Cell_Rules',
        conds= {'cellType': 'GoC', 'cellModel': 'GoC_Solinas'},
        fileName='mod/Golgi_template.hoc',
        cellName='Goc')


#For simplicity purposes will be creating a dummy pyramidal cell (Not of Golgi type) in order to first test a few things

netParams.cellParams['PYR'] = {
    'secs': {'soma':
            {'geom': {'diam': 18.8, 'L': 18.8, 'Ra': 123.0},
            'mechs': {'hh': {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}}}},
            'dend':
            {'geom': {'diam': 5.0, 'L': 150.0, 'Ra': 150.0, 'cm': 1},
            'mechs': {'pas': {'g': 0.0000357, 'e': 0}}}}


#Create Stimulation (VClamp)

netParams.stimSourceParams['Input_1'] = {'type': 'VClamp', 'dur': [0, 50, 100], 'amp': [-60, -30, 40], 'gain': 1e5, 'rstim': 1, 'tau1': 0.1, 'tau2': 0}
netParams.stimTargetParams['Input_1->P1'] = {'source': 'Input_1', 'sec':'soma', 'loc': 0.8, 'conds': {'pop':'P1'}}

#Create Background Noise as well since it should be present
netParams.stimSourceParams['background'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.8}
netParams.stimTargetParams['background->Pop'] = {'source': 'background', 'conds': {'cellType': 'PYR'}, 'weight': 0.03, 'delay': 10, 'synMech': 'exc'}

#Connections


netParams.connParams['P1->P2'] = { 
        'preConds': {'pop': 'P1'},    # presynaptic conditions
        'postConds': {'pop': 'P2'},   # postsynaptic conditions
        'probability': cfg.prob1,     # probability of connection
        'weight': 0.01,               # synaptic weight
        'delay': 5,                   # transmission delay (ms)
        'sec': 'dend',                # section to connect to
        'loc': 1.0,                   # location of synapse
        'synMech': 'exc'}             # target synaptic mechanism

netParams.connParams['P2->P3'] = { 
        'preConds': {'pop': 'P2'},     
        'postConds': {'pop': 'P3'},  
        'probability': cfg.prob2,           
        'weight': 0.01,           
        'delay': 5,               
        'sec': 'dend',              
        'loc': 1.0,                  
        'synMech': 'exc'}       

netParams.connParams['P1->Golgi'] = { 
        'preConds': {'pop': 'P2'},     
        'postConds': {'pop': 'Golgi'},  
        'probability': cfg.prob_G_0,           
        'weight': 0.01,           
        'delay': 5,               
        'sec': 'dend_0',              
        'loc': 1.0,                  
        'synMech': 'exc'} 

netParams.connParams['P2->Golgi'] = { 
        'preConds': {'pop': 'P2'},     
        'postConds': {'pop': 'Golgi'},  
        'probability': cfg.prob_G_1,           
        'weight': 0.01,           
        'delay': 5,               
        'sec': 'dend_1',              
        'loc': 1.0,                  
        'synMech': 'exc'} 

netParams.connParams['P2->Golgi'] = { 
        'preConds': {'pop': 'P2'},     
        'postConds': {'pop': 'Golgi'},  
        'probability': cfg.prob_G_2,           
        'weight': 0.01,           
        'delay': 5,               
        'sec': 'dend_2',              
        'loc': 1.0,                  
        'synMech': 'exc'} 

netParams.connParams['Golgi->Golgi'] = { 
        'preConds': {'pop': 'Golgi'},     
        'postConds': {'pop': 'Golgi'},  
        'probability': .4,           
        'weight': 0.01,           
        'delay': 5,               
        'sec': 'dend_0',              
        'loc': 1.0,                  
        'synMech': 'exc'} 