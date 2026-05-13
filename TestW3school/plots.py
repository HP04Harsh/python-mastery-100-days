'''import matplotlib.pyplot as plt 
import numpy as np 
x = np.array([1,5])
y = np.array([2,7])

plt.subplot(1,1,1)
plt.plot(x,y,'o:r',linestyle='dotted')

plt.subplot(1,2,2)
plt.plot(x,y,'o:r',linestyle='dotted')

plt.xlabel('Birth Average')
plt.ylabel('Mortality Rate')
plt.show()'''

import matplotlib.pyplot as plt
import numpy as np
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

y = np.array([35, 25, 25, 15])

plt.pie(y,labels=mylabels, explode = myexplode,shadow = True)
plt.show()