"""
Cargando imagenes desde una carpeta y convirtiendo a escala de grises,
se almacenan las imagenes de 176x144=25344px en un vector.
Se realiza el mismo procedimiento para las 21 letras, se concatenan
y al final se obtiene una matriz de 10500x25344
@author: estevez
"""
import numpy as np
from PIL import Image
import glob

#abecedario = ['A']
abecedario = ['A','B','C','D','E','F','G','H','I','L','M','N','O','P','R','S','T','U','V','W','Y']
#data = np.zeros(shape=(1,25344))
data = np.arange(6336)
data = np.reshape(data,(1,6336))
for j in abecedario:
    #Almacenando las imagenes en una lista
    image_list = []
    for filename in glob.glob('/home/estevez/Documentos/Programas Python/dataTesis/{}/*.jpg'.format(j)): 
        im=Image.open(filename)
        image_list.append(im)

    #Convirtiendo a escala de grises
    data_gray = []
    for i in np.arange(500):
        gray = image_list[i].convert('L').resize((88,72), Image.ANTIALIAS)
        data_gray.append(gray)
    
    #Guargando en una carpeta las imagenes grises y comprimiendo
    #for i in np.arange(500):
    #    data_gray[i].save('{}_gray/{}_{}.jpg'.format(j,j,i),optimize=True,quality=50)
    
    #Guardando imagen como array numpy
    img=np.array(data_gray[0])
    vector=img.reshape(1,6336)
        
    for i in np.arange(1,500):
        img=np.array(data_gray[i])
        img=img.reshape(1,6336) #aplanando el vector
        vector=np.vstack((vector,img))    #Queda guardado el vector de n elementos x 25344
    
    data=np.vstack((data,vector)) 

# Guardando las imagenes en un .csv
#data=np.delete(data,0,0)    #Eliminando el primer renglón de ceros
data=data.astype(int)   #Pasando de float64 a int    
np.savetxt("LSM_reduced.csv", data, delimiter=",")




# Cambiando escala de la imagen guardando la relacion de aspecto
# dado los pixeles de la base
#basewidth = 88 #mitad de 176, 88x72 (imagen con la mitad de px)
#img = Image.open('W_2.jpg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#img.save('sompic.jpg') 









