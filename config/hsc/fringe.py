import os.path

from lsst.utils import getPackageDir

config.load(os.path.join(getPackageDir("obs_subaru"), "config", "hsc", "isr.py"))

config.isr.doBrighterFatter = False

