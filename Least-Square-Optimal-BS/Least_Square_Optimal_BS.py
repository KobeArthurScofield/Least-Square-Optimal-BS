# Least Square Optimal
# Kobe Arthur Scofield
# 2018-04-27
# Build 2
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.7

print("Loading main libraries.")
import numpy as np
import matplotlib.pyplot as mtpl
from scipy.optimize import leastsq
print("Libraries loaded.")

# Inilitize all data
x = np.linspace(-4, 4, 1001)                            # Data foe optimal line
X = np.array([0., 1., 2., 3., -1., -2., -3.])           # Origin X data
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])     # Origin Y data

# This function contains the function for optimize
def f(p, X):
    a, b, c = p
    return (Y - (a * (X**2) + b * X + c))

r = leastsq(f, [0., 0., 0.], X)
a, b, c = r[0]
print("a=",a,"b=",b,"c=",c)

mtpl.scatter(X, Y, s=100, alpha=1.0, marker='o',label=u'Data')

y= a * (x**2) + b * x + c

ax = mtpl.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

mtpl.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'Optimized')

mtpl.legend(loc=0, numpoints=1)
leg = mtpl.gca().get_legend()
ltext  = leg.get_texts()
mtpl.setp(ltext, fontsize='xx-large')

mtpl.xlabel("X")
mtpl.ylabel("Y")

xrange = x.max() - x.min()
yrange = y.max() - y.min()
mtpl.xlim(x.min() - xrange * 0.2, x.max() + xrange * 0.2)
mtpl.ylim(y.min() - yrange * 0.2, y.max() + yrange * 0.2)

mtpl.xticks(fontsize=20)
mtpl.yticks(fontsize=20)
#刻度字体大小
mtpl.legend(loc='upper left')

mtpl.show()
