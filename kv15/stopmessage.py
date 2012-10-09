from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

from enum.messagepriority import MessagePriority
from enum.messagetype import MessageType
from enum.messagedurationtype import MessageDurationType
from enum.reason import ReasonType
from enum.reason import SubReasonType
from enum.effect import EffectType
from enum.effect import SubEffectType
from enum.measure import MeasureType
from enum.measure import SubMeasureType
from enum.advice import AdviceType
from enum.advice import SubAdviceType

class StopMessage():
	def __init__(self, dataownercode='openOV', messagecontent=None, userstopcodes=None):
		self.subscriberid = 'openOV'		

		self.dataownercode = dataownercode
		self.messagecodedate = date.today()
		self.messagecodenumber = 0

		if userstopcodes is None:
			self.userstopcodes = []
		else:
			self.userstopcodes = userstopcodes
		
		self.messagepriority = MessagePriority.PTPROCESS
		self.messagetype = MessageType.GENERAL
		self.messagedurationtype = MessageDurationType.ENDTIME

		self.messagestarttime = datetime.now()
		self.messageendtime = datetime.combine(date.today() + timedelta(days = 1), time(4, 0, 0))

		if messagecontent is None:
			self.messagecontent = ''
		else:
			self.messagecontent = messagecontent

		self.reasontype = ReasonType.ONGEDEFINIEERD
		self.subreasontype = SubReasonType.ONBEKEND
		self.reasoncontent = ''

		self.effecttype = EffectType.ONGEDEFINIEERD
		self.subeffecttype = SubEffectType.ONBEKEND
		self.effectcontent = ''

		self.measuretype = MeasureType.ONGEDEFINIEERD
		self.submeasuretype = SubMeasureType.GEEN
		self.measurecontent = ''
		
		self.advicetype = AdviceType.ONGEDEFINIEERD
		self.subadvicetype = SubAdviceType.GEEN
		self.advicecontent = ''

		self.messagetimestamp = datetime.now()
	
	def __str__(self):
		data = {'dataownercode': self.dataownercode,
			'messagetimestamp': self.messagetimestamp.replace(microsecond=0).isoformat(),
			'messagecodedate': self.messagecodedate,
			'messagecodenumber': self.messagecodenumber,
			'messagepriority': self.messagepriority,
			'messagetype': self.messagetype,
			'messagedurationtype': self.messagedurationtype,
			'messagestarttime': self.messagestarttime.replace(microsecond=0).isoformat(),
			'messageendtime': self.messageendtime.replace(microsecond=0).isoformat(),
			'messagecontent': self.messagecontent,
			'reasontype': self.reasontype,
			'subreasontype': self.subreasontype,
			'reasoncontent': self.reasoncontent,
			'effecttype': self.effecttype,
			'subeffecttype': self.subeffecttype,
			'effectcontent': self.effectcontent,
			'measuretype': self.measuretype,
			'submeasuretype': self.submeasuretype,
			'measurecontent': self.measurecontent,
			'advicetype': self.advicetype,
			'subadvicetype': self.subadvicetype,
			'advicecontent': self.advicecontent}

		xml = """		<tmi8:STOPMESSAGE>
			<tmi8:dataownercode>%(dataownercode)s</tmi8:dataownercode>
			<tmi8:messagecodedate>%(messagecodedate)s</tmi8:messagecodedate>
			<tmi8:messagecodenumber>%(messagecodenumber)d</tmi8:messagecodenumber>
			<tmi8:userstopcodes>\n""" % data

		for userstopcode in self.userstopcodes:
			xml += """				<tmi8:userstopcode>%(userstopcode)s</tmi8:userstopcode>\n""" % {'userstopcode': userstopcode}

		xml += """			</tmi8:userstopcodes>
			<tmi8:messagepriority>%(messagepriority)s</tmi8:messagepriority>
			<tmi8:messagetype>%(messagetype)s</tmi8:messagetype>
			<tmi8:messagedurationtype>%(messagedurationtype)s</tmi8:messagedurationtype>
			<tmi8:messagestarttime>%(messagestarttime)s</tmi8:messagestarttime>
			<tmi8:messageendtime>%(messageendtime)s</tmi8:messageendtime>
			<tmi8:messagecontent>%(messagecontent)s</tmi8:messagecontent>\n""" % data

		if self.reasontype != ReasonType.ONGEDEFINIEERD:
			xml += """			<tmi8:reasontype>%(reasontype)s</tmi8:reasontype>
				<tmi8:subreasontype>%(subreasontype)s</tmi8:subreasontype>
				<tmi8:reasoncontent>%(reasoncontent)s</tmi8:reasoncontent>\n""" % data

		if self.effecttype != EffectType.ONGEDEFINIEERD:
			xml += """			<tmi8:effecttype>%(effecttype)s</tmi8:effecttype>
			<tmi8:subeffecttype>%(subeffecttype)s</tmi8:subeffecttype>
			<tmi8:effectcontent>%(effectcontent)s</tmi8:effectcontent>\n""" % data

		if self.measuretype != MeasureType.ONGEDEFINIEERD:
			"""			<tmi8:measuretype>%(measuretype)s</tmi8:measuretype>
			<tmi8:submeasuretype>%(submeasuretype)s</tmi8:submeasuretype>
			<tmi8:measurecontent>%(measurecontent)s</tmi8:measurecontent>\n""" % data

		if self.advicetype != AdviceType.ONGEDEFINIEERD:
			"""			<tmi8:advicetype>%(advicetype)s</tmi8:advicetype>
			<tmi8:subadvicetype>%(subadvicetype)s</tmi8:subadvicetype>
			<tmi8:advicecontent>%(advicecontent)s</tmi8:advicecontent>\n""" % data

		xml += """			<tmi8:messagetimestamp>%(messagetimestamp)s</tmi8:messagetimestamp>
		</tmi8:STOPMESSAGE>\n""" % data

		return xml

