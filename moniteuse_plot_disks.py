#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy import loadtxt
import datetime

######################
# Load data from files
######################
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

years = mdates.YearLocator() # every year
months = mdates.MonthLocator() # every month
yearsFmt = mdates.DateFormatter('%Y')

###################
# plot1 : disk size
###################
plt.clf()

fig = plt.figure(figsize=(7,6))

#########
# sub 1
#########
ax1 = plt.subplot(211)

# format the ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
ax1.xaxis.set_minor_locator(months)

plt.title("size [GiB]")

# Set y limits
plt.ylim(0,40)

labels = ["root", "home"]
# plot
plt.stackplot( xdates_sda, SDA_USED_ROOT/(1024*1024), SDA_USED_HOME/(1024*1024), labels=labels)
plt.legend(loc = 2)

#########
# sub 2
#########
ax2 = plt.subplot(212)

# format the ticks
ax2.xaxis.set_major_locator(years)
ax2.xaxis.set_major_formatter(yearsFmt)
ax2.xaxis.set_minor_locator(months)

# Set y limits
plt.ylim(0,1024)

# plot
plt.stackplot( xdates_sdb, SDB_USED_WDCG/(1024*1024))
plt.legend(["data"], loc = 2)

plt.savefig('disks_size.png', bbox_inches='tight')

##########################
# plot2 : ssd HW32 per day
##########################
plt.clf()

fig = plt.figure(figsize=(7,3))

#########
# sub 1
#########
ax1 = plt.subplot(111)

years = mdates.YearLocator() # every year
months = mdates.MonthLocator() # every month
yearsFmt = mdates.DateFormatter('%Y')

plt.title("ssd HostWrite [GiB]")

# plot
plt.plot( xdates_sda, (SDA_HW32[:])*32/1024)
#plt.legend(loc = 2)
fig.autofmt_xdate()

plt.savefig('disks_ssd_hw32.png', bbox_inches='tight')
