# Converting .mat file to .csv :


import scipy.io
import numpy as np
 
data = scipy.io.loadmat("B006.mat")
 
for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("Batt/"+i+".csv"),data[i],delimiter=',')
 
