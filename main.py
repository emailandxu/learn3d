import numpy as np
import meshplot as mp

data = np.load('data.npz')
v, f, n, fs = data["v"], data["f"], data["n"], data["fs"]
v1, f1, v2, f2 = data["v1"], data["f1"], data["v2"], data["f2"]

mp.plot(v, f)
