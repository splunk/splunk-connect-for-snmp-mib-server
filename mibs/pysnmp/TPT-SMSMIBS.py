#
# PySNMP MIB module TPT-SMSMIBS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-SMSMIBS
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, TimeTicks, Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Counter64, ModuleIdentity, NotificationType, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_reg, tpt_products = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg", "tpt-products")
tpt_smsMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4)).setLabel("tpt-smsMIBs")
if mibBuilder.loadTexts: tpt_smsMIBs.setLastUpdated('0508121508Z')
if mibBuilder.loadTexts: tpt_smsMIBs.setOrganization('TippingPoint Technologies, Inc.')
tpt_sms_conf = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 1)).setLabel("tpt-sms-conf")
if mibBuilder.loadTexts: tpt_sms_conf.setStatus('current')
tpt_sms_objs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 2)).setLabel("tpt-sms-objs")
if mibBuilder.loadTexts: tpt_sms_objs.setStatus('current')
tpt_sms_events = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3)).setLabel("tpt-sms-events")
if mibBuilder.loadTexts: tpt_sms_events.setStatus('current')
tpt_sms_groups = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1)).setLabel("tpt-sms-groups")
if mibBuilder.loadTexts: tpt_sms_groups.setStatus('current')
tpt_sms_compls = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 2)).setLabel("tpt-sms-compls")
if mibBuilder.loadTexts: tpt_sms_compls.setStatus('current')
tpt_sms_eventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0)).setLabel("tpt-sms-eventsV2")
if mibBuilder.loadTexts: tpt_sms_eventsV2.setStatus('current')
tpt_sms_notifypayload = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1)).setLabel("tpt-sms-notifypayload")
if mibBuilder.loadTexts: tpt_sms_notifypayload.setStatus('current')
tpt_sms_family = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4)).setLabel("tpt-sms-family")
if mibBuilder.loadTexts: tpt_sms_family.setStatus('current')
tpt_sms_model_1750 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 1)).setLabel("tpt-sms-model-1750")
if mibBuilder.loadTexts: tpt_sms_model_1750.setStatus('deprecated')
tpt_sms_model_1850 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 2)).setLabel("tpt-sms-model-1850")
if mibBuilder.loadTexts: tpt_sms_model_1850.setStatus('deprecated')
tpt_sms_model_1950 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 3)).setLabel("tpt-sms-model-1950")
if mibBuilder.loadTexts: tpt_sms_model_1950.setStatus('deprecated')
tpt_sms_model_vmware = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 4)).setLabel("tpt-sms-model-vmware")
if mibBuilder.loadTexts: tpt_sms_model_vmware.setStatus('deprecated')
tpt_sms_model_h1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 5)).setLabel("tpt-sms-model-h1")
if mibBuilder.loadTexts: tpt_sms_model_h1.setStatus('current')
tpt_sms_model_xl = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 6)).setLabel("tpt-sms-model-xl")
if mibBuilder.loadTexts: tpt_sms_model_xl.setStatus('current')
tpt_sms_model_vsms = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 7)).setLabel("tpt-sms-model-vsms")
if mibBuilder.loadTexts: tpt_sms_model_vsms.setStatus('current')
tpt_sms_model_hp_2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 8)).setLabel("tpt-sms-model-hp-2000")
if mibBuilder.loadTexts: tpt_sms_model_hp_2000.setStatus('current')
tpt_sms_model_hp_xl2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 9)).setLabel("tpt-sms-model-hp-xl2000")
if mibBuilder.loadTexts: tpt_sms_model_hp_xl2000.setStatus('current')
tpt_sms_model_vsmslite = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 10)).setLabel("tpt-sms-model-vsmslite")
if mibBuilder.loadTexts: tpt_sms_model_vsmslite.setStatus('current')
tpt_sms_model_h3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 11)).setLabel("tpt-sms-model-h3")
if mibBuilder.loadTexts: tpt_sms_model_h3.setStatus('current')
tpt_sms_model_h3_xl = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 4, 12)).setLabel("tpt-sms-model-h3-xl")
if mibBuilder.loadTexts: tpt_sms_model_h3_xl.setStatus('current')
mibBuilder.exportSymbols("TPT-SMSMIBS", tpt_sms_model_vmware=tpt_sms_model_vmware, tpt_sms_model_h1=tpt_sms_model_h1, tpt_sms_model_h3_xl=tpt_sms_model_h3_xl, tpt_sms_model_vsms=tpt_sms_model_vsms, tpt_sms_compls=tpt_sms_compls, tpt_sms_model_hp_2000=tpt_sms_model_hp_2000, tpt_sms_model_1950=tpt_sms_model_1950, tpt_sms_notifypayload=tpt_sms_notifypayload, tpt_sms_family=tpt_sms_family, tpt_smsMIBs=tpt_smsMIBs, PYSNMP_MODULE_ID=tpt_smsMIBs, tpt_sms_events=tpt_sms_events, tpt_sms_model_vsmslite=tpt_sms_model_vsmslite, tpt_sms_objs=tpt_sms_objs, tpt_sms_model_1750=tpt_sms_model_1750, tpt_sms_conf=tpt_sms_conf, tpt_sms_model_xl=tpt_sms_model_xl, tpt_sms_model_1850=tpt_sms_model_1850, tpt_sms_model_hp_xl2000=tpt_sms_model_hp_xl2000, tpt_sms_model_h3=tpt_sms_model_h3, tpt_sms_groups=tpt_sms_groups, tpt_sms_eventsV2=tpt_sms_eventsV2)
