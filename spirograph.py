import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons


plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 5))
plt.axis('off')

ax.set_aspect('equal')
ax.set_xlim([-500, 500])
ax.set_ylim([-500, 500])

# Radius of the first circle, scales the whole image.
R = 40
# Ratio of the radius of the first circle to the second
k = 1
# Ratio of the radius of the first circle to the third
k2 = 2.01
# Distance to the drawing point
h = 40
# Ratio of the paths
p = 0.5

r = R/k
r2 = R/k2


# Length of the spiral
# High length can be difficult for the processor
len = 200
# If you see dots, decrease delta.
# Low delta can be difficult for the processor
delta = 0.001

t = np.arange(0, len, delta)

def hipo_draw(k, k2, h, p):
    r = R / k
    x = (R - r) * np.cos(t) + h * np.cos(t - R * t / r)
    y = (R - r) * np.sin(t) + h * np.sin(t - R * t / r)
    print('r = ', r, 'R = ', R, 'h = ', h)
    print('r = ', r, 'R = ', R, 'h = ', h)
    return x, y

def epi_draw(k, k2, h, p):
    r = R / k
    x = (R + r) * np.cos(t) - h * np.cos(t + R * t / r)
    y = (R + r) * np.sin(t) - h * np.sin(t + R * t / r)
    print('r = ', r, 'R = ', R, 'h = ', h)
    print('r = ', r, 'R = ', R, 'h = ', h)
    return x, y

def epi2_draw(k, k2, h, p):
    r = R / k
    r2 = R / k2
    #h = r2

    # x = (R + r) * np.cos(t) + (r + r2) * np.cos(-t) + h * np.cos(-t - r * t / r2)
    # y = (R + r) * np.sin(t) + (r + r2) * np.sin(-t) + h * np.sin(-t - r * t / r2)

    # x = (R + r) * np.cos(t) + (r + r2) * np.cos(t - t * R/r) + h * np.cos(t - t*R/r - t*R/r2)
    # y = (R + r) * np.sin(t) + (r + r2) * np.sin(t - t * R/r) + h * np.sin(t - t*R/r - t*R/r2)

    x = (R + r) * np.cos(t) + (r + r2) * np.cos(t + (R*t)/r - R*t/(p*r)) + h * np.cos(t + R*t/r - R*t/(p*r) - R*t/(p*r2))
    y = (R + r) * np.sin(t) + (r + r2) * np.sin(t + (R*t)/r - R*t/(p*r)) + h * np.sin(t + R*t/r - R*t/(p*r) - R*t/(p*r2))
    print('r = ', r, 'R = ', R, 'h = ', h)
    print('r = ', r, 'R = ', R, 'h = ', h)
    return x, y

def hipo2_draw(k, k2, h, p):
    r = R / k
    r2 = r / k2
    x = (R + r) * np.cos(t) - (r - r2) * np.cos(-t) + h * np.cos(t + r * t / r2)
    y = (R + r) * np.sin(t) - (r - r2) * np.sin(-t) + h * np.sin(t + r * t / r2)
    print(R, r, r2)
    return x, y


x, y = epi2_draw(k, k2, h, p)
sp2, = ax.plot(x, y, linewidth=0.5, color='red', antialiased=True)

def update(val):
    x, y = epi2_draw(k_slider.val,
                     k2_slider.val,
                     h_slider.val,
                     p_slider.val)

    sp2.set_xdata(x)
    sp2.set_ydata(y)
    fig.canvas.draw_idle()


# Sliders
h_ax = plt.axes([0.25, 0.07, 0.65, 0.01])
h_slider = Slider(h_ax,
                   'h',
                   valmin = 0,
                   valmax = 200.0,
                   valinit=h,
                   valstep=1)
h_slider.on_changed(update)

p_ax = plt.axes([0.25, 0.05, 0.65, 0.01])
p_slider = Slider(p_ax,
                   'p',
                   valmin = -5,
                   valmax = 10.0,
                   valinit=p,
                   valstep=0.01)
p_slider.on_changed(update)

k_ax = plt.axes([0.25, 0.03, 0.65, 0.01])
k_slider = Slider(k_ax,
                   'k',
                   valmin = 0,
                   valmax = 10.0,
                   valinit=k,
                   valstep=0.01)
k_slider.on_changed(update)

k2_ax = plt.axes([0.25, 0.01, 0.65, 0.01])
k2_slider = Slider(k2_ax,
                   'k2',
                   valmin = 0.1,
                   valmax = 10,
                   valinit=k2,
                   valstep=0.01)
k2_slider.on_changed(update)

plt.show()