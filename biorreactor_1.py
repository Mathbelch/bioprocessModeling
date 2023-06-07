import numpy as np # to work with matrix
from matplotlib import pyplot as plt; # to work with graphs

total_time = 120 #hours (according to experimental data)
h = 0.01 #hour - timeStep
n = int(total_time/h) # number of points

# Creating matrix of size 'n' filled with 0 for Biomass, Substrate and Product:
B = np.zeros(n)
S = np.zeros(n)
P = np.zeros(n)

# Creating time matrix from 0 to 'total_time', variyng 'h':
t = np.arange(0, total_time, h)

# Setting initial conditions:
B[0] = 0.01 #billions of cells/mL (inoculum)
S[0] = 10 #g/L
P[0] = 0

# Setting parameters values:
u_max = 0.7
km = 60
yp = 4
ys = 0.38

# Solving model through finite difference method:
for i in range(n-1):
   
   B[i+1] = B[i] + h * ((u_max * S[i] * B[i]) / (km + S[i]))
   
   S[i+1] = S[i] - (1/ys) * h * ((u_max * S[i] * B[i]) / (km + S[i]))
   
   P[i+1] = P[i] + (1/yp) * h * ((u_max * S[i] * B[i]) / (km + S[i]))
   
# Plotting graph:
plt.figure(figsize=(16,8))
plt.plot(t,B)
plt.plot(t,P)
plt.plot(t,S)
plt.xlabel('Time [h])')
plt.ylabel('Cell [bil/mL]')

experimental_data = np.loadtxt('trichoderma_reesei_data.txt') # time X B (basis article makes modeling only with biomass)

plt.plot(experimental_data[:,0], experimental_data[:,1], 'bo')

plt.show()
   