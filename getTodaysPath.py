import datetime, time, os, sys, subprocess
from lxml import etree
from xml.dom.minidom import parseString
from threading import Thread


#set parameters
def set_global():
	global YYYY, MM, DD, path, dirs, linktokml
	YYYY = time.strftime("%Y")
	MM = time.strftime("%m")
	DD = time.strftime("%d")
	path = os.getcwd()
	dirs = os.listdir(path)

	linktokml = """https://www.google.com/maps/timeline/kml?authuser=0&pb=!1m8!1m3!1i"""
	linktokml += YYYY
	linktokml += """!2i"""
	linktokml += MM
	linktokml += """!3i"""
	linktokml += DD
	linktokml += """!2m3!1i"""
	linktokml += MM
	linktokml += """!3i"""
	linktokml += DD


#checks if former KML file and deletes it
def sup_previous_kml():
	for localFile in dirs:
		if localFile.lower().endswith(('.kml')):
			os.remove(localFile)
	time.sleep(3)
	global kml_presence
	kml_presence = False
	print('PREVIOUS KML ERASED SUCCESFULLY')


#DL new KML and makes sure it went right
def do_dl():
	global kml_presence, linktokml, proc
	FNULL = open(os.devnull, 'w')
	proc = subprocess.Popen(["surf", linktokml], stderr=FNULL)
	while not kml_presence:
		pass
	FNULL.close()
	time.sleep(1)
	proc.kill()



def do_mon():
	global kml_presence, path, dirs, kml_location
	while not kml_presence:
		time.sleep(1)
		dirs = os.listdir(path)
		for localFile in dirs:
			if localFile.lower().endswith(('.kml')):
				kml_presence = True
				kml_location = path+"/"+localFile
				time.sleep(1)


def dl_new_kml():
	download_thread = Thread(target=do_dl, name="DOWNLOAD_KML")
	monitor_thread = Thread(target=do_mon, name="CHECK_IF_KML")

	download_thread.start()
	monitor_thread.start()	

	iteration = 0
	while not kml_presence:
		iteration += 1
		time.sleep(0.1)
		#remove hashtag to monitorthe download variables
		#print("download: ",download_thread.is_alive(), "	monitor: ",monitor_thread.is_alive(), "	iter: ", iteration, "kml_presence: ", kml_presence, end="\r"	)
	print("NEW KML DOWNLOADED SUCCESFULLY")
	time.sleep(3)


#Extracts information from download KML file
def read_kml():
#http://chrisagocs.blogspot.fr/2013/01/how-to-parse-kml-file-and-find-centroid.html
	global kml_location, points
	localFile = open(kml_location,'r')
	data = localFile.read()
	localFile.close()

	dom = parseString(data)

	#latitudes = []
	#longitudes = []
	points = []

	for d in dom.getElementsByTagName('gx:coord'):
		coords = d.firstChild.data.split(' ')
		#longitudes.append(float(coords[0]))
		#latitudes.append(float(coords[1]))
		points.append(coords)
	print('INFORMATION READ SUCCESFULLY')


#Save extracted information into .coords file
def save_coords():
	global path, points
	directory = path+"/history/"
	if not os.path.exists(directory):
		os.makedirs(directory)

	filename = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d.%m.%Y")+".coords"
	localFile = open(directory+filename,"w")
	localFile.write("### Fait le "+time.strftime('%c')+" ###\n")
	for point in points:
		for coord in point:
			localFile.write(coord+" ")
		localFile.write("\n")
	localFile.closed
	print('COORDS SAVED SUCCESFULLY')




set_global()
sup_previous_kml()
dl_new_kml()
read_kml()
save_coords()







	




























































