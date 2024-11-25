import numpy as np
import matplotlib.pyplot as plt
color1 = [40,120,60]
color2 = [60,50,90]

ax= plt.figure().add_subplot(projection='3d')

ax.scatter(xs=color1[0], ys= color1[1], zs=color1[2], zdir='z', label='color1')
ax.scatter(xs=color2[0], ys= color2[1], zs=color2[2], zdir='z', label='color2')

ax.scatter(0,0,0, zdir='z', label='origin', c='black')

ax.quiver(0,0,0,color1[0],color1[1],color1[2],color='black',arrow_length_ratio= 0.1)
ax.quiver(0,0,0,color2[0],color2[1],color2[2],color='black',arrow_length_ratio= 0.1)

ax.legend();
ax.set_xlim(0,150)
ax.set_ylim(0,150)
ax.set_zlim(0,150)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=20, azim=45, roll=0)

plt.show()  

#calculate the manhattan distance

L1 = [color1[i]-color2[i] for i in range(len(color1))]
l1= np.abs(L1).sum()
print('manhattan distance',l1)

#alternate approach 

a= np.array(color1)
print(a)
b= np.array(color2)

lal1 = np.linalg.norm((a-b), ord=1)
print('manhattan distance lal1',lal1)

#euclidian Distance
L2= [(color1[i]-color2[i])**2 for i in range(len(color1))]
L2= np.sqrt(np.array(L2).sum())
print(L2)

#alternate approach

print(np.linalg.norm((a-b),ord=2))

#cosine distnace

cosine = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
print(cosine)

#dot product 
dot= np.array([color1[i]*color2[i] for i in range(len(color1))]).sum()
print(dot)
