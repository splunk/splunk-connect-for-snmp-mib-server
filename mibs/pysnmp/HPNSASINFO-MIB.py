#
# PySNMP MIB module HPNSASINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPNSASINFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, NotificationType, ModuleIdentity, Bits, ObjectIdentity, IpAddress, TimeTicks, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "NotificationType", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "TimeTicks", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Integer32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7))
hpnsaSiMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1))
hpnsaSiAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2))
hpnsaSiBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3))
hpnsaSiSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4))
hpnsaSiPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5))
hpnsaSiMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6))
hpnsaSiFloppyDrive = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8))
hpnsaSiRemoteLocatorLED = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9))
hpnsaSiMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiMibRevMajor.setStatus('mandatory')
hpnsaSiMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiMibRevMinor.setStatus('mandatory')
hpnsaSiAgentTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1), )
if mibBuilder.loadTexts: hpnsaSiAgentTable.setStatus('mandatory')
hpnsaSiAgentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1), ).setIndexNames((0, "HPNSASINFO-MIB", "hpnsaSiAgentIndex"))
if mibBuilder.loadTexts: hpnsaSiAgentEntry.setStatus('mandatory')
hpnsaSiAgentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiAgentIndex.setStatus('mandatory')
hpnsaSiAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiAgentName.setStatus('mandatory')
hpnsaSiAgentVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiAgentVersion.setStatus('mandatory')
hpnsaSiAgentDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiAgentDate.setStatus('mandatory')
hpnsaSiModel = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 35, 36, 40, 41, 42, 43, 44, 46, 47, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89))).clone(namedValues=NamedValues(("hp-vectra-pc", 0), ("hp-vectra-es-12-pc", 1), ("hp-vectra-rs-20-pc", 2), ("hp-vectra-portablecs-pc", 3), ("hp-vectra-es-pc", 4), ("hp-vectra-cs-pc", 5), ("hp-vectra-rs-16-pc", 6), ("hp-vectra-qs-16-pc", 7), ("hp-vectra-qs-20-pc", 8), ("hp-vectra-rs-20c-pc", 9), ("hp-vectra-rs-25c-pc", 10), ("hp-vectra-ls-286-pc", 11), ("hp-vectra-qs-16s-pc", 12), ("hp-vectra-386-25-pc", 13), ("hp-vectra-486-25t-pc", 14), ("hp-vectra-286-12-pc", 15), ("hp-vectra-486-33t-pc", 16), ("hp-vectra-386-20-pc", 17), ("hp-vectra-386-16n-pc", 18), ("hp-vectra-386-20n-pc", 19), ("hp-vectra-486s-20-pc", 20), ("hp-vectra-386s-20-pc", 21), ("hp-vectra-486-25u-pc", 22), ("hp-vectra-486-33u-pc", 23), ("hp-vectra-486-50u-pc", 24), ("hp-vectra-486-66u-pc", 25), ("hp-vectra-486-st-series", 26), ("hp-vectra-386-25n", 27), ("hp-vectra-486-n", 28), ("hp-vectra-386s-25", 29), ("hp-vectra-386-33n", 30), ("hp-vectra-486-33n", 32), ("hp-netserver-le-series", 35), ("hp-netserver-lm-series", 36), ("hp-netserver-lf-series", 40), ("hp-netserver-lc-series", 41), ("hp-netserver-ls-series", 42), ("hp-netserver-lh-series", 43), ("hp-netserver-lc-series", 44), ("hp-netserver-lx-series", 46), ("hp-netserver-lh-series", 47), ("hp-netserver-lh-series", 49), ("hp-netserver-e-series", 50), ("hp-netserver-e-series", 51), ("hp-netserver-ld-series", 52), ("hp-netserver-racks-series", 54), ("hp-netserver-lc-series", 55), ("hp-netserver-e-series", 56), ("hp-netserver-lx-series", 57), ("hp-netserver-e-series", 58), ("hp-netserver-e-series", 59), ("hp-netserver-lh-series", 60), ("hp-netserver-lc-series", 61), ("hp-netserver-lh-series", 62), ("hp-netserver-lh-series", 63), ("hp-netserver-lx-series", 64), ("hp-netserver-lx-series", 65), ("hp-netserver-lh3000", 66), ("hp-netserver-lh6000", 67), ("hp-netserver-lc2000", 68), ("hp-netserver-lt6000", 69), ("hp-netserver-e-series", 70), ("hp-netserver-e-series", 71), ("hp-netserver-lp1000r", 72), ("hp-netserver-lp2000r", 73), ("hp-netserver-tc6100", 75), ("hp-netserver-tc3100", 79), ("hp-netserver-tc4100", 80), ("hp-netserver-lh6000u3", 82), ("hp-netserver-lt6000ru3", 83), ("hp-netserver-lc2000u3", 84), ("hp-netserver-lh3000u3", 85), ("hp-netserver-lp1000r", 86), ("hp-netserver-lp2000r", 87), ("hp-netserver-tc7100", 88), ("hp-netserver-rc7100", 89)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiModel.setStatus('mandatory')
hpnsaSiBIOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiBIOSVersion.setStatus('mandatory')
hpnsaSiVideoBIOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiVideoBIOSVersion.setStatus('optional')
hpnsaSiSCSIBIOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiSCSIBIOSVersion.setStatus('mandatory')
hpnsaSiNumEISASlots = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiNumEISASlots.setStatus('mandatory')
hpnsaSiNumPCISlots = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiNumPCISlots.setStatus('mandatory')
hpnsaSiNumCPU = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiNumCPU.setStatus('mandatory')
hpnsaSiCPUTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8), )
if mibBuilder.loadTexts: hpnsaSiCPUTable.setStatus('mandatory')
hpnsaSiCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1), ).setIndexNames((0, "HPNSASINFO-MIB", "hpnsaSiCPUIndex"))
if mibBuilder.loadTexts: hpnsaSiCPUEntry.setStatus('mandatory')
hpnsaSiCPUIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiCPUIndex.setStatus('mandatory')
hpnsaSiCPUModel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 253, 254, 255))).clone(namedValues=NamedValues(("cpu-80286", 0), ("cpu-8088", 1), ("cpu-8086", 2), ("cpu-80386", 3), ("cpu-80386-sx", 4), ("cpu-486-dx", 5), ("cpu-486-sx", 6), ("cpu-486-dx2-or-overdrive", 8), ("cpu-486-p23t", 9), ("cpu-487-sx", 10), ("cpu-pentium", 11), ("cpu-pentium-overdrive", 12), ("cpu-486-24c", 13), ("cpu-pentium-series-p54c", 14), ("cpu-pentium-series-p54ct", 15), ("cpu-pentium-series-p54cm", 16), ("cpu-486-sx2", 17), ("cpu-486-sl", 18), ("cpu-pentium-series-p6", 19), ("cpu-pentium-ii", 20), ("cpu-pentium-ii-xeon", 21), ("cpu-pentium-iii", 22), ("cpu-pentium-iii-xeon", 23), ("cpu-itanium", 25), ("notpresent", 253), ("cpu-dual-pentium", 254), ("cpu-unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiCPUModel.setStatus('mandatory')
hpnsaSiCPUSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiCPUSpeed.setStatus('mandatory')
hpnsaSiOpSysType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiOpSysType.setStatus('mandatory')
hpnsaSiOpSysVer = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiOpSysVer.setStatus('mandatory')
hpnsaSiSystemName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiSystemName.setStatus('mandatory')
hpnsaSiSystemID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiSystemID.setStatus('optional')
hpnsaSiKbdType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiKbdType.setStatus('optional')
hpnsaSiMouseType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiMouseType.setStatus('optional')
hpnsaSiVideoType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiVideoType.setStatus('optional')
hpnsaSiNumISASlots = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiNumISASlots.setStatus('mandatory')
hpnsaSiModelName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiModelName.setStatus('mandatory')
hpnsaSiOpSysDescription = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiOpSysDescription.setStatus('mandatory')
hpnsaSiPowerOnPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiPowerOnPassword.setStatus('mandatory')
hpnsaSiNetServerMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiNetServerMode.setStatus('mandatory')
hpnsaSiKeyboardLockPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiKeyboardLockPassword.setStatus('mandatory')
hpnsaSiVideoBlankMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiVideoBlankMode.setStatus('mandatory')
hpnsaSiBootDiskPriority = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("n-a", 0), ("c-then-a", 1), ("a-then-c", 2), ("c-only", 3), ("a-only", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiBootDiskPriority.setStatus('mandatory')
hpnsaSiWriteToFloppy = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiWriteToFloppy.setStatus('mandatory')
hpnsaSiKbdMouseInactivityTO = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("n-a", 0), ("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiKbdMouseInactivityTO.setStatus('mandatory')
hpnsaSiPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1), )
if mibBuilder.loadTexts: hpnsaSiPortTable.setStatus('mandatory')
hpnsaSiPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1), ).setIndexNames((0, "HPNSASINFO-MIB", "hpnsaSiPortIndex"))
if mibBuilder.loadTexts: hpnsaSiPortEntry.setStatus('mandatory')
hpnsaSiPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiPortIndex.setStatus('mandatory')
hpnsaSiPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("serial", 1), ("parallel", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiPortType.setStatus('mandatory')
hpnsaSiPortStartAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiPortStartAddress.setStatus('mandatory')
hpnsaSiPortEndAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiPortEndAddress.setStatus('mandatory')
hpnsaSiPortInterruptNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiPortInterruptNum.setStatus('mandatory')
hpnsaSiBaseMemSize = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiBaseMemSize.setStatus('mandatory')
hpnsaSiExtMemSize = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiExtMemSize.setStatus('mandatory')
hpnsaSiMemType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 0), ("on-board", 1), ("singleWidthModule", 2), ("doubleWidthModule", 3), ("simm", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiMemType.setStatus('optional')
hpnsaSiMemSpeed = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiMemSpeed.setStatus('optional')
hpnsaSiNumFloppyDrives = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiNumFloppyDrives.setStatus('mandatory')
hpnsaSiFloppyDriveTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2), )
if mibBuilder.loadTexts: hpnsaSiFloppyDriveTable.setStatus('mandatory')
hpnsaSiFloppyDriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1), ).setIndexNames((0, "HPNSASINFO-MIB", "hpnsaSiFloppyDriveIndex"))
if mibBuilder.loadTexts: hpnsaSiFloppyDriveEntry.setStatus('mandatory')
hpnsaSiFloppyDriveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiFloppyDriveIndex.setStatus('mandatory')
hpnsaSiFloppyDriveType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("m-360K", 1), ("m-1-2MB", 2), ("m-1-2-MB", 3), ("m-1-44MB", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiFloppyDriveType.setStatus('mandatory')
hpnsaSiRemoteLocatorLEDSupported = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notsupported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiRemoteLocatorLEDSupported.setStatus('mandatory')
hpnsaSiRemoteLocatorLEDStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ledoff", 0), ("ledon", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaSiRemoteLocatorLEDStatus.setStatus('mandatory')
hpnsaSiRemoteLocatorLEDSet = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ledoff", 0), ("ledon", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnsaSiRemoteLocatorLEDSet.setStatus('mandatory')
mibBuilder.exportSymbols("HPNSASINFO-MIB", hpnsaSiBIOSVersion=hpnsaSiBIOSVersion, nm=nm, hp=hp, hpnsaSiAgentEntry=hpnsaSiAgentEntry, hpnsaSiFloppyDriveIndex=hpnsaSiFloppyDriveIndex, hpnsaSiMemType=hpnsaSiMemType, hpnsaSiNumEISASlots=hpnsaSiNumEISASlots, hpnsaSiCPUIndex=hpnsaSiCPUIndex, hpnsaSiModelName=hpnsaSiModelName, hpnsaSiPowerOnPassword=hpnsaSiPowerOnPassword, hpnsaSiPortStartAddress=hpnsaSiPortStartAddress, hpnsaSiOpSysType=hpnsaSiOpSysType, hpnsaSiFloppyDriveTable=hpnsaSiFloppyDriveTable, hpnsaSiPortInterruptNum=hpnsaSiPortInterruptNum, hpnsaSiAgent=hpnsaSiAgent, hpnsaSiMibRevMinor=hpnsaSiMibRevMinor, hpnsaSiMibRevMajor=hpnsaSiMibRevMajor, hpnsaSiVideoType=hpnsaSiVideoType, hpnsaSiRemoteLocatorLEDSet=hpnsaSiRemoteLocatorLEDSet, hpnsaSiMibRev=hpnsaSiMibRev, hpnsaSiRemoteLocatorLED=hpnsaSiRemoteLocatorLED, hpnsaSiSecurity=hpnsaSiSecurity, hpnsaSiFloppyDrive=hpnsaSiFloppyDrive, hpnsaSiKbdMouseInactivityTO=hpnsaSiKbdMouseInactivityTO, hpnsaSiPortType=hpnsaSiPortType, hpnsaSiMemSpeed=hpnsaSiMemSpeed, hpnsaSiRemoteLocatorLEDStatus=hpnsaSiRemoteLocatorLEDStatus, hpnsaSiPortEntry=hpnsaSiPortEntry, hpnsa=hpnsa, hpnsaSiModel=hpnsaSiModel, hpnsaSiAgentIndex=hpnsaSiAgentIndex, hpnsaSiSystemName=hpnsaSiSystemName, hpnsaSiVideoBIOSVersion=hpnsaSiVideoBIOSVersion, hpnsaSiOpSysVer=hpnsaSiOpSysVer, hpnsaSiMouseType=hpnsaSiMouseType, hpnsaSiExtMemSize=hpnsaSiExtMemSize, hpnsaSiNumCPU=hpnsaSiNumCPU, hpnsaSiKbdType=hpnsaSiKbdType, hpnsaSiNumFloppyDrives=hpnsaSiNumFloppyDrives, hpnsaSiFloppyDriveType=hpnsaSiFloppyDriveType, hpnsaSiFloppyDriveEntry=hpnsaSiFloppyDriveEntry, hpnsaSiAgentTable=hpnsaSiAgentTable, hpnsaSystemInfo=hpnsaSystemInfo, hpnsaSiCPUTable=hpnsaSiCPUTable, hpnsaSiCPUModel=hpnsaSiCPUModel, hpnsaSiNumISASlots=hpnsaSiNumISASlots, hpnsaSiOpSysDescription=hpnsaSiOpSysDescription, hpnsaSiNetServerMode=hpnsaSiNetServerMode, hpnsaSiVideoBlankMode=hpnsaSiVideoBlankMode, hpnsaSiBaseMemSize=hpnsaSiBaseMemSize, hpnsaSiCPUEntry=hpnsaSiCPUEntry, hpnsaSiAgentName=hpnsaSiAgentName, hpnsaSiAgentVersion=hpnsaSiAgentVersion, hpnsaSiPortIndex=hpnsaSiPortIndex, hpnsaSiAgentDate=hpnsaSiAgentDate, hpnsaSiRemoteLocatorLEDSupported=hpnsaSiRemoteLocatorLEDSupported, hpnsaSiBootDiskPriority=hpnsaSiBootDiskPriority, hpnsaSiMemory=hpnsaSiMemory, hpnsaSiSCSIBIOSVersion=hpnsaSiSCSIBIOSVersion, hpnsaSiCPUSpeed=hpnsaSiCPUSpeed, hpnsaSiWriteToFloppy=hpnsaSiWriteToFloppy, hpnsaSiKeyboardLockPassword=hpnsaSiKeyboardLockPassword, hpnsaSiNumPCISlots=hpnsaSiNumPCISlots, hpnsaSiPortTable=hpnsaSiPortTable, hpnsaSiBasicInfo=hpnsaSiBasicInfo, hpnsaSiSystemID=hpnsaSiSystemID, hpnsaSiPort=hpnsaSiPort, hpnsaSiPortEndAddress=hpnsaSiPortEndAddress)
