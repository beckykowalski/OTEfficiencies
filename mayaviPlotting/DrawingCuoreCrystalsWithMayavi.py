import numpy as np
from mayavi import mlab
import matplotlib.pyplot as py


crystal_positions = np.genfromtxt('CUORE_Crystal_Positions.txt',
                                  names=['Channel','X','Y','Z'], delimiter = ',')

fig = mlab.figure(1,size=(600,600),fgcolor=(1,1,1),bgcolor=None)
mlab.clf()


all_indices = np.arange(crystal_positions['X'].size)
#generates 10 random channels
hit_indices = np.random.choice(all_indices,10)
miss_indices = np.delete(all_indices,hit_indices)

mlab.points3d(crystal_positions['X'][miss_indices],
              crystal_positions['Y'][miss_indices],
              crystal_positions['Z'][miss_indices],
              mode='cube',
              scale_factor=50,
              opacity=0.3,
              color=(1,1,1))

mlab.points3d(crystal_positions['X'][hit_indices],
              crystal_positions['Y'][hit_indices],
              crystal_positions['Z'][hit_indices],
              mode='cube',
              scale_factor=50,
              opacity=0.8,
              color=(1,0,0))

mlab.savefig(filename='SampleCuoreCrystalArray.png')

        
