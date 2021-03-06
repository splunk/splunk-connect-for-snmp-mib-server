#
# PySNMP MIB module APCODEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APCODEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ApPercentage, = mibBuilder.importSymbols("ACMEPACKET-TC", "ApPercentage")
apSigRealmStatsEntry, = mibBuilder.importSymbols("APSYSMGMT-MIB", "apSigRealmStatsEntry")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, ModuleIdentity, Gauge32, Bits, IpAddress, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Bits", "IpAddress", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apCodecModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 7))
apCodecModule.setRevisions(('2012-07-16 00:00', '2012-06-22 10:00',))
if mibBuilder.loadTexts: apCodecModule.setLastUpdated('201207160000Z')
if mibBuilder.loadTexts: apCodecModule.setOrganization('Acme Packet, Inc')
apCodecMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1))
apCodecRealmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1), )
if mibBuilder.loadTexts: apCodecRealmStatsTable.setStatus('current')
apCodecRealmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1), )
apSigRealmStatsEntry.registerAugmentions(("APCODEC-MIB", "apCodecRealmStatsEntry"))
apCodecRealmStatsEntry.setIndexNames(*apSigRealmStatsEntry.getIndexNames())
if mibBuilder.loadTexts: apCodecRealmStatsEntry.setStatus('current')
apCodecRealmCountOther = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountOther.setStatus('current')
apCodecRealmCountPCMU = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountPCMU.setStatus('current')
apCodecRealmCountPCMA = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountPCMA.setStatus('current')
apCodecRealmCountG722 = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG722.setStatus('current')
apCodecRealmCountG723 = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG723.setStatus('current')
apCodecRealmCountG726_16 = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 6), Counter32()).setLabel("apCodecRealmCountG726-16").setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG726_16.setStatus('current')
apCodecRealmCountG726_24 = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 7), Counter32()).setLabel("apCodecRealmCountG726-24").setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG726_24.setStatus('current')
apCodecRealmCountG726_32 = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 8), Counter32()).setLabel("apCodecRealmCountG726-32").setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG726_32.setStatus('current')
apCodecRealmCountG726_40 = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 9), Counter32()).setLabel("apCodecRealmCountG726-40").setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG726_40.setStatus('current')
apCodecRealmCountG728 = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG728.setStatus('current')
apCodecRealmCountG729 = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountG729.setStatus('current')
apCodecRealmCountGSM = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountGSM.setStatus('current')
apCodecRealmCountILBC = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountILBC.setStatus('current')
apCodecRealmCountAMR = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountAMR.setStatus('current')
apCodecRealmCountEVRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountEVRC.setStatus('current')
apCodecRealmCountH261 = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountH261.setStatus('current')
apCodecRealmCountH263 = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountH263.setStatus('current')
apCodecRealmCountT38 = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmCountT38.setStatus('current')
apCodecTranscodingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2))
apCodecTranscodingRealmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1), )
if mibBuilder.loadTexts: apCodecTranscodingRealmStatsTable.setStatus('current')
apCodecTranscodingRealmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1), )
apSigRealmStatsEntry.registerAugmentions(("APCODEC-MIB", "apCodecTranscodingRealmStatsEntry"))
apCodecTranscodingRealmStatsEntry.setIndexNames(*apSigRealmStatsEntry.getIndexNames())
if mibBuilder.loadTexts: apCodecTranscodingRealmStatsEntry.setStatus('current')
apCodecRealmSessionsTransparent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmSessionsTransparent.setStatus('current')
apCodecRealmSessionsTransrated = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmSessionsTransrated.setStatus('current')
apCodecRealmSessionsTranscoded = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecRealmSessionsTranscoded.setStatus('current')
class ApCodecDigitTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 0), ("none", 1), ("inband", 2), ("rfc2833", 3), ("noneDual", 4), ("inbandTrans", 5), ("inbandDual", 6), ("rfc2833Trans", 7), ("rfc2833Dual", 8))

apCodecTranscodingResourceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2))
apCodecTranscodingResourcesTotal = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecTranscodingResourcesTotal.setStatus('current')
apCodecTranscodingResourcesCurrent = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecTranscodingResourcesCurrent.setStatus('current')
apCodecTranscodingResourcesHigh = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecTranscodingResourcesHigh.setStatus('current')
apCodecTranscodingInUsePercentCurrent = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 4), ApPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecTranscodingInUsePercentCurrent.setStatus('current')
apCodecTranscodingInUsePercentHigh = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 2, 5), ApPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecTranscodingInUsePercentHigh.setStatus('current')
apCodecTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3), )
if mibBuilder.loadTexts: apCodecTable.setStatus('current')
apCodecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3, 1), ).setIndexNames((0, "APCODEC-MIB", "apCodecIndex"))
if mibBuilder.loadTexts: apCodecEntry.setStatus('current')
apCodecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: apCodecIndex.setStatus('current')
apCodecName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecName.setStatus('current')
apCodecPairStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4), )
if mibBuilder.loadTexts: apCodecPairStatsTable.setStatus('current')
apCodecPairStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1), ).setIndexNames((0, "APCODEC-MIB", "apCodecPairAIndex"), (0, "APCODEC-MIB", "apCodecPairBIndex"), (0, "APCODEC-MIB", "apCodecPairAPValue"), (0, "APCODEC-MIB", "apCodecPairBPValue"), (0, "APCODEC-MIB", "apCodecPairADigitType"), (0, "APCODEC-MIB", "apCodecPairBDigitType"))
if mibBuilder.loadTexts: apCodecPairStatsEntry.setStatus('current')
apCodecPairAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: apCodecPairAIndex.setStatus('current')
apCodecPairBIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: apCodecPairBIndex.setStatus('current')
apCodecPairAPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: apCodecPairAPValue.setStatus('current')
apCodecPairBPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: apCodecPairBPValue.setStatus('current')
apCodecPairADigitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 5), ApCodecDigitTypes())
if mibBuilder.loadTexts: apCodecPairADigitType.setStatus('current')
apCodecPairBDigitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 6), ApCodecDigitTypes())
if mibBuilder.loadTexts: apCodecPairBDigitType.setStatus('current')
apCodecPairTranscodingCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecPairTranscodingCurrent.setStatus('current')
apCodecPairTranscodingHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 7, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCodecPairTranscodingHigh.setStatus('current')
apCodecNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 3))
apCodecNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 4))
apCodecNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 4, 0))
apCodecConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5))
apCodecCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 1))
apCodecGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2))
apCodecNotificationsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 3))
apCodecRealmStatsObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 1)).setObjects(("APCODEC-MIB", "apCodecRealmCountOther"), ("APCODEC-MIB", "apCodecRealmCountPCMU"), ("APCODEC-MIB", "apCodecRealmCountPCMA"), ("APCODEC-MIB", "apCodecRealmCountG722"), ("APCODEC-MIB", "apCodecRealmCountG723"), ("APCODEC-MIB", "apCodecRealmCountG726_16"), ("APCODEC-MIB", "apCodecRealmCountG726_24"), ("APCODEC-MIB", "apCodecRealmCountG726_32"), ("APCODEC-MIB", "apCodecRealmCountG726_40"), ("APCODEC-MIB", "apCodecRealmCountG728"), ("APCODEC-MIB", "apCodecRealmCountG729"), ("APCODEC-MIB", "apCodecRealmCountGSM"), ("APCODEC-MIB", "apCodecRealmCountILBC"), ("APCODEC-MIB", "apCodecRealmCountH261"), ("APCODEC-MIB", "apCodecRealmCountH263"), ("APCODEC-MIB", "apCodecRealmCountT38"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmStatsObjectsGroup = apCodecRealmStatsObjectsGroup.setStatus('current')
apCodecMediaProcessingObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 2)).setObjects(("APCODEC-MIB", "apCodecRealmSessionsTransparent"), ("APCODEC-MIB", "apCodecRealmSessionsTransrated"), ("APCODEC-MIB", "apCodecRealmSessionsTranscoded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingObjectsGroup = apCodecMediaProcessingObjectsGroup.setStatus('current')
apCodecRealmStatsObjectsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 3)).setObjects(("APCODEC-MIB", "apCodecRealmCountAMR"), ("APCODEC-MIB", "apCodecRealmCountEVRC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmStatsObjectsGroup2 = apCodecRealmStatsObjectsGroup2.setStatus('current')
apCodecTranscodingStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 7, 5, 2, 4)).setObjects(("APCODEC-MIB", "apCodecTranscodingResourcesTotal"), ("APCODEC-MIB", "apCodecTranscodingResourcesCurrent"), ("APCODEC-MIB", "apCodecTranscodingResourcesHigh"), ("APCODEC-MIB", "apCodecTranscodingInUsePercentCurrent"), ("APCODEC-MIB", "apCodecTranscodingInUsePercentHigh"), ("APCODEC-MIB", "apCodecName"), ("APCODEC-MIB", "apCodecPairTranscodingCurrent"), ("APCODEC-MIB", "apCodecPairTranscodingHigh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsGroup = apCodecTranscodingStatsGroup.setStatus('current')
mibBuilder.exportSymbols("APCODEC-MIB", ApCodecDigitTypes=ApCodecDigitTypes, apCodecRealmCountG726_32=apCodecRealmCountG726_32, apCodecRealmCountG728=apCodecRealmCountG728, apCodecNotificationObjects=apCodecNotificationObjects, apCodecTranscodingInUsePercentHigh=apCodecTranscodingInUsePercentHigh, apCodecPairBDigitType=apCodecPairBDigitType, apCodecPairTranscodingCurrent=apCodecPairTranscodingCurrent, apCodecRealmStatsEntry=apCodecRealmStatsEntry, apCodecPairBIndex=apCodecPairBIndex, apCodecMediaProcessingObjectsGroup=apCodecMediaProcessingObjectsGroup, apCodecTranscodingResourceMIBObjects=apCodecTranscodingResourceMIBObjects, apCodecPairStatsEntry=apCodecPairStatsEntry, apCodecPairBPValue=apCodecPairBPValue, apCodecRealmCountEVRC=apCodecRealmCountEVRC, apCodecPairTranscodingHigh=apCodecPairTranscodingHigh, apCodecMIBObjects=apCodecMIBObjects, apCodecRealmCountG723=apCodecRealmCountG723, apCodecName=apCodecName, apCodecRealmCountGSM=apCodecRealmCountGSM, apCodecRealmCountAMR=apCodecRealmCountAMR, apCodecModule=apCodecModule, apCodecRealmCountPCMA=apCodecRealmCountPCMA, apCodecRealmSessionsTransrated=apCodecRealmSessionsTransrated, apCodecEntry=apCodecEntry, apCodecRealmCountH263=apCodecRealmCountH263, apCodecRealmStatsObjectsGroup=apCodecRealmStatsObjectsGroup, apCodecPairStatsTable=apCodecPairStatsTable, apCodecPairAPValue=apCodecPairAPValue, apCodecRealmCountG726_40=apCodecRealmCountG726_40, apCodecRealmStatsTable=apCodecRealmStatsTable, apCodecRealmCountILBC=apCodecRealmCountILBC, apCodecTranscodingResourcesTotal=apCodecTranscodingResourcesTotal, apCodecTranscodingResourcesHigh=apCodecTranscodingResourcesHigh, apCodecRealmStatsObjectsGroup2=apCodecRealmStatsObjectsGroup2, apCodecGroups=apCodecGroups, PYSNMP_MODULE_ID=apCodecModule, apCodecConformance=apCodecConformance, apCodecNotificationsGroups=apCodecNotificationsGroups, apCodecNotifications=apCodecNotifications, apCodecTranscodingMIBObjects=apCodecTranscodingMIBObjects, apCodecTranscodingInUsePercentCurrent=apCodecTranscodingInUsePercentCurrent, apCodecRealmCountT38=apCodecRealmCountT38, apCodecRealmCountG726_24=apCodecRealmCountG726_24, apCodecTranscodingStatsGroup=apCodecTranscodingStatsGroup, apCodecRealmCountPCMU=apCodecRealmCountPCMU, apCodecTranscodingRealmStatsEntry=apCodecTranscodingRealmStatsEntry, apCodecNotificationPrefix=apCodecNotificationPrefix, apCodecIndex=apCodecIndex, apCodecPairAIndex=apCodecPairAIndex, apCodecRealmCountOther=apCodecRealmCountOther, apCodecRealmSessionsTranscoded=apCodecRealmSessionsTranscoded, apCodecRealmCountG722=apCodecRealmCountG722, apCodecRealmSessionsTransparent=apCodecRealmSessionsTransparent, apCodecTable=apCodecTable, apCodecRealmCountH261=apCodecRealmCountH261, apCodecRealmCountG729=apCodecRealmCountG729, apCodecRealmCountG726_16=apCodecRealmCountG726_16, apCodecPairADigitType=apCodecPairADigitType, apCodecTranscodingResourcesCurrent=apCodecTranscodingResourcesCurrent, apCodecCompliances=apCodecCompliances, apCodecTranscodingRealmStatsTable=apCodecTranscodingRealmStatsTable)
