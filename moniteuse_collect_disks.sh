#!/bin/sh

cd /home/nonas/projets/moniteuse
DATE=$(date +%Y%m%d)
DF=$(df)

# /dev/sda is Intel X18-M/X25-M/X25-V G2 SSDs (40GB)
SMART_SDA=$(/usr/sbin/smartctl -a /dev/sda)
SUT_A=$(echo "$SMART_SDA" | awk -F" " '/Spin_Up_Time/ {print $NF}')
SSC_A=$(echo "$SMART_SDA" | awk -F" " '/Start_Stop_Count/ {print $NF}')
RSC_A=$(echo "$SMART_SDA" | awk -F" " '/Reallocated_Sector_Ct/ {print $NF}')
POH_A=$(echo "$SMART_SDA" | awk -F" " '/Power_On_Hours/ {print $NF}')
PCC_A=$(echo "$SMART_SDA" | awk -F" " '/Power_Cycle_Count/ {print $NF}')
USC_A=$(echo "$SMART_SDA" | awk -F" " '/Unsafe_Shutdown_Count/ {print $NF}')
HW32_A=$(echo "$SMART_SDA" | awk -F" " '/Host_Writes_32MiB/ {print $NF}')
WMWI_A=$(echo "$SMART_SDA" | awk -F" " '/Workld_Media_Wear_Indic/ {print $NF}')
WHRP_A=$(echo "$SMART_SDA" | awk -F" " '/Workld_Host_Reads_Perc/ {print $NF}')
WM_A=$(echo "$SMART_SDA" | awk -F" " '/Workload_Minutes/ {print $NF}')
ARS_A=$(echo "$SMART_SDA" | awk -F" " '/Available_Reservd_Space/ {print $NF}')
MWI_A=$(echo "$SMART_SDA" | awk -F" " '/Media_Wearout_Indicator/ {print $NF}')
EEE_A=$(echo "$SMART_SDA" | awk -F" " '/End-to-End_Error/ {print $NF}')

S_USED_ROOT=$(echo "$DF" | awk -F" " '/\/dev\/sda1/ {print $3}')
S_USED_HOME=$(echo "$DF" | awk -F" " '/\/dev\/sda3/ {print $3}')

echo $DATE $SUT_A $SSC_A $RSC_A $POH_A $PCC_A $USC_A $HW32_A $WMWI_A $WHRP_A $WM_A $ARS_A $MWI_A $EEE_A $S_USED_ROOT $S_USED_HOME >> sda.dat

# /deb/sdb is Western Digital Caviar Green (1TB)
SMART_SDB=$(/usr/sbin/smartctl -a /dev/sdb)
RRER_B=$(echo "$SMART_SDB" | awk -F" " '/Raw_Read_Error_Rate/ {print $NF}')
SUT_B=$(echo "$SMART_SDB" | awk -F" " '/Spin_Up_Time/ {print $NF}')
SSC_B=$(echo "$SMART_SDB" | awk -F" " '/Start_Stop_Count/ {print $NF}')
RSC_B=$(echo "$SMART_SDB" | awk -F" " '/Reallocated_Sector_Ct/ {print $NF}')
SER_B=$(echo "$SMART_SDB" | awk -F" " '/Seek_Error_Rate/ {print $NF}')
POH_B=$(echo "$SMART_SDB" | awk -F" " '/Power_On_Hours/ {print $NF}')
SRC_B=$(echo "$SMART_SDB" | awk -F" " '/Spin_Retry_Count/ {print $NF}')
CRC_B=$(echo "$SMART_SDB" | awk -F" " '/Calibration_Retry_Count/ {print $NF}')
POC_B=$(echo "$SMART_SDB" | awk -F" " '/Power_Cycle_Count/ {print $NF}')
PORC_B=$(echo "$SMART_SDB" | awk -F" " '/Power-Off_Retract_Count/ {print $NF}')
LCC_B=$(echo "$SMART_SDB" | awk -F" " '/Load_Cycle_Count/ {print $NF}')
TC_B=$(echo "$SMART_SDB" | awk -F" " '/Temperature_Celsius/ {print $NF}')
REC_B=$(echo "$SMART_SDB" | awk -F" " '/Reallocated_Event_Count/ {print $NF}')
CPS_B=$(echo "$SMART_SDB" | awk -F" " '/Current_Pending_Sector/ {print $NF}')
OU_B=$(echo "$SMART_SDB" | awk -F" " '/Offline_Uncorrectable/ {print $NF}')
UCEC_B=$(echo "$SMART_SDB" | awk -F" " '/UDMA_CRC_Error_Count/ {print $NF}')
MZER_B=$(echo "$SMART_SDB" | awk -F" " '/Multi_Zone_Error_Rate/ {print $NF}')

S_USED_WDCG=$(echo "$DF" | awk -F" " '/\/dev\/sdb1/ {print $3}')

echo $DATE $RRER_B $SUT_B $SSC_B $RSC_B $SER_B $POH_B $SRC_B $CRC_B $POC_B $PORC_B $LCC_B $TC_B $REC_B $CPS_B $OU_B $UCEC_B $MZER_B $S_USED_WDCG >> sdb.dat
