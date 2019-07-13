import re as regexp
from semvercomp.validators import validate_version

class Version():
	"""
		Version represents a semantic version number
	"""

	def __init__(self, major=0, minor=0, patch=0, pre_release="", build="", has_v=False):
		self.has_v = has_v
		self.major = major
		self.minor = minor
		self.patch = patch
		self.pre_release = pre_release
		self.build = build
		self.version_number = self.__str__()

	def __str__(self):
		base = ''

		if self.has_v:
			base = 'v'

		base = f'{base}{self.major}.{self.minor}.{self.patch}'

		if self.pre_release != "":
			base = f'{base}-{self.pre_release}'

		if self.build != "":
			base = f'{base}+{self.build}'

		return base

	def parse_version_number(self, version_string):
		(parts, is_ok) = validate_version(version_string)

		if is_ok:
			self.has_v = parts['has_v']
			self.major = int(parts['major'])
			self.minor = int(parts['minor'])
			self.patch = int(parts['patch'])
			self.pre_release = parts['pre_release']
			self.build = parts['build']
			self.version_number = version_string
		else:
			raise Exception(f'Version string {version_string} is not a valid version tag.')
