import pickle
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import font_manager


my_font = font_manager.FontProperties(
    fname=r"c:/Windows/Fonts/simhei.ttf")
f = open("./sse.pkl", "rb")
SSE = pickle.load(f)
f.close()
plt.plot(range(1, 9), SSE, marker="o")
plt.xlabel("K值——簇数量", fontproperties=my_font, size=20)
plt.ylabel("簇内误方差SSE", fontproperties=my_font, size=20)
plt.show()
