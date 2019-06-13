
allComputers = {'MacBook Pro': {'google drive':2,'photos':100},
'Surface Pro':{'google drive':1,'videos':40},
'ipad':{'google drive':3, 'photos':15},
'iphone':{'google drive':1, 'videos':3}
}

def totalThings(devices, things):
	numThing = 0
	for k, v in devices.items():
		numThing = numThing + v.get(things, 0)
	return numThing

print('Number of things on my devices')
print(' - google drive ' + str(totalThings(allComputers, 'google drive')))
print(' - photos ' + str(totalThings(allComputers, 'photos')))
print(' - videos ' + str(totalThings(allComputers, 'videos')))




allFamily = {'Dad':{'iPhone':1, 'iPad':3, 'macbook pro':1}, 'Mum':{'iPhone':1, 'iPad':1, 'MacBook':1}, 'Andrew':{'iPhone':1, 'iPad':1,'MacBook pro':1},
'William':{'iPhone':1, 'iPad':1}, 'Harry':{'iPhone':1, 'macbook pro':1}, 'Louise':{'iPhone':1, 'iPad':1, 'macbook pro':1}}

def totalDevices (names, devices):
	numDevices = 0
	for k, v in names.items():
		numDevices = numDevices + v.get(devices, 0)
	return numDevices

print('Number of devices owned by the family')
print(' - iPhone ' + str(totalDevices(allFamily, 'iPhone')))
print(' - iPad ' + str(totalDevices(allFamily, 'iPad')))
print(' - macbook pro ' + str(totalDevices(allFamily, 'macbook pro')))
print(' - Macbook ' + str(totalDevices(allFamily, 'MacBook')))