class Version():
	'''Version represents a semantic version number'''
	version_number = ''
	major = 0
	minor = 0
	patch = 0

	def __init__(self, major, minor, patch):
		self.major = major
		self.minor = minor
		self.patch = patch
		self.version_number = self.__str__()

	def __str__(self):
		return f'{self.major}.{self.minor}.{self.patch}'

	def to_version(self, version_string):
		[major, minor, patch] = version_string.split('.')
		self.major = major
		self.minor = minor
		self.patch = patch
		self.version_number = self.__str__()
