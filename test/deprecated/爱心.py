from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# x = np.linspace(-10, 10, 100)
# y = pow(np.sin(x), 3) * 16
#
# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, y)
# plt.show()

df = pd.DataFrame({
    "c": ['1231231', "32135512", '213123', "暂无"]
})

print(df[df["c"] != "暂无"])

