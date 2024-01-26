import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

time_domain_1_3 = pd.DataFrame()

time_domain_1_3_1 = pd.read_csv("Образец 1 режим 3 скорость 1.txt", sep='\s+', skiprows=52, header=None, engine='python')
time_domain_1_3_10 = pd.read_csv("Образец 1 режим 3 скорость 10.txt", sep='\s+', skiprows=52, header=None, engine='python')
time_domain_1_3_25 = pd.read_csv("Образец 1 режим 3 скорость 25.txt", sep='\s+', skiprows=52, header=None, engine='python')

time_domain_1_3_1 = time_domain_1_3_1.drop(time_domain_1_3_1.index[:61],)
time_domain_1_3_1 = time_domain_1_3_1.drop(time_domain_1_3_1.index[1377 - 61:],)

time_domain_1_3_10 = time_domain_1_3_10.drop(time_domain_1_3_10.index[:200])
time_domain_1_3_10 = time_domain_1_3_10.drop(time_domain_1_3_10.index[1516 - 200:])

time_domain_1_3_25 = time_domain_1_3_25.drop(time_domain_1_3_25.index[:440])
time_domain_1_3_25 = time_domain_1_3_25.drop(time_domain_1_3_25.index[1756 - 440:])

time_domain_1_3_1 = time_domain_1_3_1.reset_index()
time_domain_1_3_1.drop('index', axis=1, inplace = True)


time_domain_1_3_10 = time_domain_1_3_10.reset_index()
time_domain_1_3_10.drop('index', axis=1, inplace = True)

time_domain_1_3_25 = time_domain_1_3_25.reset_index()
time_domain_1_3_25.drop('index', axis=1, inplace = True)

time_domain_1_3 = pd.concat([time_domain_1_3_1, time_domain_1_3_10, time_domain_1_3_25], axis=1, join='outer', ignore_index=True)

fig, ax = plt.subplots(3, 1, sharex=True, sharey=True, figsize=[11, 9])

fig.suptitle('Образец 1, MODE = 3', fontsize=19, fontweight='bold')

# subplot is created

ax[0].plot( time_domain_1_3.index / 1024, time_domain_1_3[1], 'b-')
ax[0].set_title('Speed = 1', fontsize=15)
ax[0].set_ylabel('Амплитуда, g')
ax[0].grid(True)


ax[1].plot( time_domain_1_3.index / 1024, time_domain_1_3[3], 'b-')
ax[1].set_title('Speed = 10', fontsize=15)
ax[1].set_ylabel('Амплитуда, g')
ax[1].grid(True)

ax[2].plot( time_domain_1_3.index / 1024, time_domain_1_3[5], 'b-')
ax[2].set_title('Speed = 25', fontsize=15)
ax[2].set_ylabel('Амплитуда, g')
ax[2].set_xlabel('Время, с')
ax[2].grid(True)
# plt.xlim(0, 1.5)


plt.show()

plt.show()