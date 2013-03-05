"""
Extreme deconvolution of stars
==============================

The (very simple) model that transformed SDSS-III.

"""

from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

# Instantiate the PGM.
pgm = daft.PGM([3.2, 3.55], origin=[-0.6, 0.3])

# Hierarchical parameters.
pgm.add_node(daft.Node("alpha", r"$\alpha$", 1, 3.5, fixed=True))
pgm.add_node(daft.Node("theta", r"$\theta$", 1, 2.5))
pgm.add_node(daft.Node("sigma", r"$\Sigma$", 1, 1))

# Latent variables.
pgm.add_node(daft.Node("q", r"$q_n$", 2, 3))
pgm.add_node(daft.Node("qt", r"$q_m$", 0, 3))
pgm.add_node(daft.Node("X", r"$X_n$", 2, 2))
pgm.add_node(daft.Node("Xt", r"$X_m$", 0, 3))

# Data.
pgm.add_node(daft.Node("x", r"$x_n$", 2, 1, observed=True))
pgm.add_node(daft.Node("x", r"$x_n$", 0, 1, observed=True))

# Add in the edges.
pgm.add_edge("alpha", "theta")
pgm.add_edge("theta", "X")
pgm.add_edge("sigma", "x")
pgm.add_edge("X", "x")

# And plates.
pgm.add_plate(daft.Plate([-0.5, 0.5, 1, 3], label=r"train", shift=-0.1))
pgm.add_plate(daft.Plate([1.5, 0.5, 1, 3], label=r"test", shift=-0.1))

# Render and save.
pgm.render()
pgm.figure.savefig("xdqso.pdf")
pgm.figure.savefig("xdqso.png", dpi=150)
