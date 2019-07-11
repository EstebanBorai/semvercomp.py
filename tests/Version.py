import unittest

from semvercomp.Version import Version

class TestVersion(unittest.TestCase):
	def test_Version_constructor_major(self):
		"""
			Test constructor major argument
		"""
		major = 22

		ver = Version(22, 0, 0)

		self.assertEqual(major, ver.major)	

	def test_Version_constructor_minor(self):
		"""
			Test constructor minor argument
		"""
		minor = 1

		ver = Version(0, 1, 0)

		self.assertEqual(minor, ver.minor)

	def test_Version_constructor_patch(self):
		"""
			Test constructor patch argument
		"""
		patch = 2

		ver = Version(0, 0, 2)

		self.assertEqual(patch, ver.patch)

	def test_Version__str__(self):
		"""
			Test an instance of Version parsed to string
		"""
		version_number = '1.4.11'

		ver = Version(1, 4, 11)
		ver_str = str(ver)

		self.assertEqual(ver_str, version_number)

	def test_Version_parse_version_number(self):
		"""
			Test parse_version_number method from Version class
		"""

		major = 12
		minor = 9
		patch = 1

		ver = Version()
		ver.parse_version_number("12.9.1")
		
		self.assertEqual(str(ver), str(Version(major, minor, patch)))
