import os.path

from lsst.utils import getPackageDir

config.load(os.path.join(getPackageDir("obs_subaru"), "config", "hsc", "isr.py"))

config.darkTime = None

config.isr.doBias = True
config.repair.cosmicray.nCrPixelMax = 1000000
config.repair.cosmicray.minSigma = 5.0
config.repair.cosmicray.min_DN = 50.0

config.isr.doBrighterFatter = False

