import sys
sys.path.append('../..')

from gmos_longslit_fieldflattening import *
from matplotlib import pyplot as plt

from astropy.io import fits
# bin1 central
data1 = fits.open('S20200225S0048.fits')
gmos_hamamatsu(data1, show_fig=True)

# bin2 full frame
data2 = fits.open('N20180811S0148.fits')
gmos_hamamatsu(data2, show_fig=True)

# bin2 central
data3 = fits.open('N20180811S0201.fits.bz2')
gmos_hamamatsu(data3, show_fig=True)
