import numpy as np
import matplotlib.pyplot as plt

# Number of points and time steps
N = 100
T = np.linspace(0, 5, N)

# Parameters for the simulation
a = 2  # wave speed
CFL = 1  # CFL condition

# Create an empty array for the solution U
U = np.zeros((N, N))  # Use a 2D array to store solution at each time step

# Initialize U at t=0, set some initial condition, for example a sine wave
U[0, :] = np.sin(np.linspace(0, 2*np.pi, N))

# Loop over time steps to evolve the solution
for n in range(N-1):
    if a > 0:
        # Forward direction (positive wave speed)
        for i in range(1, N):
            U[n+1, i] = U[n, i] - CFL * (U[n, i] - U[n, i-1])
        # Apply periodic boundary condition (wraparound)
        U[n+1, 0] = U[n+1, N-1]
    else:
        # Backward direction (negative wave speed)
        for i in range(0, N-1):
            U[n+1, i] = U[n, i] - CFL * (U[n, i+1] - U[n, i])
        # Apply periodic boundary condition (wraparound)
        U[n+1, N-1] = U[n+1, 0]

# Plot the solution at different time steps

# Plot at t = 0 (initial condition)
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.plot(np.linspace(0, 2*np.pi, N), U[0, :], label='t = 0')
plt.title('t = 0')
plt.xlabel('x')
plt.ylabel('U(x, t)')

# Plot at halfway time
halfway_index = N // 2
plt.subplot(132)
plt.plot(np.linspace(0, 2*np.pi, N), U[halfway_index, :], label='t = halfway')
plt.title(f't = halfway (t={T[halfway_index]:.2f})')
plt.xlabel('x')
plt.ylabel('U(x, t)')

# Plot at final time
plt.subplot(133)
plt.plot(np.linspace(0, 2*np.pi, N), U[-1, :], label='t = final')
plt.title(f't = final (t={T[-1]:.2f})')
plt.xlabel('x')
plt.ylabel('U(x, t)')

plt.tight_layout()
plt.show()

# Plot moving animation
fig, ax = plt.subplots()
line, = ax.plot(np.linspace(0, 2*np.pi, N), U[0, :], label='U(x,t)')
ax.set_title("Wave Propagation")
ax.set_xlabel("x")
ax.set_ylabel("U(x,t)")
ax.set_ylim(-1.5, 1.5)  # Keep y-axis limits fixed for clarity

def update(frame):
    line.set_ydata(U[frame, :])  # Update the plot with data at time step frame
    ax.set_title(f"Wave Propagation at t = {T[frame]:.2f}")
    return line,

from matplotlib.animation import FuncAnimation

ani = FuncAnimation(fig, update, frames=range(N), interval=100, blit=True)
plt.show()
