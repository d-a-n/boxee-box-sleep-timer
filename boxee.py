#!/usr/bin/env python

import os
import sys
import fnmatch
import glob

import socket, hashlib, random, re, time, urllib2
import xml.dom.minidom as dom

def is_numeric(s):
	try:
		i = float(s)
	except ValueError, TypeError:
		return False
	else:
		return True
	

class BoxeeClient:

	def __init__(self):
		self.port = 2562
		self.application = "iphone_remote" #Must have the value iphone_remote. This will change in the future.
		self.shared_key = "b0xeeRem0tE!" #The shared key string to use must be b0xeeRem0tE!. This will change in the future.
		self.timeout = 2 #seconds
		self.devices = []
		self.api = {
			'commands': {
				'up': 'SendKey(270)',
				'down': 'SendKey(271)',
				'left': 'SendKey(272)',
				'right': 'SendKey(2703)',
				'select': 'SendKey(256)',
				'back': 'SendKey(275)',
				'pause': 'Pause()',
				'get_percentage':'GetPercentage'
			},
			'url': 'http://%s:%s/xbmcCmds/xbmcHttp?command=%s'
		}				
		
	def generateAPIUrls(self, device):
		
		base_url = self.api['url'] % (device['ip'], device['port'], "%s")
		api_urls = {}

		for key in self.api['commands']:
			api_urls[key] = base_url % self.api['commands'][key]
			
		return api_urls

	def putDeviceToSleep(self, id):
		print "put boxee %d to sleep" % id
		
		device = self.devices[id]
		api = self.generateAPIUrls(device)

		f = urllib2.urlopen(api['get_percentage'])
		response = re.sub(r'<[^>]*?>', '', f.read())
		
		cmds = []

		if is_numeric(response):

			cmds = [
				'pause',
				'back',
				'select',
				'back','back','back','back','back','back','back','back',
				'up','left','up','left','up','left',
				'select','select',
				'back','back','back','back','back','back','back',
				'up','left','up','left','up','left',
				'select','select',
				'back','back','back','back','back','back','back','back',
				'up','left','up','left','up','left',
				'select','select',
			]		

		for cmd in cmds:
			urllib2.urlopen(api[cmd])
			time.sleep(0.5)
		print "boxee should sleep now..."

	def discover(self):
		
		challenge = str(random.randint(1000, 9999))
		signature = self.getSignature(challenge)
		
		message = '<?xml version="1.0"?\><BDP1 cmd="discover" application="iphone_remote" version="1.0" challenge="%s" signature="%s"/>' % (challenge, signature)

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
		s.settimeout(self.timeout)
		s.sendto(message, ("<broadcast>", self.port))
		
		devices = []
		
		try:			
			while True:		
				data, address = s.recvfrom(1024)
				resounse = self.handleResponse(address, data)
				if resounse:
					devices.append(resounse)
				
		except socket.timeout:
			print "timeout"
		finally:
			s.close()

		self.devices = devices
		return devices

	def getSignature(self, challenge):
		h = hashlib.md5()
		h.update(challenge)
		h.update(self.shared_key)
		return h.hexdigest()

	'''
	Process response XML data
	<BDP1 cmd="found" application="boxee" version="1.2.0"
			name="boxeebox" httpPort="8800" httpAuthRequired="false"
			response="3531B473B97E4F61D8BCED056270A05C"
			signature="6369D3180DF19108E35708466CB1270E"/>
	'''
	def handleResponse(self, address, data):

		try:
			d = dom.parseString(data)
			el = d.getElementsByTagName('BDP1')[0]
			response = {
				'name':el.getAttribute('name'),
				'port':el.getAttribute('httpPort'),
				'ip': address[0],
				'application': el.getAttribute('boxee'),
				'version': el.getAttribute('version')
			}
			return response
		except:
			print "data is not valid"
			
		return False


#boxee = BoxeeClient()

#def test():
#	window.alert('demo');

#def pGetDevices():

#	devices = boxee.discover()
#	return devices

#getDevices()
