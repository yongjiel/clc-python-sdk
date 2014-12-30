"""
Group related functions.  

These group related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21013480-Groups
"""

# TODO - Get Group
# TODO - Get Group Billing Details
# TODO - Get Group Monitoring Statistics

# TODO - GetLocation ignoring: computelimits, networklimits, horizontalAutoscalePolicyMapping, scheduledActivities

import clc

class Group(object):

	@staticmethod
	def GetAll(root_group_id,alias=None):  
		"""Gets a list of groups within a given account.


		"""

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		r = clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,self.id),{})


	@staticmethod
	def Create(name,alias=None,location=None):  
		"""Creates a new group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def __init__(self,id,alias=None,name=None,location=None):
		"""Create Group object.

		If parameters are populated then create object location.  
		Else if only id is supplied issue a Get Policy call

		https://t3n.zendesk.com/entries/44658344-Get-Anti-Affinity-Policy

		>>> clc.v2.AntiAffinity(id="f5b5e523ed8e4604842ec417d5502510")
		<clc.APIv2.anti_affinity.AntiAffinity object at 0x104753690>

		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()
		if location:  self.location = location
		else:  self.location = clc.v2.Account.GetLocation()

		if name:
			self.name = name
			self.location = location
			#self.servers = servers
		else:
			pass
			#r = clc.v2.API.Call('GET','antiAffinityPolicies/%s/%s' % (self.alias,self.id),{})
			#self.name = r['name']
			#self.location = r['location']
			#self.servers = [obj['id'] for obj in r['links'] if obj['rel'] == "server"]


	def Update(self):
		"""Update group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def Delete(self):
		"""Delete group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def __str__(self):
		pass

