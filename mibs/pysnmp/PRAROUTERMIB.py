#
# PySNMP MIB module PRAROUTERMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PRAROUTERMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, Gauge32, TimeTicks, IpAddress, ModuleIdentity, iso, Counter32, MibIdentifier, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Gauge32", "TimeTicks", "IpAddress", "ModuleIdentity", "iso", "Counter32", "MibIdentifier", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
itk = MibIdentifier((1, 3, 6, 1, 4, 1, 1195))
pramib = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3))
config = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 1))
prasoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3))
status = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 2))
channels = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 2, 1))
watchdog = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 2, 2))
fault = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3))
performance = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 3))
cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 3, 1))
sessions = MibIdentifier((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2))
praVersion = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: praVersion.setStatus('mandatory')
asIpTable = MibTable((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: asIpTable.setStatus('mandatory')
asIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2, 1), ).setMaxAccess("readonly").setIndexNames((0, "PRAROUTERMIB", "asNumber"))
if mibBuilder.loadTexts: asIpEntry.setStatus('mandatory')
asNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asNumber.setStatus('mandatory')
asIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asIpAddr.setStatus('mandatory')
linecntPspdn = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linecntPspdn.setStatus('mandatory')
linecntPspdnPerBchannel = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linecntPspdnPerBchannel.setStatus('mandatory')
linecntPspdnPh = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linecntPspdnPh.setStatus('mandatory')
linecntMax = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linecntMax.setStatus('mandatory')
asIpAddrTableMaxIndex = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asIpAddrTableMaxIndex.setStatus('mandatory')
numberOfEngagedBchan = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfEngagedBchan.setStatus('mandatory')
numberOfFreeBchan = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfFreeBchan.setStatus('mandatory')
numberOfTransToAs = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfTransToAs.setStatus('mandatory')
numberOfRecvToAs = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfRecvToAs.setStatus('mandatory')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('mandatory')
isdnMuxOk = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnMuxOk.setStatus('mandatory')
modemAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2), )
if mibBuilder.loadTexts: modemAdapterTable.setStatus('mandatory')
modemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1), ).setIndexNames((0, "PRAROUTERMIB", "modemCardNumber"))
if mibBuilder.loadTexts: modemEntry.setStatus('mandatory')
modemCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemCardNumber.setStatus('mandatory')
modemAdapterOk = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemAdapterOk.setStatus('mandatory')
modem1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem1.setStatus('mandatory')
modem2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem2.setStatus('mandatory')
modem3 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem3.setStatus('mandatory')
modem4 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem4.setStatus('mandatory')
modem5 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem5.setStatus('mandatory')
modem6 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem6.setStatus('mandatory')
modem7 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem7.setStatus('mandatory')
modem8 = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modem8.setStatus('mandatory')
practrlOk = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: practrlOk.setStatus('mandatory')
isdnInOk = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnInOk.setStatus('mandatory')
isdnOutOk = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnOutOk.setStatus('mandatory')
pstnInOk = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pstnInOk.setStatus('mandatory')
pspdnOk = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pspdnOk.setStatus('mandatory')
modemCardMax = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 2, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemCardMax.setStatus('mandatory')
cpuCapacity = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuCapacity.setStatus('mandatory')
sessionTable = MibTable((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1), )
if mibBuilder.loadTexts: sessionTable.setStatus('mandatory')
sessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1), ).setIndexNames((0, "PRAROUTERMIB", "sessionNumber"))
if mibBuilder.loadTexts: sessionEntry.setStatus('mandatory')
sessionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionNumber.setStatus('mandatory')
sessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionType.setStatus('mandatory')
b2Protocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: b2Protocol.setStatus('mandatory')
cntRcvByteCapi = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvByteCapi.setStatus('mandatory')
cntSndByteCapi = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndByteCapi.setStatus('mandatory')
cntRcvMsgCapi = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvMsgCapi.setStatus('mandatory')
cntSndMsgCapi = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndMsgCapi.setStatus('mandatory')
cntRcvBytePsp = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvBytePsp.setStatus('mandatory')
cntSndBytePsp = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndBytePsp.setStatus('mandatory')
cntRcvMsgPsp = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvMsgPsp.setStatus('mandatory')
cntSndMsgPsp = MibTableColumn((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndMsgPsp.setStatus('mandatory')
cntRcvTotalByteCapi = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvTotalByteCapi.setStatus('mandatory')
cntSndTotalByteCapi = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndTotalByteCapi.setStatus('mandatory')
cntRcvTotalMsgCapi = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvTotalMsgCapi.setStatus('mandatory')
cntSndTotalMsgCapi = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndTotalMsgCapi.setStatus('mandatory')
cntRcvTotalBytePsp = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvTotalBytePsp.setStatus('mandatory')
cntSndTotalBytePsp = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndTotalBytePsp.setStatus('mandatory')
cntRcvTotalMsgPsp = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntRcvTotalMsgPsp.setStatus('mandatory')
cntSndTotalMsgPsp = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntSndTotalMsgPsp.setStatus('mandatory')
sessionTableMaxIndex = MibScalar((1, 3, 6, 1, 4, 1, 1195, 3, 3, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionTableMaxIndex.setStatus('mandatory')
mibBuilder.exportSymbols("PRAROUTERMIB", numberOfFreeBchan=numberOfFreeBchan, config=config, pramib=pramib, modem1=modem1, pspdnOk=pspdnOk, asIpAddr=asIpAddr, isdnOutOk=isdnOutOk, sessionNumber=sessionNumber, isdnInOk=isdnInOk, sessionEntry=sessionEntry, cntSndBytePsp=cntSndBytePsp, watchdog=watchdog, cntSndTotalBytePsp=cntSndTotalBytePsp, asNumber=asNumber, modem7=modem7, modem5=modem5, modem8=modem8, channels=channels, modemCardNumber=modemCardNumber, fault=fault, temperature=temperature, linecntMax=linecntMax, modemEntry=modemEntry, b2Protocol=b2Protocol, cntSndTotalByteCapi=cntSndTotalByteCapi, cntSndMsgCapi=cntSndMsgCapi, modemCardMax=modemCardMax, itk=itk, asIpTable=asIpTable, cntSndMsgPsp=cntSndMsgPsp, cntRcvBytePsp=cntRcvBytePsp, asIpEntry=asIpEntry, cntRcvTotalMsgPsp=cntRcvTotalMsgPsp, status=status, numberOfTransToAs=numberOfTransToAs, prasoftware=prasoftware, cpu=cpu, modemAdapterOk=modemAdapterOk, praVersion=praVersion, practrlOk=practrlOk, cntSndTotalMsgCapi=cntSndTotalMsgCapi, numberOfRecvToAs=numberOfRecvToAs, modem4=modem4, modem6=modem6, modem3=modem3, sessions=sessions, cntRcvTotalMsgCapi=cntRcvTotalMsgCapi, isdnMuxOk=isdnMuxOk, cntSndTotalMsgPsp=cntSndTotalMsgPsp, asIpAddrTableMaxIndex=asIpAddrTableMaxIndex, sessionTableMaxIndex=sessionTableMaxIndex, modem2=modem2, linecntPspdnPh=linecntPspdnPh, cntRcvMsgCapi=cntRcvMsgCapi, modemAdapterTable=modemAdapterTable, cntRcvByteCapi=cntRcvByteCapi, sessionType=sessionType, pstnInOk=pstnInOk, sessionTable=sessionTable, cntRcvTotalByteCapi=cntRcvTotalByteCapi, cpuCapacity=cpuCapacity, linecntPspdnPerBchannel=linecntPspdnPerBchannel, numberOfEngagedBchan=numberOfEngagedBchan, performance=performance, cntRcvTotalBytePsp=cntRcvTotalBytePsp, cntRcvMsgPsp=cntRcvMsgPsp, cntSndByteCapi=cntSndByteCapi, linecntPspdn=linecntPspdn)
