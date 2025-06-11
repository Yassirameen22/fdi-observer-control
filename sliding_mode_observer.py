
import numpy as np

class SlidingModeObserver:
    def __init__(self, A, B, C, L, rho=0.01):
        self.A = A
        self.B = B
        self.C = C
        self.L = L
        self.rho = rho
        self.n = A.shape[0]
        self.x_hat = np.zeros((self.n,))

    def reset(self):
        self.x_hat = np.zeros_like(self.x_hat)

    def update(self, y, u):
        y_pred = self.C @ self.x_hat
        s = y - y_pred
        correction = self.L @ s + self.rho * np.sign(s)
        self.x_hat = self.A @ self.x_hat + self.B @ u + correction
        return self.x_hat.copy()
