#
# PySNMP MIB module DANWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DANWARE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ObjectIdentity, TimeTicks, Unsigned32, ModuleIdentity, MibIdentifier, IpAddress, Bits, Counter32, Gauge32, enterprises, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ObjectIdentity", "TimeTicks", "Unsigned32", "ModuleIdentity", "MibIdentifier", "IpAddress", "Bits", "Counter32", "Gauge32", "enterprises", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
danware = MibIdentifier((1, 3, 6, 1, 4, 1, 8116))
netop = MibIdentifier((1, 3, 6, 1, 4, 1, 8116, 2))
netopEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 8116, 2, 6))
netopManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 8116, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netopManufacturer.setStatus('mandatory')
netopProducts = MibScalar((1, 3, 6, 1, 4, 1, 8116, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 10, 20, 21, 22, 23, 24, 25, 30))).clone(namedValues=NamedValues(("unknown", 0), ("guest", 1), ("teacher", 10), ("host", 20), ("nameserver", 21), ("gateway", 22), ("logserver", 23), ("accessserver", 24), ("classserver", 25), ("student", 30)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: netopProducts.setStatus('mandatory')
netopVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 8116, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netopVersionNumber.setStatus('mandatory')
netopStatus = MibScalar((1, 3, 6, 1, 4, 1, 8116, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netopStatus.setStatus('mandatory')
netopCallHost = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,0))
netopHangupHost = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,1))
netopStartHelp = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,2))
netopStopHelp = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,3))
netopHelpDefined = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,4))
netopHelpDeleted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,5))
netopHelpReqReceived = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,6))
netopHelpReqCancel = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,7))
netopSesRecStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,8))
netopSesRecStop = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,9))
netopACLogin = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,10))
netopACLogOff = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,11))
netopUnknown = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,12))
netopHostStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,32))
netopHostStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,33))
netopStartRemoteCtrl = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,34))
netopStopRemoteCtrl = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,35))
netopStartCallback = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,36))
netopHelpReqSent = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,37))
netopHstHelpReqCancel = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,38))
netopIndvSeqEnab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,39))
netopIndvSeqDisab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,40))
netopSecRoleAdded = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,41))
netopSecRoleDeleted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,42))
netopSecRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,43))
netopGstGrpAdded = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,44))
netopGstGrpDeleted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,45))
netopGstGrpChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,46))
netopPWEnabled = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,47))
netopPWDisabled = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,48))
netopPWChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,49))
netopCallBEnabled = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,50))
netopCallBDisabled = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,51))
netopCallBChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,52))
netopConfAccEnab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,53))
netopConfAccDisab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,54))
netopGatewCallb = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,64))
netopGatewIndvDef = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,65))
netopGatewIndvDEL = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,66))
netopGatewGstAdded = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,67))
netopGatewGstDelete = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,68))
netopGatewGstChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,69))
netopGatewPWEnab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,70))
netopGatewPWDisab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,71))
netopGatewPWChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,72))
netopGatewCallbEnab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,73))
netopGatewCallbDisab = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,74))
netopGatewCallbChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,75))
netopFileReceive = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,96))
netopFileSent = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,97))
netopBooted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,98))
netopConectionLost = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,99))
netopPassWordRejected = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,100))
netopConfAccessDenied = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,101))
netopASPWRejected = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,102))
netopASAdminChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,103))
netopEventLoggingFailed = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,112))
netopSNMPLoggingFailed = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,113))
netopRCStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,114))
netopRCStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,115))
netopFileTrStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,116))
netopFileTrStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,117))
netopGChatStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,118))
netopGChatStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,119))
netopGAudioStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,120))
netopGAudioStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,121))
netopClipReceived = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,122))
netopClipSent = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,123))
netopRrintReceived = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,124))
netopPrintSent = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,125))
netopCommProfileStart = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,126))
netopCommProfileStop = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,127))
netopLogLocalOn = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,128))
netopLogLocalOff = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,129))
netopLogLocalChange = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,130))
netopLogServerOn = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,131))
netopLogServerOff = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,132))
netopIsLogServer = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,133))
netopIsNotLogServer = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,134))
netopLogEventlogOn = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,135))
netopLogEventlogOff = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,136))
netopLogSNMPOn = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,137))
netopLogSNMPOff = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,138))
netopKbdLock = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,139))
netopKbdUnlock = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,140))
netopScrBlank = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,141))
netopScrUnblank = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,142))
netopLogoff = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,143))
netopGWLogin = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,144))
netopOptWaitStart = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,145))
netopOptLoadStar = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,146))
netopOptMinStart = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,147))
netopOptStealth = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,148))
netopOptMinConn = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,149))
netopOptOnTop = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,150))
netopOptShowFile = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,151))
netopOptKeepAlive = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,152))
netopOptBootHangUp = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,153))
netopOptLogOffHangUp = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,154))
netopOptNaming = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,155))
netopOptPublic = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,156))
netopOptNotification = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,157))
netopOptHlpDescr = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,158))
netopOptHlpProvid = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,159))
netopOptHlpComm = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,160))
netopOptHlpAdr = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,161))
netopOptHlpIcon = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,162))
netopOptAudDuplex = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,163))
netopOptAudSilence = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,164))
netopOptAudLineHold = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,165))
netopOptNNSChg = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,166))
netopMaintGuest = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,167))
netopMaintGW = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,168))
netopMaintOther = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,169))
netopMaintExit = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,170))
netopMaintProtect = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,171))
netopMaintPW = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,172))
netopAccessAllowance = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,173))
netopAccessMACIP = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,174))
netopAccessFTrans = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,175))
netopSSGroupIDChg = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,176))
netopPWRejectLimit = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,177))
netopNameServerStart = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,178))
netopNameServerStop = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,179))
netopSecurityServerStart = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,180))
netopSecurityServerStop = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,181))
netopGatewayStart = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,182))
netopGatwayStop = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,183))
netopOptLockHangUp = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,184))
netopOptNothingHangUp = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,185))
netopOptUserName = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,186))
netopFMStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,187))
netopFMStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,188))
netopHChatStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,189))
netopHChatStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,190))
netopHAudioStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,191))
netopHAudioStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,192))
netopCommunicationStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,193))
netopCommunicationStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,194))
netopRunScript = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,195))
netopRunProgram = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,196))
netopExecuteCommand = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,197))
netopGatewGrpDefined = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,198))
netopGatewGrpDeleted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,199))
netopGatewAccessAllowed = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,200))
netopGatewNNSGDIChanged = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,201))
netopAccessServerPWChanged = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,202))
netopInventoryReceived = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,203))
netopMessageSent = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,204))
netopInventorySent = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,205))
netopMessageReceived = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,206))
netopTimeoutLimitExeded = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,207))
netopAuthenticatedUser = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,208))
netopGatewayPWRejected = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,209))
netopWebUpdateCheck = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,210))
netopWebUpdateDownload = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,211))
netopWebUpdateInstall = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,212))
netopWebUpdateSuccess = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,213))
netopWebUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,214))
netopClassServerStart = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,215))
netopClassServerStop = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,216))
netopOptMultiGuest = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,217))
netopRemoteMgmStarted = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,218))
netopRemoteMgmStopped = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,219))
netopRemoteMgmStarted2 = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,220))
netopRemoteMgmStopped2 = NotificationType((1, 3, 6, 1, 4, 1, 8116, 2, 6) + (0,221))
mibBuilder.exportSymbols("DANWARE-MIB", netopEvent=netopEvent, netopGatewCallbEnab=netopGatewCallbEnab, netopMaintOther=netopMaintOther, netopOptKeepAlive=netopOptKeepAlive, netopGatewPWDisab=netopGatewPWDisab, netopSecRoleChange=netopSecRoleChange, netopCallBEnabled=netopCallBEnabled, netopSesRecStop=netopSesRecStop, netopOptShowFile=netopOptShowFile, netopCommunicationStarted=netopCommunicationStarted, netopMessageReceived=netopMessageReceived, netopHAudioStarted=netopHAudioStarted, netopGatewayStart=netopGatewayStart, netopRCStopped=netopRCStopped, netopGatewIndvDef=netopGatewIndvDef, netopOptWaitStart=netopOptWaitStart, netopOptHlpIcon=netopOptHlpIcon, netopOptNaming=netopOptNaming, netopOptNNSChg=netopOptNNSChg, netopStatus=netopStatus, netopOptUserName=netopOptUserName, netopHangupHost=netopHangupHost, netopACLogOff=netopACLogOff, netopOptStealth=netopOptStealth, netopPrintSent=netopPrintSent, netopVersionNumber=netopVersionNumber, netopKbdLock=netopKbdLock, netopLogLocalOn=netopLogLocalOn, netopWebUpdateInstall=netopWebUpdateInstall, netop=netop, netopGWLogin=netopGWLogin, netopGatwayStop=netopGatwayStop, netopOptHlpProvid=netopOptHlpProvid, netopGatewGstDelete=netopGatewGstDelete, netopOptAudDuplex=netopOptAudDuplex, netopIndvSeqDisab=netopIndvSeqDisab, netopRemoteMgmStarted=netopRemoteMgmStarted, netopOptPublic=netopOptPublic, netopFileReceive=netopFileReceive, netopMaintGW=netopMaintGW, netopCallBDisabled=netopCallBDisabled, netopGChatStopped=netopGChatStopped, netopOptOnTop=netopOptOnTop, netopLogoff=netopLogoff, netopASPWRejected=netopASPWRejected, netopOptLockHangUp=netopOptLockHangUp, netopAccessAllowance=netopAccessAllowance, netopGatewCallbDisab=netopGatewCallbDisab, netopGatewPWChange=netopGatewPWChange, netopFileTrStopped=netopFileTrStopped, netopNameServerStop=netopNameServerStop, netopGatewPWEnab=netopGatewPWEnab, netopFileTrStarted=netopFileTrStarted, netopGatewIndvDEL=netopGatewIndvDEL, danware=danware, netopStopHelp=netopStopHelp, netopSecRoleAdded=netopSecRoleAdded, netopGatewayPWRejected=netopGatewayPWRejected, netopEventLoggingFailed=netopEventLoggingFailed, netopClipSent=netopClipSent, netopGAudioStopped=netopGAudioStopped, netopPWRejectLimit=netopPWRejectLimit, netopIsNotLogServer=netopIsNotLogServer, netopMaintProtect=netopMaintProtect, netopScrBlank=netopScrBlank, netopClassServerStart=netopClassServerStart, netopOptBootHangUp=netopOptBootHangUp, netopRunProgram=netopRunProgram, netopGatewGrpDefined=netopGatewGrpDefined, netopStartCallback=netopStartCallback, netopSSGroupIDChg=netopSSGroupIDChg, netopBooted=netopBooted, netopOptMinStart=netopOptMinStart, netopCommProfileStart=netopCommProfileStart, netopACLogin=netopACLogin, netopGatewGrpDeleted=netopGatewGrpDeleted, netopInventorySent=netopInventorySent, netopRemoteMgmStopped=netopRemoteMgmStopped, netopASAdminChange=netopASAdminChange, netopScrUnblank=netopScrUnblank, netopLogSNMPOn=netopLogSNMPOn, netopSecurityServerStart=netopSecurityServerStart, netopClipReceived=netopClipReceived, netopCallBChange=netopCallBChange, netopLogLocalChange=netopLogLocalChange, netopOptMultiGuest=netopOptMultiGuest, netopGChatStarted=netopGChatStarted, netopOptHlpComm=netopOptHlpComm, netopRemoteMgmStopped2=netopRemoteMgmStopped2, netopConfAccessDenied=netopConfAccessDenied, netopCommunicationStopped=netopCommunicationStopped, netopGatewAccessAllowed=netopGatewAccessAllowed, netopTimeoutLimitExeded=netopTimeoutLimitExeded, netopAccessFTrans=netopAccessFTrans, netopSecRoleDeleted=netopSecRoleDeleted, netopPassWordRejected=netopPassWordRejected, netopFMStarted=netopFMStarted, netopOptHlpDescr=netopOptHlpDescr, netopGstGrpDeleted=netopGstGrpDeleted, netopLogLocalOff=netopLogLocalOff, netopSesRecStarted=netopSesRecStarted, netopAccessMACIP=netopAccessMACIP, netopLogSNMPOff=netopLogSNMPOff, netopWebUpdateSuccess=netopWebUpdateSuccess, netopHstHelpReqCancel=netopHstHelpReqCancel, netopStopRemoteCtrl=netopStopRemoteCtrl, netopMaintPW=netopMaintPW, netopSecurityServerStop=netopSecurityServerStop, netopHelpDefined=netopHelpDefined, netopConfAccDisab=netopConfAccDisab, netopOptAudSilence=netopOptAudSilence, netopClassServerStop=netopClassServerStop, netopFileSent=netopFileSent, netopStartRemoteCtrl=netopStartRemoteCtrl, netopAccessServerPWChanged=netopAccessServerPWChanged, netopWebUpdateFailed=netopWebUpdateFailed, netopOptNothingHangUp=netopOptNothingHangUp, netopLogEventlogOff=netopLogEventlogOff, netopMaintGuest=netopMaintGuest, netopHelpReqSent=netopHelpReqSent, netopProducts=netopProducts, netopOptAudLineHold=netopOptAudLineHold, netopHelpDeleted=netopHelpDeleted, netopGatewCallb=netopGatewCallb, netopMessageSent=netopMessageSent, netopRemoteMgmStarted2=netopRemoteMgmStarted2, netopGatewNNSGDIChanged=netopGatewNNSGDIChanged, netopIndvSeqEnab=netopIndvSeqEnab, netopHAudioStopped=netopHAudioStopped, netopWebUpdateCheck=netopWebUpdateCheck, netopWebUpdateDownload=netopWebUpdateDownload, netopOptLogOffHangUp=netopOptLogOffHangUp, netopKbdUnlock=netopKbdUnlock, netopLogEventlogOn=netopLogEventlogOn, netopGstGrpAdded=netopGstGrpAdded, netopOptLoadStar=netopOptLoadStar, netopConfAccEnab=netopConfAccEnab, netopRunScript=netopRunScript, netopOptHlpAdr=netopOptHlpAdr, netopMaintExit=netopMaintExit, netopPWEnabled=netopPWEnabled, netopGatewCallbChange=netopGatewCallbChange, netopCommProfileStop=netopCommProfileStop, netopLogServerOff=netopLogServerOff, netopPWDisabled=netopPWDisabled, netopPWChange=netopPWChange, netopGatewGstChange=netopGatewGstChange, netopManufacturer=netopManufacturer, netopHelpReqReceived=netopHelpReqReceived, netopRrintReceived=netopRrintReceived, netopOptMinConn=netopOptMinConn, netopStartHelp=netopStartHelp, netopNameServerStart=netopNameServerStart, netopUnknown=netopUnknown, netopOptNotification=netopOptNotification, netopExecuteCommand=netopExecuteCommand, netopAuthenticatedUser=netopAuthenticatedUser, netopHostStopped=netopHostStopped, netopGstGrpChange=netopGstGrpChange, netopLogServerOn=netopLogServerOn, netopFMStopped=netopFMStopped, netopInventoryReceived=netopInventoryReceived, netopIsLogServer=netopIsLogServer, netopHelpReqCancel=netopHelpReqCancel, netopSNMPLoggingFailed=netopSNMPLoggingFailed, netopHChatStarted=netopHChatStarted, netopRCStarted=netopRCStarted, netopGatewGstAdded=netopGatewGstAdded, netopConectionLost=netopConectionLost, netopHChatStopped=netopHChatStopped, netopCallHost=netopCallHost, netopHostStarted=netopHostStarted, netopGAudioStarted=netopGAudioStarted)
