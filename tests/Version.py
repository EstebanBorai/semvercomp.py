import unittest

from semvercomp.Version import Version

class TestVersion(unittest.TestCase):
	def test_Version_instance(self):
		"""
			Test an instance of Version
		"""
		major = 1
		minor = 4
		patch = 11
		version_number = '1.4.11'

		ver = Version(major, minor, patch)

		self.assertEqual(major, ver.major)
		self.assertEqual(minor, ver.minor)
		self.assertEqual(patch, ver.patch)
		self.assertEqual(ver.version_number, version_number)
