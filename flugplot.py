################################# import packages/libraries

import os, sys, subprocess, ConfigParser,time, string
import numpy as np
import scipy as scipy
import datetime 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import PCA

def ableitung(x,y):
        dev=np.empty([y.shape[0],2])
        for i in range(y.shape[0]-1):
                a=float(y[i+1]-y[i])
                b=float(x[i+1]-x[i])
                dev[i,1]=a/b
                dev[i,0]=x[i]
        return dev

def flugroute(datum_list):
	for datum in datum_list:
		start=time.clock()
		data=np.genfromtxt("../txt/"+datum+"_data.txt",skip_header=1,usecols=(45,46,47,3,48))
		dat=[]
		try:
			for i in range(data.shape[0]):
				if np.isnan(np.max(data[i,:]))==False:dat.append(data[i,:])
			dat=np.array(dat)

			fig = plt.figure()
			ax = fig.gca(projection='3d')

			for i in range(dat.shape[0]): 
				if dat[i,3]>0:dat[i,4],dat[i,3]=dat[i,4]/dat[i,3]*100,np.log(dat[i,3])
				else: dat[i,4],dat[i,3]=0,0
			print dat[:,3]
			y2=dat[:,3]
			dicke=(y2-np.nanmin(y2))/(np.nanmax(y2)-np.nanmin(y2))*200

			sc = ax.scatter(dat[:,0],dat[:,1],dat[:,2],c=dat[:,4],vmin=0, vmax=25,s=dicke,alpha=0.3, edgecolors='none')
			ax.invert_zaxis()
			ax.set_xlabel("latitude")
			ax.set_ylabel("longitude")
			ax.set_zlabel("altitude")
			cbar = plt.colorbar(sc)
			plt.savefig("../plots/"+datum+"_flugroute_3D.png")

			fig = plt.figure()
			ax = fig.gca()
			sc = ax.scatter(dat[:,0],dat[:,1],c=dat[:,2],s=dicke,alpha=0.3, edgecolors='none')
			cbar = plt.colorbar(sc)
			plt.savefig("../plots/"+datum+"_flugroute.png")
			print datum, 'flugroute geplottet in %d s'%(time.clock()-start)
		except: print "data incomplete"
	

#flugroute(["20140708"])
