import pytest

from semvercomp.Version import Version

def test_Version_init_major():
	major = 11

	ver = Version(major)
	assert ver.major == major

def test_Version_init_minor():
	minor = 33

	ver = Version(None, minor)
	assert ver.minor == minor

def test_Version_init_patch():
	patch = 22

	ver = Version(None, None, patch)
	assert ver.patch == patch

def test_Version__str__():
	v_string = "1.21.11"

	ver = Version(1, 21, 11)
	assert v_string == str(ver)

def test_Version_parse_version_number():
	v_string = "19.22.133"

	ver = Version()
	ver.parse_version_number(v_string)

	assert ver.major == 19
	assert ver.minor == 22
	assert ver.patch == 133
