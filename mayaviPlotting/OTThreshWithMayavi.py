import numpy as np
from mayavi import mlab
import matplotlib.pyplot as py

crystal_positions = np.genfromtxt('CUORE_Crystal_Positions.txt',
                                  names=['Channel','X','Y','Z'], delimiter = ',')
#file that contains the low threshold channels to be plotted
#This line will need to be changed depending onn the file format and path
lowThresh_position= np.genfromtxt('/home/slp78/project/LowThreshStudy/ds3555/LowThres/LessThanSeven/run350191_ds3555_7.txt',
				  dtype=[('Channel','int'),('Thresh','f8')])


fig = mlab.figure(1,size=(600,600),fgcolor=(1,1,1),bgcolor=None)
mlab.clf()


all_indices = np.arange(crystal_positions['X'].size)
#Set hit indicies to the channels with low OT threshold
hit_indices=lowThresh_position['Channel']
#Shift by -1 due to  CUORE Crystal Positions txt file beginning at 0
hit_indices=hit_indices-1

#update miss indicies
miss_indices = np.delete(all_indices,hit_indices)

#plot miss indices
mlab.points3d(crystal_positions['X'][miss_indices],
              crystal_positions['Y'][miss_indices],
              crystal_positions['Z'][miss_indices],
              mode='cube',
              scale_factor=50,
              opacity=0.3,
              color=(1,1,1))
#plot hit indices
mlab.points3d(crystal_positions['X'][hit_indices],
              crystal_positions['Y'][hit_indices],
              crystal_positions['Z'][hit_indices],
              mode='cube',
              scale_factor=50,
              opacity=0.8,
              color=(1,0,0))

mlab.savefig(filename='SampleLowTCrystalArray.png')

        
