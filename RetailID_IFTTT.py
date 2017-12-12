# -*- coding:utf-8 -*-
import os, sys, datetime, json, time

def down(rtl):
	global upb; spr = "/R" + rtl + ".png"; sx = sbn + rtl + ".png"
	if os.path.isfile(sx): oldsize = os.path.getsize(sx)
	else: oldsize = 0
	os.system("wget -t 0 -T 5 -q -N -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr)
	if os.path.isfile(sx): newsize = os.path.getsize(sx)
	else: newsize = 0
	if newsize != oldsize and newsize > 1:
		try: rname = storejson[0][rtl]
		except KeyError: rname = "一家未存档名称的零售店"
		reload(sys); sys.setdefaultencoding('utf-8')
		pushRaw = "[零售店图片]Apple " + rname + " 刚刚更新，店号 R" + rtl + "，图片大小 " + str(newsize / 1024) + " KB。"
		upb = upb + pushRaw + "\n"; print pushRaw
		if os.path.isfile(sx): os.system("mv -n " + sbn + rtl + ".png " + rpath + "Other/previous/")
		os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1=" + pushRaw 
				+ "' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x")
		os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1=" + pushRaw 
				+ "' https://maker.ifttt.com/trigger/raw/with/key/bOGI8iEAyvjh782UYFKbRa")
		print
		# GitHub users please notice: IFTTT key only uses for private.
	else: 
		try: pname = "R" + rtl + ": " + storejson[0][rtl]
		except KeyError: pname = "R" + rtl
		if newsize == 0: print pid + " Checked " + pname + " does not exist, ignore."
		else: print pid + " Checked R" + rtl + " has no update, ignore."

arg = 0; pid = str(os.getpid())
for m in sys.argv[1:]: arg += 1
if arg == 0: start = 1
else: start = int(sys.argv[1])
rpath = "/home/pi/Retail/"; sbn = rpath + "Pictures/R"; argv = list(range(10))
dieter = "https://rtlimages.apple.com/cmc/dieter/store"; arg = arm = 0;
sTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

while True:
	global upb; upb = ""; nameopen = open("/home/pi/Retail/name.md"); storejson = json.loads(nameopen.read()); nameopen.close()
	for j in range(start, 730): down("%03d" % j)
	if upb == "": upb = "No stores were updated in this check."
	print "\nStarted: " + sTime + "\nEnded:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	print "\n" + upb + "\nPID " + pid + " is sleeping, interval will be 12hr."; time.sleep(43200)