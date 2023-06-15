"""
This file could contain the necessary calls to make plots etc for 
case 3

"""
import sys
sys.path.append('../')
import os
import time
from lorenz import *

sys.path.append('../')
directory = "../result/case3/"

# Create a directory for this case in case it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Initializing objects for file handler and plotter classes
file_handler = filehandling.OdeFileHandler(directory)
plotter = plot.OdePlotter("Case 3")

print("Initiated Case # 3 ...\n")

sol = solver.OdeSolver(10, 8 / 3, 28)
n = 10000
t = 0.02
print("N: " + str(n) + ", Time Interval: " + str(t) + ", and x , y, z = 1")
sol.set_num_of_steps(n)
sol.set_time_interval(t)

print("Simulating...")
st = time.time()
result = sol.simulator(1, 1, 1)
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Writing...")
st = time.time()
file_handler.ode_solver_writer(sol.to_string(), "ode_solver.txt")
file_handler.ode_data_writer(result, "ode_result.txt")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 3D...")
st = time.time()
plot_color = plotter.three_d_plot_color(result)
file_handler.ode_plot_figure_saver(plot_color, "plot_3d_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 2D - xy...")
st = time.time()
plot_color = plotter.two_d_plot_color(result, "xy")
file_handler.ode_plot_figure_saver(plot_color, "plot_2d_xy_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 2D - xz...")
st = time.time()
plot_color = plotter.two_d_plot_color(result, "xz")
file_handler.ode_plot_figure_saver(plot_color, "plot_2d_xz_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 2D - yz...")
st = time.time()
plot_color = plotter.two_d_plot_color(result, "yz")
file_handler.ode_plot_figure_saver(plot_color, "plot_2d_yz_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))