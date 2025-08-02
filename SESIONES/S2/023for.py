'''El programa lee un arreglo de número y se detiene la cantidad de 
segundos que indica el número leído 
'''

import time

for i in [5,1,4,6,3,2,1]:
    print(f'Habrá un retardo de {i} segundos ')
    time.sleep(i)
    