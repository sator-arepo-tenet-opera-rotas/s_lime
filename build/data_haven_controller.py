######################################################################
########################### DEPENDENCIES #############################
######################################################################

# for polling the queue
import time

# for file system monitoring:
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# for aws-specific functionality:
import boto3

# for HD and Evo integration
from ftplib import FTP
import os # file renaming, but this will be deprecated soon

# for controlling the HD directly
import sys
import socket


# for future features:
# import logging


######################################################################
ascii_art = '''
 _______/\\\\\\\//////_____
'''

######################################################################

rack_1 = [
"192.168.10.99",
"192.168.10.100",
"192.168.10.101",
"192.168.10.102",
"192.168.10.103",
"192.168.10.104",
"192.168.10.105",
"192.168.10.106",
"192.168.10.107",
"192.168.10.108"
]

rack_2 = [
"192.168.10.137",
"192.168.10.138",
"192.168.10.139",
"192.168.10.140",
"192.168.10.141",
"192.168.10.142",
"192.168.10.143",
"192.168.10.144",
"192.168.10.145",
"192.168.10.146"
]

rack_3 = [
"192.168.10.174",
"192.168.10.175",
"192.168.10.176",
"192.168.10.177",
"192.168.10.178",
"192.168.10.179",
"192.168.10.180",
"192.168.10.181",
"192.168.10.182",
"192.168.10.183"
]

racks = [rack_1, rack_2, rack_3]

######################################################################

def hd_rack_command(rack_num: int = 0, cmd: str = "ping") -> int:
	[hd_command(i, cmd) for i in racks[rack_num]]
	
	return 0

def hd_command(ip: str = "0.0.0.0", command: str = "", ) -> int:
	#status_code = 1
	
	#target_host = "192.168.3.190"
	response = 0
	target_port = 9993
	
	print("Attempting to send command " + command + " to " + ip + "\n")
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	client.settimeout(10)
	
	
	# add try/catch here otherwise the program halts early
	try:
		client.connect((ip, target_port))
		cm = bytes(command+"\n", 'utf-8') # not sure if utf-8 is correct choice to make
		client.send(cm)
		response = client.recv(4096)
		print(response.decode("utf-8"))
		print("\n")
	except socket.error as msg:
		print("Host unresponsive (" + ip + ")")
		pass
		#print("Host unavailable, now exiting program")
	
	'''
	if command == "ping":
		client.send(b"ping\n")
	elif command == "stop":
		...
	elif command == "record":
		...
	elif command == "remote":
		...
	else:
		print("Unavailable Command!!!\n")
	'''
	
	return response

######################################################################

# this operates in an automatic and manual way, manual way is callable from main menu
def purge_rack(rack_num:int = 2, manual:bool = True) -> int:

# if manual:
# get user input, ask for rack then confirm clearing the rack


	# USE THIS:
	#[purge_server(i) for i in racks[rack_num]]
	#purge_count = [purge_server(i) for i in racks[rack_num-1]] # with proper offset

	if rack_num == 1:
		print("Purging Rack " + str(rack_num))
		...
	elif rack_num == 2:
		purge_count = [purge_server(i) for i in racks[1]]
		print("Files purged: ")
		print(purge_count)
	
	elif rack_num == 3:
		...
	else:
		print("Rack not found")
		
	return 0

######################################################################

def purge_server(ip: str, default_dir: str = "1", name: str = "unknown") -> int:

	print("Purging " + ip)
	purge_count = 0 # counter
	
	# this should signal if HD has files or is empty
	# if it has any files,
	# add confirmation Y/n input for use in manual mode

	# add try/except:
	try:
		ftp = FTP(ip)
		ftp.login()
		ftp.cwd(default_dir)
	
		for file_name in ftp.nlst():
			ftp.delete(file_name)
	
		ftp.quit()
	except:
		print("Connection failed")
		pass

	return purge_count


######################################################################
######################################################################

# need to update the file name to reflect nomenclature policy
def pull_server(ip: str, default_dir: str = "1", name: str = "unknown") -> int:

	print("Pulling files from: " + ip)

	try:
		ftp = FTP(ip, timeout=30) # adjust timeout according to feedback
		ftp.login()
		ftp.cwd(default_dir)
	
		for file_name in ftp.nlst():
			rac_prefix = "rack_" + ip + "_"
	
			file = open(file_name, 'wb')
			print(file)
			
			#old_name = file_name
			'''
			new_name = rac_prefix+file_name
			file = ftp.rename(file_name, new_name)
			
			time.sleep(1) # this is causing issues; may need to roll back or just use the on-machine version
			
			ftp.retrbinary('RETR '+ file_name, file.write)# open(new_name, 'wb').write
			'''
			# os.rename(before, after)
			#os.rename(file_name, rac_prefix+file_name)
			
			# file = ftpInstance.rename("ToServer.txt", "NewFile.txt");
			
			ftp.retrbinary('RETR '+ file_name, file.write)
			
			os.rename(file_name, rac_prefix+file_name)
			
			file.close()
	
		ftp.quit()
	except:
		print("Host unresponsive (" + ip + ")\n")
		pass

	return 1


######################################################################
######################################################################

# aka "pull_rack"
def rack_stacker(rack_num:int = 0) -> int:
	if rack_num == 1:
		print("Sending the Rack-Racoon to Rack 1")
		...
	elif rack_num == 2:
		all_files = [pull_server(i) for i in racks[1]] # REMEMBER THE -1 OFFSET
		print(all_files)
	
	elif rack_num == 3:
		...
	else:
		print("throw an error")
	
	return 0


######################################################################
######################################################################

def q_connector(aws_region:str = 'us-west-2', q_name:str = "test" ) -> int:

	rds = boto3.setup_default_session(region_name=aws_region)
	rds = boto3.client('rds')
	sqs = boto3.resource('sqs')
	
	queue = sqs.get_queue_by_name(QueueName = q_name)
	print("Watching queue: " + queue.url + "\n")
	
	for message in queue.receive_messages(MessageAttributeNames=['Reference'],
		MaxNumberOfMessages=5,
		VisibilityTimeout=123,
		WaitTimeSeconds=10,
		ReceiveRequestAttemptId='string'):
		# Print out the body of the message
		#print('Displaying message: {0}'.format(message.body))
		
		# need to log this to a file to record transaction:
		print('Message:, {0}'.format(message.body))
		print(type(message.body))
		#print('Displaying message: {0}'.format(message.MessageAttributes))
		
		
		region_code = message.message_attributes['Reference']['StringValue']
		
		print("Region to stop:")
		print(region_code)
		
		route_to_rack = region_validator(region_code)
		
		if route_to_rack > 0 and route_to_rack < 4:
			print("Routing to rack " + str(route_to_rack) + "...")
			
			
			#async / await situation?
			# replace this with:
			# new rack(rack_num)
			# then call some rack.pull() method
			mux = rack_stacker(route_to_rack)
			
			
			# once sent to rack, message should be popped off of the queue
			# so as to ensure it doesnt invoke the Pull routine more than once
				
			
			# once the mutex lock is released, call purge
			# this makes it so only one rack is being pulled at a time (spawn/fork/new for multiple racks at once)
			
			
			
		else:
			print("Deleting message (bad routing): " + region_code)
			message.delete()
			
	return 0
	
######################################################################
######################################################################
	
def region_validator(r_code: str = "") -> int:
	# receives a region code, returns the rack number or 0 if it's invalid
	print("Checking " + r_code + " ")
	print(type(r_code))

	validity = 0
	if r_code == "AMER":
		return 1
	elif r_code == "EMEA":
		return 2
	elif r_code == "APAC":
		return 3
	else:
		"rejected, invalid status code"
		
	return validity
	
######################################################################
######################################################################

def poll_queue(queueName="default_queue") -> int:
	# return type needs to reflect < reference_code : region_code
	ref_number = 0 # placeholder for now
	
	try:
		while True:
			
			ref_number = q_connector()
			time.sleep(1)
	except:
		print( "Error")
			
	return 0


######################################################################
######################## FILE MONITORING #############################
######################################################################

# this part of the program (might split into a second daemon):
# watches a folder for new files
# uploads those new files to google drive (or another remote server)
# 	(if they have not been uploaded already)
# copies those files to cold storage
# removes the files from the storage area


# NOT implemented:
def watch() -> int:
	print("Now watching the some folder for new files")

	# every X minutes, call the poll_queue() function

	return 0

# NOT implemented:
class Watcher:
	DIRECTORY_TO_WATCH = "watch"

	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
		self.observer.start()
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print( "Error")

		self.observer.join()

######################################################################

# NOT implemented:
class Handler(FileSystemEventHandler):

	@staticmethod
	def on_any_event(event):
		if event.is_directory:
			return None

		elif event.event_type == 'created':
			# Take any action here when a file is first created.
			print ("Received created event - %s." % event.src_path)

		elif event.event_type == 'modified':
			# Taken any action here when a file is modified.
			print ("Received modified event - %s." % event.src_path)

######################################################################
############################# MAIN PROGRAM ###########################
######################################################################

menu_options = {
	1: ' 1: Refresh Screen',
	2: ' 2: Invoke Q-Monitor and pull from racks',
	3: ' 3: Send [STOP] Command to Rack',
	4: ' 4: Purge a Rack [CAUTION]',
	5: ' 5: View Settings',
	6: ' 6: Exit',
}

def print_menu():
	for k in menu_options.keys():
		print (k, '--', menu_options[k] )

clearConsole = lambda: print('\n' * 150)
#clearConsole()

######################################################################

def option0():
	print("SK8 FAST EAT-A55 ERROR")
	
def option1():
	clearConsole()
	print(ascii_art)
	#print('Handle option \'Option 1\'')

def option2():
	clearConsole()
	poll_queue()
	#w = Watcher()
	#w.run()
	
	#print('Handle option \'Option 2\'')

def option3():
	print("CAUTION")
	
	# the rack list starts at zero so user inputs 1 means rack # in program is 0
	hd_rack_command(1, "stop")
	#print('Handle option \'Option 3\'')

def option4():
	purge_rack() # default is rack 2
	#print('Handle option \'Option 3\'')

def option5():
	print("Not implemented...")

######################################################################

if __name__=='__main__':
	clearConsole()
	print(ascii_art)

	while(True):
		print_menu()
		option = ''
		try:
			option = int(input('Enter your choice: '))
		except:
			print('Wrong input. Please enter a number ...')

		if option == 0:
			option0()
		elif option == 1:
			option1()
		elif option == 2:
			option2()
		elif option == 3:
			option3()
		elif option == 4:
			option4()
		elif option == 5:
			option5()
		elif option == 6:
			print('EXITING')
			exit()
		else:
			print('Invalid option. Please enter a number between 1 and 4.')

# end of program
