from netpyne import specs

cfg = specs.SimConfig()

cfg.duration = 1*1e3       # Duration of the simulation, in ms
cfg.dt = 0.025              # Internal integration timestep to use
cfg.verbose = False         # Show detailed messages
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
cfg.recordStep = 0.1        # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'output'       # Set file output name
cfg.saveJson = True
cfg.printPopAvgRates = True

cfg.analysis['plotRaster'] = {'saveFig': True}                   # Plot a raster
cfg.analysis['plotTraces'] = {'include': [0], 'saveFig': True}  # Plot recorded traces for this list of cells
cfg.analysis['plot2Dnet'] = {'saveFig': True} 
cfg.analysis['plotConn'] = {'saveFig': True}

cfg.saveDataInclude = ['simData', 'simConfig', 'netParams', 'net']

# Parameters that go into NetParams.py
#Population Paramters
cfg.P1_pop = 20
cfg.P2_pop = 20
cfg.P3_pop = 20
cfg.G_pop = 15

# Connection Parameters

cfg.prob1 = .8
cfg.prob2 = .5


cfg.prob_G_0 = .5
cfg.prob_G_1 = .5
cfg.prob_G_2 = .5