# PhD-Python-1
A repository contains a project for the PhD
course "Scientific Computing using Python, part 1", held 
at Aalborg University, most recently in June 2023

#  
- Author: Ikhtiyor Nematov, Computer Science Department Aalborg University

Code Modules: The project’s source code consists of the following modules:
(1) lorenz: This module contains five files: init, filehandling, solver, plot, and testing. The solver file
implements Algorithm 1 and provides getter and setter methods for the required parameters.
It also includes methods to compute the values of 𝑥, 𝑦, and 𝑧 using the given equations, as well
as a method to retrieve the class configuration as a string. The plot file includes methods for
plotting 2D and 3D plots in color format. The filehandling file contains methods for writing
the configuration and the (𝑥, 𝑦, 𝑧) values to files. The testing file includes test methods to
verify the functionality of the solver class using the Unittest library.
#
(2) cases: This module includes separate files for each test case. These files execute the ODE
solver with different configurations, plot the results, and save the configurations.
#
(3) result directory: This directory contains folders to store the resultant files for each test case
