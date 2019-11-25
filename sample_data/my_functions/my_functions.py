import numpy as np

def test(x, K):
	return np.exp(-K * x /50) * np.sin(x)
