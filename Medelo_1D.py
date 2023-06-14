# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:13:32 2022

@author: 
"""

import numpy as np
import matplotlib.pyplot as plt

#Parámetros 
niter=50
r=0.8
vretina=9.34e-4#cm/h
vvitre=0.127
vlens=0.164
vp=0.094
vscl=0.010
D=1

n=31
dt=1
dr=0.8/(n-1)
ci=0#concentración inicial nodos internos
cf=0#concentración inicial (derecho)
ci=10#concentración inicial izq 

#vectores
A=np.zeros(shape=(n,n))
B=np.zeros(n)
solution=np.zeros(shape=(n,niter+1))
tnodes=np.linspace(0,niter*dt,niter+1)
Tp=np.zeros(n)#Tiempo presente
Tf=np.zeros(n)#tiempo futuro

#condiciones iniciales:
#condiciones iniciales
Tp[1:n-1:1]=0
Tp[0]=7.11e-3#g/cm3
Tp[n-1]=0
solution[:,0]=Tp

for j in range(0,50,1):#Tiempo
    
    t=j
    
        
    
    #Izq
    for i in[0]:
         A[i,i]=1
         B[i]=(7.11e-3)-(7.11e-3*t/50)
         
     #Derecha

    for i in [n-1]:
         
         A[i,i]=1
         B[i]=0
         ########################internos#############
         
         #lens
    for i in[1,2,3,4,5,6,7,8,9]:
        
        A[i,i-1]=vlens/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vlens/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        #limit vitro
        
    for i in[10]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
      
        
        #vitreo
        
    for i in[11,12,13,14,15,16]:
        A[i,i-1]=vvitre/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vvitre/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
       
        
        
        #sclera
        
    for i in[17]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
        #sclera
        
    for i in[18,19,20,21,22,23]:
        A[i,i-1]=vscl/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vscl/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        
        B[i]=(-1/dt)*Tp[i]
        
        #retina
    for i in[24]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
        
    for i in[25,26,27,28,29]:
        A[i,i-1]=vretina/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vretina/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        
        B[i]=(-1/dt)*Tp[i]
        
    x=np.linalg.solve(A,B) 
    Tp=np.transpose(x)
    Tf=Tp
    solution[:,j+1]=Tf[:]




    xr=np.linspace(0,0.8,n)#11
   

    
        
plt.figure(6)



plt.plot(xr,solution[:,1],label='1hr')
plt.title("Difusividad 1cm^2/s")
# plt.plot(xr,solution[:,2],label='2hr')
# plt.plot(xr,solution[:,10],label='10hr')
plt.plot(xr,solution[:,3],label='3hr')
plt.plot(xr,solution[:,20],label='20hr')
plt.plot(xr,solution[:,50],label='50hr')
plt.ylabel("Concentración g/cm^3")
plt.xlabel("Distancia (cm)")
plt.legend(loc='upper right')

plt.figure(1)
plt.title("Análisis de las superficies en función del tiempo, D=1cm^2/s")
plt.plot(tnodes,solution[0,:],label="Lens")
plt.plot(tnodes,solution[10,:],label="Vitreous")
plt.plot(tnodes,solution[17,:],label="sclera")
plt.plot(tnodes,solution[24,:],label="retina")
plt.xlabel("Time(hr)")
plt.ylabel("Mean concentration g/cm")

  
plt.legend(loc='upper right') 

D=0.1

#vectores
A=np.zeros(shape=(n,n))
B=np.zeros(n)
solution=np.zeros(shape=(n,niter+1))
tnodes=np.linspace(0,niter*dt,niter+1)
Tp=np.zeros(n)#Tiempo presente
Tf=np.zeros(n)#tiempo futuro

#condiciones iniciales:
#condiciones iniciales
Tp[1:n-1:1]=0
Tp[0]=7.11e-3#g/cm3
Tp[n-1]=0
solution[:,0]=Tp

for j in range(0,50,1):#Tiempo
    
    t=j
    
        
    
    #Izq
    for i in[0]:
         A[i,i]=1
         B[i]=(7.11e-3)-(7.11e-3*t/50)
         
     #Derecha

    for i in [n-1]:
         
         A[i,i]=1
         B[i]=0
         ########################internos#############
         
         #lens
    for i in[1,2,3,4,5,6,7,8,9]:
        
        A[i,i-1]=vlens/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vlens/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        #limit vitro
        
    for i in[10]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
      
        
        #vitreo
        
    for i in[11,12,13,14,15,16]:
        A[i,i-1]=vvitre/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vvitre/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
       
        
        
        #sclera
        
    for i in[17]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
        #sclera
        
    for i in[18,19,20,21,22,23]:
        A[i,i-1]=vscl/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vscl/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        
        B[i]=(-1/dt)*Tp[i]
        
        #retina
    for i in[24]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
        
    for i in[25,26,27,28,29]:
        A[i,i-1]=vretina/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vretina/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        
        B[i]=(-1/dt)*Tp[i]
        
    x=np.linalg.solve(A,B) 
    Tp=np.transpose(x)
    Tf=Tp
    solution[:,j+1]=Tf[:]




    xr=np.linspace(0,0.8,n)#11
   

    
        
plt.figure(7)



plt.plot(xr,solution[:,1],label='1hr')
plt.title("Difusividad 0.1cm^2/s")
# plt.plot(xr,solution[:,2],label='2hr')
# plt.plot(xr,solution[:,10],label='10hr')
plt.plot(xr,solution[:,3],label='3hr')
plt.plot(xr,solution[:,20],label='20hr')
plt.plot(xr,solution[:,50],label='50hr')
plt.ylabel("Concentración g/cm^3")
plt.xlabel("Distancia (cm)")
plt.legend(loc='upper right')

plt.figure(2)
plt.title("Análisis de las superficies en función del tiempo , D=0.1cm^2/s")
plt.plot(tnodes,solution[0,:],label="Lens")
plt.plot(tnodes,solution[10,:],label="Vitreous")
plt.plot(tnodes,solution[17,:],label="sclera")
plt.plot(tnodes,solution[24,:],label="retina")
plt.xlabel("Time(hr)")
plt.ylabel("Mean concentration g/cm")

  
plt.legend(loc='upper right') 

D=0.001

#vectores
A=np.zeros(shape=(n,n))
B=np.zeros(n)
solution=np.zeros(shape=(n,niter+1))
tnodes=np.linspace(0,niter*dt,niter+1)
Tp=np.zeros(n)#Tiempo presente
Tf=np.zeros(n)#tiempo futuro

#condiciones iniciales:
#condiciones iniciales
Tp[1:n-1:1]=0
Tp[0]=7.11e-3#g/cm3
Tp[n-1]=0
solution[:,0]=Tp

for j in range(0,50,1):#Tiempo
    
    t=j
    
        
    
    #Izq
    for i in[0]:
         A[i,i]=1
         B[i]=(7.11e-3)-(7.11e-3*t/50)
         
     #Derecha

    for i in [n-1]:
         
         A[i,i]=1
         B[i]=0
         ########################internos#############
         
         #lens
    for i in[1,2,3,4,5,6,7,8,9]:
        
        A[i,i-1]=vlens/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vlens/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        #limit vitro
        
    for i in[10]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
      
        
        #vitreo
        
    for i in[11,12,13,14,15,16]:
        A[i,i-1]=vvitre/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vvitre/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
       
        
        
        #sclera
        
    for i in[17]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
        #sclera
        
    for i in[18,19,20,21,22,23]:
        A[i,i-1]=vscl/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vscl/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        
        B[i]=(-1/dt)*Tp[i]
        
        #retina
    for i in[24]:
        A[i,i-1]=vp/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vp/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        B[i]=(-1/dt)*Tp[i]
        
        
        
    for i in[25,26,27,28,29]:
        A[i,i-1]=vretina/(2*i*dr)+D/(i*dr**2)
        A[i,i+1]=-vretina/(2*i*dr)+D/(i*dr**2)
        A[i,i]=-1/(dt)-2*D/(i*dr**2)
        
        
        B[i]=(-1/dt)*Tp[i]
        
    x=np.linalg.solve(A,B) 
    Tp=np.transpose(x)
    Tf=Tp
    solution[:,j+1]=Tf[:]




    xr=np.linspace(0,0.8,n)#11
   

    
        
plt.figure(17)



plt.plot(xr,solution[:,1],label='1hr')
plt.title("Difusividad 0.001cm^2/s")
# plt.plot(xr,solution[:,2],label='2hr')
# plt.plot(xr,solution[:,10],label='10hr')
plt.plot(xr,solution[:,3],label='3hr')
plt.plot(xr,solution[:,20],label='20hr')
plt.plot(xr,solution[:,50],label='50hr')
plt.ylabel("Concentración g/cm^3")
plt.xlabel("Distancia (cm)")
plt.legend(loc='upper right')

plt.figure(12)
plt.title("Análisis de las superficies en función del tiempo , D=0.001cm^2/s")
plt.plot(tnodes,solution[0,:],label="Lens")

plt.plot(tnodes,solution[24,:],label="retina")
plt.xlabel("Time(hr)")
plt.ylabel("Mean concentration g/cm")

  
plt.legend(loc='upper right') 


        

  

