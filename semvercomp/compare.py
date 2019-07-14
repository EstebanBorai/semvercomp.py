from enum import Enum
from semvercomp.utils import to_version_list
from semvercomp.Version import Version

class Relation(Enum):
	"""
		Enumerates the three kind of relationships between
		Version objects
	"""
	GREATER = 1
	EQUAL = 0
	LOWER = -1

def is_equal(va, vb, with_pre_release=False, with_build=False):
	"""
		Returns True if "va" is equal to "vb".
		This function results are based on Major, Minor and Patch numbers.
	"""
	if with_pre_release and va.pre_release != vb.pre_release:
		return False
	
	if with_build and va.build != vb.build:
		return False

	if va.major != vb.major:
		return False
	
	if va.minor != vb.minor:
		return False
	
	if va.patch != vb.patch:
		return False
	
	return True

def relationship(va, vb):
	"""
		Returns the kind of "Relation" between
		two version objects
	"""
	if is_equal(va, vb):
		return Relation.EQUAL
	
	if va.major != vb.major:
		if va.major > vb.major:
			return Relation.GREATER
		else:
			return Relation.LOWER

	if va.minor != vb.minor:
		if va.minor > vb.minor:
			return Relation.GREATER
		else:
			return Relation.LOWER
	
	if va.patch != vb.patch:
		if va.patch > vb.patch:
			return Relation.GREATER
		else:
			return Relation.LOWER
	

def is_greater(va, vb):
	"""
		Returns True if "va" is greater than
		"vb" otherwise returns False
	"""
	if relationship(va, vb) == Relation.GREATER:
		return True

	return False


def greatest(version_list):
	"""
		Returns the greatest version from an iterable
		of version strings as a version object
	"""
	current = Version(0, 0, 0)
	versions = to_version_list(version_list)

	for v in versions:
		if is_greater(v, current):
			current = v
		else:
			continue
