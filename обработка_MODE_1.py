import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csvframe = pd.read_csv('Образец 3 измерение 1_результаты.csv', skiprows=2)


# plt.figure(1)

csvframe.plot( y=1, style=".-", grid=True, label='Образец 3 MODE 1', xlabel='Speed', ylabel='Частота, Гц')


csvframe.plot( y=2, style=".-", grid=True, label='Образец 3 MODE 1', xlabel='Speed', ylabel='Амплитуда, g')
plt.ylim(0, 5)
plt.show()