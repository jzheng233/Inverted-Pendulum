from ip_mtor_simulator import InvertedPudulemSimulator

simulator = InvertedPudulemSimulator()

tfinal: float = 2
dt: float = 0.001

[x_path, t_angle] = simulator.run_simulation(tfinal, dt)

print(x_path)
print(t_angle)
