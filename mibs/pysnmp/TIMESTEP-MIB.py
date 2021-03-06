#
# PySNMP MIB module TIMESTEP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMESTEP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, Unsigned32, Gauge32, Bits, TimeTicks, iso, Counter64, MibIdentifier, Integer32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "Unsigned32", "Gauge32", "Bits", "TimeTicks", "iso", "Counter64", "MibIdentifier", "Integer32", "IpAddress", "NotificationType")
DisplayString, TimeStamp, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention", "DateAndTime")
timestep = ModuleIdentity((1, 3, 6, 1, 4, 1, 1022))
timestep.setRevisions(('1998-10-21 00:00',))
if mibBuilder.loadTexts: timestep.setLastUpdated('9810210000Z')
if mibBuilder.loadTexts: timestep.setOrganization('Newbridge Corporation')
permitGate = MibIdentifier((1, 3, 6, 1, 4, 1, 1022, 9))
permitGateSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateSerialNumber.setStatus('current')
permitGateCpuUtilInst = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateCpuUtilInst.setStatus('current')
permitGateCpuUtilAvg1Min = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateCpuUtilAvg1Min.setStatus('current')
permitGateCpuUtilAvg5Min = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateCpuUtilAvg5Min.setStatus('current')
permitGateLastConfigModifTime = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateLastConfigModifTime.setStatus('current')
permitGateTotalRebootNum = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateTotalRebootNum.setStatus('current')
permitGateTotalVolMemory = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateTotalVolMemory.setStatus('current')
permitGateFreeVolMemory = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateFreeVolMemory.setStatus('current')
permitGateEncDevStatus = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("up", 0), ("down", 1), ("notApplicable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateEncDevStatus.setStatus('current')
permitGateRandNumGenStatus = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("up", 0), ("down", 1), ("notApplicable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateRandNumGenStatus.setStatus('current')
permitGateCertExpDate = MibScalar((1, 3, 6, 1, 4, 1, 1022, 9, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateCertExpDate.setStatus('current')
permitGateIfArpTable = MibTable((1, 3, 6, 1, 4, 1, 1022, 9, 12), )
if mibBuilder.loadTexts: permitGateIfArpTable.setStatus('current')
permitGateIfArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1022, 9, 12, 1), ).setIndexNames((0, "TIMESTEP-MIB", "permitGateIfArpIndex"))
if mibBuilder.loadTexts: permitGateIfArpEntry.setStatus('current')
permitGateIfArpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateIfArpIndex.setStatus('current')
permitGateIfArpInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateIfArpInPkts.setStatus('current')
permitGateIfArpOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateIfArpOutPkts.setStatus('current')
permitGateIfArpInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateIfArpInOctets.setStatus('current')
permitGateIfArpOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1022, 9, 12, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permitGateIfArpOutOctets.setStatus('current')
mibBuilder.exportSymbols("TIMESTEP-MIB", permitGateIfArpEntry=permitGateIfArpEntry, permitGateCpuUtilInst=permitGateCpuUtilInst, permitGateFreeVolMemory=permitGateFreeVolMemory, permitGateEncDevStatus=permitGateEncDevStatus, permitGateCpuUtilAvg5Min=permitGateCpuUtilAvg5Min, permitGateIfArpOutOctets=permitGateIfArpOutOctets, permitGateTotalRebootNum=permitGateTotalRebootNum, permitGate=permitGate, permitGateTotalVolMemory=permitGateTotalVolMemory, permitGateCertExpDate=permitGateCertExpDate, permitGateIfArpTable=permitGateIfArpTable, permitGateLastConfigModifTime=permitGateLastConfigModifTime, permitGateRandNumGenStatus=permitGateRandNumGenStatus, permitGateIfArpIndex=permitGateIfArpIndex, permitGateSerialNumber=permitGateSerialNumber, PYSNMP_MODULE_ID=timestep, permitGateCpuUtilAvg1Min=permitGateCpuUtilAvg1Min, permitGateIfArpInPkts=permitGateIfArpInPkts, permitGateIfArpOutPkts=permitGateIfArpOutPkts, permitGateIfArpInOctets=permitGateIfArpInOctets, timestep=timestep)
