import numpy as np

import plt

x = np.random.randn(500)
plt.kdeplot(x)
plt.gca().set(title="日本語フォントも $pdf$ に埋め込まれます．")
plt.savefig("hoge.pdf")
plt.show()
