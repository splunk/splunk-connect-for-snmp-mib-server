#
# PySNMP MIB module SW-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW-TRUNK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:05:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Gauge32, ObjectIdentity, Integer32, Counter32, ModuleIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Unsigned32, MibIdentifier, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "ObjectIdentity", "Integer32", "Counter32", "ModuleIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class TrunkSetList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

marconi = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
external = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
dlinkcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
es2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
marconi_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("marconi-mgmt")
es2000Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28))
swL2Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2))
swPortTrunk = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6))
swPortTrunkCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1), )
if mibBuilder.loadTexts: swPortTrunkCtrlTable.setStatus('mandatory')
swPortTrunkCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1), ).setIndexNames((0, "SW-TRUNK-MIB", "swPortTrunkCtrlIndex"))
if mibBuilder.loadTexts: swPortTrunkCtrlEntry.setStatus('mandatory')
swPortTrunkCtrlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkCtrlIndex.setStatus('mandatory')
swPortTrunkCtrlAnchorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortTrunkCtrlAnchorPort.setStatus('mandatory')
swPortTrunkCtrlMasterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkCtrlMasterPort.setStatus('mandatory')
swPortTrunkCtrlName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortTrunkCtrlName.setStatus('mandatory')
swPortTrunkCtrlMember = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 5), TrunkSetList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortTrunkCtrlMember.setStatus('mandatory')
swPortTrunkCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortTrunkCtrlState.setStatus('mandatory')
swPortTrunkMemberTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2), )
if mibBuilder.loadTexts: swPortTrunkMemberTable.setStatus('mandatory')
swPortTrunkMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1), ).setIndexNames((0, "SW-TRUNK-MIB", "swPortTrunkMemberIndex"), (0, "SW-TRUNK-MIB", "swPortTrunkMemberUnitIndex"), (0, "SW-TRUNK-MIB", "swPortTrunkMemberModuleIndex"), (0, "SW-TRUNK-MIB", "swPortTrunkMemberPortIndex"))
if mibBuilder.loadTexts: swPortTrunkMemberEntry.setStatus('mandatory')
swPortTrunkMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkMemberIndex.setStatus('mandatory')
swPortTrunkMemberUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkMemberUnitIndex.setStatus('mandatory')
swPortTrunkMemberModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkMemberModuleIndex.setStatus('mandatory')
swPortTrunkMemberPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 6, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkMemberPortIndex.setStatus('mandatory')
mibBuilder.exportSymbols("SW-TRUNK-MIB", TrunkSetList=TrunkSetList, swPortTrunkMemberIndex=swPortTrunkMemberIndex, swPortTrunkCtrlAnchorPort=swPortTrunkCtrlAnchorPort, marconi=marconi, swPortTrunkCtrlName=swPortTrunkCtrlName, swPortTrunkCtrlTable=swPortTrunkCtrlTable, dlinkcommon=dlinkcommon, external=external, swPortTrunkCtrlIndex=swPortTrunkCtrlIndex, swPortTrunkMemberPortIndex=swPortTrunkMemberPortIndex, swPortTrunkMemberUnitIndex=swPortTrunkMemberUnitIndex, systems=systems, dlink=dlink, swPortTrunkMemberModuleIndex=swPortTrunkMemberModuleIndex, swPortTrunkCtrlEntry=swPortTrunkCtrlEntry, golfcommon=golfcommon, swPortTrunkMemberEntry=swPortTrunkMemberEntry, swPortTrunkCtrlMember=swPortTrunkCtrlMember, es2000Mgmt=es2000Mgmt, golf=golf, swPortTrunkMemberTable=swPortTrunkMemberTable, swPortTrunk=swPortTrunk, swPortTrunkCtrlState=swPortTrunkCtrlState, swPortTrunkCtrlMasterPort=swPortTrunkCtrlMasterPort, marconi_mgmt=marconi_mgmt, swL2Mgmt=swL2Mgmt, es2000=es2000, golfproducts=golfproducts)
