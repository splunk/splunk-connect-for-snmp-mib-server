#
# PySNMP MIB module INTEL-IPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-IPF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Gauge32, MibIdentifier, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter64, Integer32, TimeTicks, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "MibIdentifier", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "TimeTicks", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipf = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34))
ipfUGs = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 1))
ipfL3UGM = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 2))
ipfL4UGM = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 3))
ipfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 4))
class UserGroupSet(OctetString):
    pass

ipfUGsTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1), )
if mibBuilder.loadTexts: ipfUGsTable.setStatus('mandatory')
ipfUGsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1), ).setIndexNames((0, "INTEL-IPF-MIB", "ipfUGsNumber"))
if mibBuilder.loadTexts: ipfUGsEntry.setStatus('mandatory')
ipfUGsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfUGsNumber.setStatus('mandatory')
ipfUGsName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfUGsName.setStatus('mandatory')
ipfL3UGMTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1), )
if mibBuilder.loadTexts: ipfL3UGMTable.setStatus('mandatory')
ipfL3UGMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1), ).setIndexNames((0, "INTEL-IPF-MIB", "ipfL3UGMIpAddress"))
if mibBuilder.loadTexts: ipfL3UGMEntry.setStatus('mandatory')
ipfL3UGMIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfL3UGMIpAddress.setStatus('mandatory')
ipfL3UGMSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfL3UGMSubnetMask.setStatus('mandatory')
ipfL3UGMUserGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 3), UserGroupSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfL3UGMUserGroups.setStatus('mandatory')
ipfL4UGMTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1), )
if mibBuilder.loadTexts: ipfL4UGMTable.setStatus('mandatory')
ipfL4UGMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1), ).setIndexNames((0, "INTEL-IPF-MIB", "ipfL4UGMPortNumber"))
if mibBuilder.loadTexts: ipfL4UGMEntry.setStatus('mandatory')
ipfL4UGMPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfL4UGMPortNumber.setStatus('mandatory')
ipfL4UGMUserGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1, 2), UserGroupSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfL4UGMUserGroups.setStatus('mandatory')
ipfInfoL3Rejects = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoL3Rejects.setStatus('mandatory')
ipfInfoL4Rejects = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoL4Rejects.setStatus('mandatory')
ipfInfoMostRecentChange = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoMostRecentChange.setStatus('mandatory')
ipfInfoOnOffSwitch = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoOnOffSwitch.setStatus('mandatory')
ipfInfoDeleteUserGroup = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoDeleteUserGroup.setStatus('mandatory')
ipfInfoDeleteL3UGM = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoDeleteL3UGM.setStatus('mandatory')
ipfInfoDeleteL4UGM = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoDeleteL4UGM.setStatus('mandatory')
ipfInfoCreateDeleteStatus = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("createTableFull", 2), ("deleteNotFound", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoCreateDeleteStatus.setStatus('mandatory')
mibBuilder.exportSymbols("INTEL-IPF-MIB", ipfUGsNumber=ipfUGsNumber, ipfL4UGMEntry=ipfL4UGMEntry, ipfL4UGMTable=ipfL4UGMTable, ipfL3UGM=ipfL3UGM, ipfInfoOnOffSwitch=ipfInfoOnOffSwitch, ipfInfoDeleteL3UGM=ipfInfoDeleteL3UGM, ipfL4UGMUserGroups=ipfL4UGMUserGroups, UserGroupSet=UserGroupSet, ipf=ipf, ipfUGsTable=ipfUGsTable, ipfInfoDeleteUserGroup=ipfInfoDeleteUserGroup, ipfInfoCreateDeleteStatus=ipfInfoCreateDeleteStatus, ipfL3UGMEntry=ipfL3UGMEntry, ipfInfoL3Rejects=ipfInfoL3Rejects, ipfInfoMostRecentChange=ipfInfoMostRecentChange, ipfL3UGMTable=ipfL3UGMTable, ipfL4UGMPortNumber=ipfL4UGMPortNumber, ipfUGsEntry=ipfUGsEntry, ipfInfo=ipfInfo, ipfInfoDeleteL4UGM=ipfInfoDeleteL4UGM, ipfUGsName=ipfUGsName, ipfUGs=ipfUGs, ipfL4UGM=ipfL4UGM, ipfL3UGMIpAddress=ipfL3UGMIpAddress, ipfL3UGMUserGroups=ipfL3UGMUserGroups, ipfL3UGMSubnetMask=ipfL3UGMSubnetMask, ipfInfoL4Rejects=ipfInfoL4Rejects)
