class Version():
	'''Version represents a semantic version number'''

	def __init__(self, major=0, minor=0, patch=0):
		self.major = major
		self.minor = minor
		self.patch = patch
		self.version_number = self.__str__()

	def __str__(self):
		return f'{self.major}.{self.minor}.{self.patch}'

	def parse_version_number(self, version_string):
		[major, minor, patch] = version_string.split('.')
		self.major = major
		self.minor = minor
		self.patch = patch
		self.version_number = self.__str__()
