import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

time_domain_1_2 = pd.DataFrame()

time_domain_1_2_1 = pd.read_csv("Образец 1 режим 2 скорость 1.txt", sep='\s+', skiprows=52, header=None, engine='python')
time_domain_1_2_10 = pd.read_csv("Образец 1 режим 2 скорость 10.txt", sep='\s+', skiprows=52, header=None, engine='python')
time_domain_1_2_25 = pd.read_csv("Образец 1 режим 2 скорость 25.txt", sep='\s+', skiprows=52, header=None, engine='python')

time_domain_1_2_1 = time_domain_1_2_1.drop(time_domain_1_2_1.index[:481],)
time_domain_1_2_1 = time_domain_1_2_1.drop(time_domain_1_2_1.index[5939 - 481:],)

time_domain_1_2_10 = time_domain_1_2_10.drop(time_domain_1_2_10.index[:1904])
time_domain_1_2_10 = time_domain_1_2_10.drop(time_domain_1_2_10.index[7444 - 1904:])

time_domain_1_2_25 = time_domain_1_2_25.drop(time_domain_1_2_25.index[:384])
time_domain_1_2_25 = time_domain_1_2_25.drop(time_domain_1_2_25.index[5969 - 384:])

time_domain_1_2_1 = time_domain_1_2_1.reset_index()
time_domain_1_2_1.drop('index', axis=1, inplace = True)

time_domain_1_2_10 = time_domain_1_2_10.reset_index()
time_domain_1_2_10.drop('index', axis=1, inplace = True)

time_domain_1_2_25 = time_domain_1_2_25.reset_index()
time_domain_1_2_25.drop('index', axis=1, inplace = True)

time_domain_1_2 = pd.concat([time_domain_1_2_1, time_domain_1_2_10, time_domain_1_2_25], axis=1, join='outer', ignore_index=True)

fig, ax = plt.subplots(3, 1, sharex=True, sharey=True, figsize=[11, 9])

fig.suptitle('Образец 1, MODE = 2', fontsize=19, fontweight='bold')

# subplot is created
ax[0].plot( time_domain_1_2.index / 1024, time_domain_1_2[1], 'b-')
ax[0].set_title('Speed = 1', fontsize=15)
ax[0].set_ylabel('Амплитуда, g')
ax[0].grid(True)


ax[1].plot( time_domain_1_2.index / 1024, time_domain_1_2[3], 'b-')
ax[1].set_title('Speed = 10', fontsize=15)
ax[1].set_ylabel('Амплитуда, g')
ax[1].grid(True)

ax[2].plot( time_domain_1_2.index / 1024, time_domain_1_2[5], 'b-')
ax[2].set_title('Speed = 25', fontsize=15)
ax[2].set_ylabel('Амплитуда, g')
ax[2].set_xlabel('Время, с')
ax[2].grid(True)
plt.xlim(0, 1.5)


plt.show()

plt.show()