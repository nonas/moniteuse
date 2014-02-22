#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy import loadtxt
import datetime

# Load data from files
DATA_SDA = loadtxt('sda.dat', delimiter=' ', skiprows=1)

SDA_DATE = DATA_SDA[:,0]
SDA_SUT = DATA_SDA[:,1]
SDA_SSC = DATA_SDA[:,2]
SDA_RSC = DATA_SDA[:,3]
SDA_POH = DATA_SDA[:,4]
SDA_PCC = DATA_SDA[:,5]
SDA_USC = DATA_SDA[:,6]
SDA_HW32 = DATA_SDA[:,7]
SDA_WMWI = DATA_SDA[:,8]
SDA_WHRP = DATA_SDA[:,9]
SDA_WM = DATA_SDA[:,10]
SDA_ARS = DATA_SDA[:,11]
SDA_MWI = DATA_SDA[:,12]
SDA_EEE = DATA_SDA[:,13]
SDA_USED_ROOT = DATA_SDA[:,14]
SDA_USED_HOME = DATA_SDA[:,15]

xdates_sda = [datetime.datetime.strptime(str(int(date)),'%Y%m%d') for date in SDA_DATE]

# Load data from files
DATA_SDB = loadtxt('sdb.dat', delimiter=' ', skiprows=1)

SDB_DATE = DATA_SDB[:,0]
SDB_RRER = DATA_SDB[:,1]
SDB_SUT = DATA_SDB[:,2]
SDB_SSC = DATA_SDB[:,3]
SDB_RSC = DATA_SDB[:,4]
SDB_SER = DATA_SDB[:,5]
SDB_POH = DATA_SDB[:,6]
SDB_SRC = DATA_SDB[:,7]
SDB_CRC = DATA_SDB[:,8]
SDB_POC = DATA_SDB[:,9]
SDB_PORC = DATA_SDB[:,10]
SDB_LCC = DATA_SDB[:,11]
SDB_TC = DATA_SDB[:,12]
SDB_REC = DATA_SDB[:,13]
SDB_CPS = DATA_SDB[:,14]
SDB_OU = DATA_SDB[:,15]
SDB_UCEC = DATA_SDB[:,16]
SDB_MZER = DATA_SDB[:,17]
SDB_USED_WDCG = DATA_SDB[:,18]

xdates_sdb = [datetime.datetime.strptime(str(int(date)),'%Y%m%d') for date in SDB_DATE]

# clear plot
plt.clf()

fig = plt.figure(figsize=(7,6))

#########
# sub 1
#########
ax1 = plt.subplot(211)

# Set x limits
#plt.xlim(0,5)
# xlabel
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.title("size [GiB]")

# Set y limits
plt.ylim(0,40)
# ylabel
#plt.ylabel("size [GiB]")

# plot
plt.stackplot( xdates_sda, SDA_USED_ROOT/(1024*1024), SDA_USED_HOME/(1024*1024))
p1 = plt.Rectangle((0, 0), 1, 1, fc="b")
p2 = plt.Rectangle((0, 0), 1, 1, fc="g")
plt.legend([p1, p2], ["root", "home"],loc = 2)

#########
# sub 2
#########
ax2 = plt.subplot(212)

# Set x limits
#plt.xlim(0,5)
# xlabel
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# Set y limits
plt.ylim(0,1000)
# ylabel
#plt.ylabel("size [GiB]")

# plot
plt.stackplot( xdates_sdb, SDB_USED_WDCG/(1024*1024))
p1 = plt.Rectangle((0, 0), 1, 1, fc="b")
plt.legend([p1], ["data"],loc = 3)

plt.savefig('disks_size.png', bbox_inches='tight')
