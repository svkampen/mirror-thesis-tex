from matplotlib import pyplot as plt
import numpy as np

plt.xlabel("$T_2$ / $T_1$")
plt.ylabel(r"$U_{ub}$")
plt.ylim(0.5, 1)
plt.xticks(range(1, 11))

def U(F, k):
    return (k - 2*F + (F * (F + 1))/k)

k = np.linspace(1, 10, 1000)
F = np.floor(k)
Us = U(F, k)

plt.plot(k, Us)
plt.savefig("ub_rm_2tasks.eps")
