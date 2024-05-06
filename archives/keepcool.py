#!/usr/bin/env python
# -*- coding: iso-8859-1  -*-
#
# Author: Philippe Fremy <phil@freehackers.org>
# Copyright Philippe Fremy 2002-2004
# License: consider this code as public domain
# Version: 1.1
#
# ChangesLog:
# 1.1, 11/08/2004
# - generate an error if the output of lmsensors or ps is not understood


# You need lm sensors to run the script: http://www2.lm-sensors.nu/~lm78/

import re, os, sys, time, signal
from pprint import pprint

# HIGH_TEMP: stop some process if any cpu temp is above this temperature
# LOW_TEMP: restart some process if all cpu temp. are under this temperature
HIGH_TEMP = 53
LOW_TEMP  = 50

# stop all the processes that take more than HIGH_CPU
HIGH_CPU = 20

# delay for interval check in seconds
DELAY = 5

debug=0

ps_cmd="ps -waeo %cpu,pid,ppid,user,args --sort %cpu"
ps_output_regexp = re.compile( r"^\s*(\d+\.\d+)\s+(\d*)\s+(\d*)\s+(\w*)\s+(.*)\s*$" )
def parse_ps_output( ps_output ):
	"""Parse ps output to extract a lists of the following tuples:
	(cpu_usage, pid, ppid, cmd ).

	The list is sorted by cpu, with the highest cpu usage first
	"""
	result = []
	for line in ps_output.split('\n'):
		mo = ps_output_regexp.match( line )
		if mo:
			result.insert( 0, 
							[float(mo.group(1)), # cpu
							int(mo.group(2)), 	 # pid
							int(mo.group(3)), 	 # ppid
							mo.group(5)[:50] ] )		 # cmd

	if not len(result):
		raise Exception("The output of the command ps could not be parsed. Please send a mail to the author to report the problem.\nps output:\n %s" % ps_output)
	result.sort()
	result.reverse()
	return result

CPU=0
PID=1
PPID=2
CMD=3
stopped_processes = []

def print_temp( msg, temp, print_time=0 ):
	if print_time:
		t = time.localtime()
		print "%02d:%02d:%02d" % (t[3], t[4], t[5] ),
	print msg,
	for t in temp:
		print "%2.1f" % t,
	print

sensors_cmd="sensors"
sensors_output_re= re.compile( r"^CPU(\d)\s+Temp:\s+\+(\d+.\d+).C\s+.*$" )
def parse_sensors_output( sensors_output ):
	"""Return the list of the temperatures of the different cpu"""
	result = []
	for line in sensors_output.split('\n'):
		mo = sensors_output_re.match( line )
		if mo:
			result.append( (int(mo.group(1)), float(mo.group(2))  ) )
	result.sort()
	result = map( lambda el: el[1], result )
	if not len(result):
		raise Exception("The output of sensors could not be parsed. Please report the problem to the author.\nSensor output:\n%s" % sensors_output )
	return result


def stop_process( process, all_processes ):
	pid_dict = {}
	for el in all_processes:
		pid_dict[ el[PID] ] = el

	while 1:
		try:
			os.kill( process[PID], signal.SIGSTOP )
			stopped_processes.insert( 0, process )
			print "process stopped: ", process[PID], process[CMD]
			return 1
		except OSError, msg:
			print "Could not stop process %d (%s): %s" % (process[PID], process[CMD], msg)
			if pid_dict.has_key( process[PPID] ):
				print "Trying its parent"
				process = pid_dict[ process[PPID] ]
				continue
			else:
				print "Could not find parent, giving up"
				return 0

def manage_high_temp():
	"""Stop some processes to lower the temperature of the cpu"""
	while 1:
		need_other_pass = 0
		ps_output = os.popen( ps_cmd ).read()
		all_processes = parse_ps_output( ps_output )
		high_cpu_processes = filter( lambda el: el[0] >= HIGH_CPU, 
			all_processes )

		if len(high_cpu_processes):
			if debug: print "Processes taking high cpu:"
			for el in high_cpu_processes:
				if debug: print "%d: %s" % (el[PID], el[CMD])
				if not stop_process( el, all_processes ):
					need_other_pass = 1
			if not need_other_pass:
				print "%d process currently stopped" % len(stopped_processes)
				return
		else:
			if debug: print "No process taking high cpu, don't know what to stop."

 
def manage_low_temp():
	"""Restart stopped processess"""
	cpu, pid, ppid, name  = stopped_processes.pop()
	print "Restarting ", pid, name
	try:
		os.kill( pid, signal.SIGCONT )
	except OSError, msg:
		print "Could not restart it :", msg

def main():
	while(1):
		sensor_output = os.popen( sensors_cmd ).read()
		cpu_temp = parse_sensors_output( sensor_output )
		if debug: print_temp( "Current temperature: ", cpu_temp, 1 )
		high_temp_cpu = filter( lambda t: t>=HIGH_TEMP, cpu_temp )
		low_temp_cpu = filter( lambda t: t<LOW_TEMP, cpu_temp )
		if debug==2: print_temp( "High temperatures: ", high_temp_cpu )
		if debug==2: print_temp( "Low temperatures:  ", low_temp_cpu )

		if len( high_temp_cpu ):
			print_temp( "CPU are above max temperature : ", high_temp_cpu, 1 )
			manage_high_temp()
		elif len( low_temp_cpu ) == len( cpu_temp ) and len(stopped_processes) != 0:
				print_temp( "Temperature is down again : ", low_temp_cpu, 1 )
				manage_low_temp()

		time.sleep( DELAY )


#### =================================== Tests ==============================

import unittest

ps_output_sample= """
 0.6 10118  2277 philippe gkrellm2
 1.6  1890  1888 root     /etc/X11/X
 3.0 23684 23683 portage  top
 0.9  2341  2119 philippe kdeinit: konqueror --silent
"""


sensors_output_sample="""
via686a-isa-6000
Adapter: ISA adapter
Algorithm: ISA algorithm
CPU0 core: +1.73 V  (min =  +0.00 V, max =  +3.03 V)
CPU1 core: +1.70 V  (min =  +2.24 V, max =  +2.74 V)   ALARM
I/O:       +3.28 V  (min =  +2.95 V, max =  +3.62 V)
+5V:       +4.97 V  (min =  +4.47 V, max =  +5.49 V)
+12V:     +11.92 V  (min = +10.79 V, max = +13.18 V)
CPU0 Fan:    0 RPM  (min = 3000 RPM, div = 2)          ALARM
CPU1 Fan:    0 RPM  (min = 3000 RPM, div = 2)          ALARM
CPU0 Temp: +39.5°C  (limit =  +60°C, hysteresis =  +50°C)
CPU1 Temp: +37.5°C  (limit =  +60°C, hysteresis =  +50°C)
"""

class TestKeepcool( unittest.TestCase ):
	def testParsePsOutput( self ):
		result = parse_ps_output( ps_output_sample )
		item = result[0]
		self.assertEquals( item[0], 3.0 )
		self.assertEquals( item[1], 23684 )
		self.assertEquals( item[2], 23683)
		self.assertEquals( item[3], "top" )
		item = result[1]
		self.assertEquals( item[0], 1.6 )
		self.assertEquals( item[1], 1890)
		self.assertEquals( item[2], 1888)
		self.assertEquals( item[3], "/etc/X11/X" )

	def testSensorsOutput( self ):
		result = parse_sensors_output( sensors_output_sample )
		self.assertEquals( result, [ 39.5, 37.5 ] )

if __name__ == "__main__":
	if len(sys.argv) > 1:
		sys.argv = sys.argv[:1]
		# unittest.main( unittest.TextTestRunner( verbosity=1 ) )
		unittest.main()
	else:
		main()




