import matplotlib as mpl
import matplotlib.pyplot as plt

color=['#CC0000','#FF3300','#FF6600','#FF6633','#FF9966','#FFCC99','#FFFF00','#FFFF33','#FFFF66','#FFFF99','#FFCC66','#FFFF00',
       '#66FF66','#99FF99','#CCFFCC','#009999','#00CCCC','#66CCCC','#66FFCC','#99FFCC','#0099FF','#00CCFF','#00FFFF','#99FFFF','#CCFFFF',
       '#0000CC','#0000FF','#3366FF','#3399FF','#66CCFF','#99CCFF','#330066','#660099','#663399','#9900CC','#9966FF']

n= len(color)-1
def C(color,x):
        return color[x]

fig, ax = plt.subplots(nrows=1,ncols=1)
for x in range(n+1):
    ax.axvline(x, color=C(color,x), linewidth=20)
    ax.set_aspect('equal')
ax.set_axis_off()
plt.show()
plt.subplots_adjust(left=0,right=0.0445,wspace=0.4,hspace=0)