#### Import necessary libraries ####
import matplotlib.pyplot as plt  # Library for plotting
import numpy as np  # Library for numerical operations
from math import sqrt  # Importing sqrt function from math module

# Improve the aesthetics of the plots
plt.rc('font', family='serif', size=16)  # Set font style and size
plt.rc('lines', linewidth=1.5)  # Set line width for plots
plt.rc('legend', fontsize=12)  # Set legend font size

# Define the range of degrees of freedom and upstream Mach number
n = np.linspace(1, 7, 100)  # Range for degrees of freedom
M = np.linspace(1, 10, 100)  # Range for upstream Mach number

# Compute the ratio of specific heats (gamma) based on degrees of freedom
gamma = 1 + (2 / n)

# Function to compute thermodynamic properties across a normal shock
def compute_ratios(M, n):
    gamma = 1 + (2 / n)  # Compute gamma dynamically

    P_ratio = 1 + ((2 * gamma) / (gamma + 1)) * (M**2 - 1)  # P2/P1 (Pressure ratio)
    rho_ratio = ((gamma + 1) * M**2) / (2 + (gamma - 1) * M**2)  # rho2/rho1 (Density ratio)
    T_ratio = P_ratio / rho_ratio  # T2/T1 (Temperature ratio)
    a_ratio = 1 / np.sqrt(T_ratio)  # a2/a1 (Speed of sound ratio)
    M_ratio = a_ratio / rho_ratio  # M2/M1 (Mach number ratio)

    return P_ratio, rho_ratio, T_ratio, a_ratio, M_ratio

# Generate mesh grid for plotting
X, Y = np.meshgrid(M, n)  # Create 2D arrays of M and n
P2_P1, rho2_rho1, T2_T1, a2_a1, M2_M1 = compute_ratios(X, Y)  # Compute all ratios

# Create figure and subplots
fig = plt.figure(figsize=(18, 12))  

# Plot Pressure Ratio
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, P2_P1, cmap='plasma', alpha=0.9)
ax1.set_xlabel(r'$M_{1}$', fontsize=12)
ax1.set_ylabel(r'$n$', fontsize=12)
ax1.set_zlabel(r'$\frac{P_2}{P_1}$', fontsize=12)
ax1.set_title('Pressure Ratio')

# Plot Density Ratio
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, rho2_rho1, cmap='viridis', alpha=0.9)
ax2.set_xlabel(r'$M_{1}$', fontsize=12)
ax2.set_ylabel(r'$n$', fontsize=12)
ax2.set_zlabel(r'$\frac{\rho_2}{\rho_1}$', fontsize=12)
ax2.set_title('Density Ratio')

# Plot Temperature Ratio
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, T2_T1, cmap='magma', alpha=0.9)
ax3.set_xlabel(r'$M_{1}$', fontsize=12)
ax3.set_ylabel(r'$n$', fontsize=12)
ax3.set_zlabel(r'$\frac{T_2}{T_1}$', fontsize=12)
ax3.set_title('Temperature Ratio')

# Plot Speed of Sound Ratio
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, a2_a1, cmap='cividis', alpha=0.9)
ax4.set_xlabel(r'$M_{1}$', fontsize=12)
ax4.set_ylabel(r'$n$', fontsize=12)
ax4.set_zlabel(r'$\frac{a_2}{a_1}$', fontsize=12)
ax4.set_title('Speed of Sound Ratio')

# Plot Mach Number Ratio
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, Y, M2_M1, cmap='coolwarm', alpha=0.9)
ax5.set_xlabel(r'$M_{1}$', fontsize=12)
ax5.set_ylabel(r'$n$', fontsize=12)
ax5.set_zlabel(r'$\frac{M_2}{M_1}$', fontsize=12)
ax5.set_title('Mach Number Ratio')

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
