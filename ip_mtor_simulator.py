import numpy as np


class InvertedPudulemSimulator:
    def __init__(self):
        print('Initialize Inverted Pendulum Simulator')
        self.M = 10
        self.m = 10
        self.l = 0.25
        self.g = 9.8
        self.Ip = self.m * self.l * self.l / 12
        self.Im = 5
        self.K = 0.02
        self.R = 0.5
        self.L = 0.0005
        self.r = 0.1
        self.Kp = 700
        self.Kv = 20
        self.tfinal = 2
        self.dt = 0.001

        self.c_1 = (self.m * self.l) / (self.M + self.m) - (
                self.Ip + self.m * np.math.pow(self.l, 2) / (self.m * self.l))
        self.c_2 = (self.M + self.m) / (self.m * self.l) - (self.m * self.l) / (
                self.Ip + self.m * np.math.pow(self.l, 2))

        self.a_21 = -self.g / self.c_1
        self.a_41 = -self.m * self.g * self.l / (self.Ip + self.m * np.math.pow(self.l, 2) * self.c_2)

    def run_simulation(self, tfinal: float, dt: float):
        self.dt = dt
        self.tfinal = tfinal
        n = self.tfinal / self.dt

        A = np.array([[0, 1, 0, 0], [self.a_21, 0, 0, 0], [0.0, 0.0, 0.0, 1.0], [self.a_41, 0.0, 0.0, 0.0]])
        B = np.array([[0], [1 / ((self.M + self.m) * self.c_1)], [0], [1 / (self.m * self.l * self.c_2)]])
        C = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

        Am = np.array([[0, 1, 0], [0, 0, self.K / self.Im], [0, -self.K / self.L, -self.R / self.L]])
        Bm = np.array([[0], [0], [1 / self.L]])
        Cm = np.array([0, 0, self.K / self.r])

        x0 = np.array([[0.017453], [0], [0], [0]])
        xm0 = np.array([[0], [0], [0]])

        x = x0
        xm = xm0

        steps: int = int(n)
        x_path = np.zeros(steps, dtype=float)
        t_angle = np.zeros(steps, dtype=float)

        k = 0
        while k < n:
            v = self.Kp * x[0] + self.Kv * x[1]
            # v = min(v, 12)

            dxm = np.dot(Am, xm) + Bm * v
            xm = np.dot(dxm, dt) + xm
            f = np.dot(Cm, xm)

            dx = np.dot(A, x) + B * f
            x = np.dot(dx, dt) + x

            t_angle[k] = x[0]
            x_path[k] = x[2]

            k += 1

        return x_path, t_angle
