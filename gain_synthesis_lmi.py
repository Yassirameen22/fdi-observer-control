
import cvxpy as cp
import numpy as np

def synthesize_observer_gain(A, C, gamma=1e-3):
    n = A.shape[0]
    p = C.shape[0]

    P = cp.Variable((n, n), symmetric=True)
    Y = cp.Variable((n, p))

    constraints = [P >> gamma * np.eye(n)]

    Acl = A - Y @ C
    constraints += [Acl.T @ P @ Acl - P << -gamma * np.eye(n)]

    prob = cp.Problem(cp.Minimize(0), constraints)
    prob.solve()

    if prob.status != cp.OPTIMAL:
        raise ValueError("LMI optimization did not converge.")

    return Y.value @ np.linalg.inv(P.value)
