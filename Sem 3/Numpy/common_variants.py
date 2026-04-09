import numpy as np

temps = np.array([20,np.nan,24,22])

print(np.mean(temps),np.nanmean(temps))
print(np.argmax(temps),np.nanargmax(temps))
print(np.argmin(temps),np.nanargmin(temps))

