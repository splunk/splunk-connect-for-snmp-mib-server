#
# PySNMP MIB module ClusterX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ClusterX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Counter64, iso, Counter32, Bits, Unsigned32, IpAddress, ModuleIdentity, Integer32, Gauge32, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Counter64", "iso", "Counter32", "Bits", "Unsigned32", "IpAddress", "ModuleIdentity", "Integer32", "Gauge32", "enterprises", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
veritassoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 1302))
veritasproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3))
clusterX = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 7))
clxMibStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 7, 1))
clxTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2))
clxMibStatsMajRev = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsMajRev.setStatus('mandatory')
clxMibStatsMinRev = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsMinRev.setStatus('mandatory')
clxMibStatsVendorName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsVendorName.setStatus('mandatory')
clxTrapDataString01 = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 1), DisplayString())
if mibBuilder.loadTexts: clxTrapDataString01.setStatus('mandatory')
clxTrapDataNodeName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 2), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNodeName.setStatus('mandatory')
clxTrapDataClusterName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 3), DisplayString())
if mibBuilder.loadTexts: clxTrapDataClusterName.setStatus('mandatory')
clxTrapDataResourceName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 4), DisplayString())
if mibBuilder.loadTexts: clxTrapDataResourceName.setStatus('mandatory')
clxTrapDataResourceType = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 5), DisplayString())
if mibBuilder.loadTexts: clxTrapDataResourceType.setStatus('mandatory')
clxTrapDataSeverityValue = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("info", 0), ("warning", 1), ("error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxTrapDataSeverityValue.setStatus('mandatory')
clxTrapDataNetwork = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 7), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNetwork.setStatus('mandatory')
clxTrapEventDate = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 8), DisplayString())
if mibBuilder.loadTexts: clxTrapEventDate.setStatus('mandatory')
clxTrapEventTime = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 9), DisplayString())
if mibBuilder.loadTexts: clxTrapEventTime.setStatus('mandatory')
clxTrapEventSource = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 10), DisplayString())
if mibBuilder.loadTexts: clxTrapEventSource.setStatus('mandatory')
clxTrapEventCategory = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 11), DisplayString())
if mibBuilder.loadTexts: clxTrapEventCategory.setStatus('mandatory')
clxTrapEventID = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 12), DisplayString())
if mibBuilder.loadTexts: clxTrapEventID.setStatus('mandatory')
clxTrapEventUser = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 13), DisplayString())
if mibBuilder.loadTexts: clxTrapEventUser.setStatus('mandatory')
clxTrapEventComputer = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 14), DisplayString())
if mibBuilder.loadTexts: clxTrapEventComputer.setStatus('mandatory')
clxTrapDataNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 15), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNetworkName.setStatus('mandatory')
clxTrapDataWLBSNodeName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 16), DisplayString())
if mibBuilder.loadTexts: clxTrapDataWLBSNodeName.setStatus('mandatory')
clxTrapDataWLBSClusterName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 17), DisplayString())
if mibBuilder.loadTexts: clxTrapDataWLBSClusterName.setStatus('mandatory')
clxTrapDataWLBSHostID = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 18), DisplayString())
if mibBuilder.loadTexts: clxTrapDataWLBSHostID.setStatus('mandatory')
clxTrapDataPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 19), DisplayString())
if mibBuilder.loadTexts: clxTrapDataPortNumber.setStatus('mandatory')
clxTrapDataApplicationName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 20), DisplayString())
if mibBuilder.loadTexts: clxTrapDataApplicationName.setStatus('mandatory')
clxTrapDataApplicationFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 21), DisplayString())
if mibBuilder.loadTexts: clxTrapDataApplicationFailureReason.setStatus('mandatory')
clxTrapDataApplicationFailureAction = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 22), DisplayString())
if mibBuilder.loadTexts: clxTrapDataApplicationFailureAction.setStatus('mandatory')
clxTrapDataApplicationOnLineAction = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 23), DisplayString())
if mibBuilder.loadTexts: clxTrapDataApplicationOnLineAction.setStatus('mandatory')
clusterXTrapStr = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,1)).setObjects(("ClusterX-MIB", "clxTrapDataString01"))
clusterXTrapNodeFail = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,2)).setObjects(("ClusterX-MIB", "clxTrapDataClusterName"), ("ClusterX-MIB", "clxTrapDataNodeName"))
clusterXTrapClusterFail = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,3)).setObjects(("ClusterX-MIB", "clxTrapDataClusterName"))
clusterXTrapResourceFail = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,4)).setObjects(("ClusterX-MIB", "clxTrapDataClusterName"), ("ClusterX-MIB", "clxTrapDataNodeName"), ("ClusterX-MIB", "clxTrapDataResourceName"))
clusterXTrapNodeJoins = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,5)).setObjects(("ClusterX-MIB", "clxTrapDataClusterName"), ("ClusterX-MIB", "clxTrapDataNodeName"))
clusterXTrapNetworkFail = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,6)).setObjects(("ClusterX-MIB", "clxTrapDataString01"), ("ClusterX-MIB", "clxTrapDataNetworkName"))
clusterXTrapNormalClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,7)).setObjects(("ClusterX-MIB", "clxTrapEventDate"), ("ClusterX-MIB", "clxTrapEventTime"), ("ClusterX-MIB", "clxTrapEventSource"), ("ClusterX-MIB", "clxTrapEventCategory"), ("ClusterX-MIB", "clxTrapEventID"), ("ClusterX-MIB", "clxTrapEventUser"), ("ClusterX-MIB", "clxTrapEventComputer"))
clusterXTrapWarningClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,8)).setObjects(("ClusterX-MIB", "clxTrapEventDate"), ("ClusterX-MIB", "clxTrapEventTime"), ("ClusterX-MIB", "clxTrapEventSource"), ("ClusterX-MIB", "clxTrapEventCategory"), ("ClusterX-MIB", "clxTrapEventID"), ("ClusterX-MIB", "clxTrapEventUser"), ("ClusterX-MIB", "clxTrapEventComputer"))
clusterXTrapCriticalClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,9)).setObjects(("ClusterX-MIB", "clxTrapEventDate"), ("ClusterX-MIB", "clxTrapEventTime"), ("ClusterX-MIB", "clxTrapEventSource"), ("ClusterX-MIB", "clxTrapEventCategory"), ("ClusterX-MIB", "clxTrapEventID"), ("ClusterX-MIB", "clxTrapEventUser"), ("ClusterX-MIB", "clxTrapEventComputer"))
clusterXWLBSTrapApplicationFail = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,10)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"), ("ClusterX-MIB", "clxTrapDataApplicationName"), ("ClusterX-MIB", "clxTrapDataApplicationFailureReason"), ("ClusterX-MIB", "clxTrapDataApplicationFailureAction"))
clusterXWLBSTrapEventLogNormal = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,11)).setObjects(("ClusterX-MIB", "clxTrapEventDate"), ("ClusterX-MIB", "clxTrapEventTime"), ("ClusterX-MIB", "clxTrapEventSource"), ("ClusterX-MIB", "clxTrapEventCategory"), ("ClusterX-MIB", "clxTrapEventID"), ("ClusterX-MIB", "clxTrapEventUser"), ("ClusterX-MIB", "clxTrapEventComputer"))
clusterXWLBSTrapEventLogWarning = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,12)).setObjects(("ClusterX-MIB", "clxTrapEventDate"), ("ClusterX-MIB", "clxTrapEventTime"), ("ClusterX-MIB", "clxTrapEventSource"), ("ClusterX-MIB", "clxTrapEventCategory"), ("ClusterX-MIB", "clxTrapEventID"), ("ClusterX-MIB", "clxTrapEventUser"), ("ClusterX-MIB", "clxTrapEventComputer"))
clusterXWLBSTrapEventLogCritical = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,13)).setObjects(("ClusterX-MIB", "clxTrapEventDate"), ("ClusterX-MIB", "clxTrapEventTime"), ("ClusterX-MIB", "clxTrapEventSource"), ("ClusterX-MIB", "clxTrapEventCategory"), ("ClusterX-MIB", "clxTrapEventID"), ("ClusterX-MIB", "clxTrapEventUser"), ("ClusterX-MIB", "clxTrapEventComputer"))
clusterXWLBSTrapSuspended = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,14)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
clusterXWLBSTrapResumed = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,15)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
clusterXWLBSTrapStarted = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,16)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
clusterXWLBSTrapStopped = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,17)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
clusterXWLBSTrapDrainStopped = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,18)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
clusterXWLBSTrapConverged = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,19)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
clusterXWLBSTrapEnabled = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,20)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"), ("ClusterX-MIB", "clxTrapDataPortNumber"))
clusterXWLBSTrapDisabled = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,21)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"), ("ClusterX-MIB", "clxTrapDataPortNumber"))
clusterXWLBSTrapDrained = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,22)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"), ("ClusterX-MIB", "clxTrapDataPortNumber"))
clusterXWLBSTrapApplicationOnLine = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,23)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"), ("ClusterX-MIB", "clxTrapDataApplicationName"), ("ClusterX-MIB", "clxTrapDataApplicationOnLineAction"))
clusterXWLBSTrapReloaded = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 7) + (0,24)).setObjects(("ClusterX-MIB", "clxTrapDataWLBSClusterName"), ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
mibBuilder.exportSymbols("ClusterX-MIB", clxTrapEventID=clxTrapEventID, clxMibStatsMajRev=clxMibStatsMajRev, clusterXWLBSTrapStopped=clusterXWLBSTrapStopped, clusterXWLBSTrapEventLogWarning=clusterXWLBSTrapEventLogWarning, clusterXTrapNormalClusterServiceLog=clusterXTrapNormalClusterServiceLog, clusterXTrapCriticalClusterServiceLog=clusterXTrapCriticalClusterServiceLog, clxTrapDataClusterName=clxTrapDataClusterName, clusterXWLBSTrapEventLogCritical=clusterXWLBSTrapEventLogCritical, clxTrapDataResourceType=clxTrapDataResourceType, clusterXWLBSTrapSuspended=clusterXWLBSTrapSuspended, clusterXWLBSTrapReloaded=clusterXWLBSTrapReloaded, clxTrapDataApplicationFailureReason=clxTrapDataApplicationFailureReason, clxTrapDataSeverityValue=clxTrapDataSeverityValue, clxTrapEventUser=clxTrapEventUser, clusterXTrapClusterFail=clusterXTrapClusterFail, clxTrapDataResourceName=clxTrapDataResourceName, clxMibStatsMinRev=clxMibStatsMinRev, clxTrapDataWLBSClusterName=clxTrapDataWLBSClusterName, clusterXTrapNodeFail=clusterXTrapNodeFail, clusterXWLBSTrapApplicationOnLine=clusterXWLBSTrapApplicationOnLine, clusterXWLBSTrapStarted=clusterXWLBSTrapStarted, clxTrapDataPortNumber=clxTrapDataPortNumber, clusterXTrapNodeJoins=clusterXTrapNodeJoins, clusterXWLBSTrapEventLogNormal=clusterXWLBSTrapEventLogNormal, clxTrapDataWLBSNodeName=clxTrapDataWLBSNodeName, clxTrapDataApplicationName=clxTrapDataApplicationName, clusterXTrapNetworkFail=clusterXTrapNetworkFail, clxTrapDataNetworkName=clxTrapDataNetworkName, clxTrapDataNetwork=clxTrapDataNetwork, clusterXTrapResourceFail=clusterXTrapResourceFail, clxTrapData=clxTrapData, clusterXWLBSTrapDisabled=clusterXWLBSTrapDisabled, clxTrapDataApplicationOnLineAction=clxTrapDataApplicationOnLineAction, clusterXTrapWarningClusterServiceLog=clusterXTrapWarningClusterServiceLog, clusterXWLBSTrapEnabled=clusterXWLBSTrapEnabled, clusterXWLBSTrapResumed=clusterXWLBSTrapResumed, clxTrapDataNodeName=clxTrapDataNodeName, clxTrapEventDate=clxTrapEventDate, clxTrapDataWLBSHostID=clxTrapDataWLBSHostID, clxTrapEventSource=clxTrapEventSource, clusterXWLBSTrapDrainStopped=clusterXWLBSTrapDrainStopped, clxMibStatsVendorName=clxMibStatsVendorName, clxTrapDataString01=clxTrapDataString01, clxTrapEventTime=clxTrapEventTime, clxTrapEventCategory=clxTrapEventCategory, clxMibStats=clxMibStats, clusterXWLBSTrapApplicationFail=clusterXWLBSTrapApplicationFail, clusterX=clusterX, veritassoftware=veritassoftware, clusterXTrapStr=clusterXTrapStr, clusterXWLBSTrapConverged=clusterXWLBSTrapConverged, clxTrapDataApplicationFailureAction=clxTrapDataApplicationFailureAction, veritasproducts=veritasproducts, clusterXWLBSTrapDrained=clusterXWLBSTrapDrained, clxTrapEventComputer=clxTrapEventComputer)
