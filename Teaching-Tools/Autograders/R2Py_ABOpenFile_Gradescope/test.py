'''
Victoria Zhong
'''

import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess32 as subprocess
import glob

class TestRePy(unittest.TestCase):
	def setUp(self):
		pass

	@weight(1)
	def test_1(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase1.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")
		#python repy.py RepyAssignments/restrictions.default RepyAssignments/encasementlib.r2py RepyAssignments/"$1" RepyAssignments/attackcase"$i".r2py 
	@weight(1)
	def test_2(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase2.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_3(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase3.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_4(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase4.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_5(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase5.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_6(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase6.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_7(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase7.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_8(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase8.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_9(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase9.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")

	@weight(1)
	def test_10(self):
		try:
			refmon = glob.glob('reference_monitor_*.r2py')[0]
			proc = subprocess.Popen(["python", "repy.py", "restrictions.default", "encasementlib.r2py", refmon ,"attackcase10.r2py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = proc.stdout.read().strip() #first item
			self.assertEqual(output, "")
			proc.terminate();
		except:
			self.fail("Test Failed")