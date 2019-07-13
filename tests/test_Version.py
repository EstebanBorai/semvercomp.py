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

def test_Version_init_pre_release():
	pre_release = 'beta'

	ver = Version(None, None, None, pre_release)
	assert ver.pre_release == pre_release

def test_Version_init_build():
	build = '123322'

	ver = Version(None, None, None, None, build)
	assert ver.build == build

def test_Version_init_has_v():
	has_v = True

	ver = Version(None, None, None, None, None, True)
	assert ver.has_v == has_v

def test_Version__str__():
	v_string = "v1.21.11-beta+123123"

	ver = Version(1, 21, 11, 'beta', '123123', True)
	assert v_string == str(ver)

def test_Version_parse_version_number():
	v_string = "19.22.133"

	ver = Version()
	ver.parse_version_number(v_string)

	assert ver.major == 19
	assert ver.minor == 22
	assert ver.patch == 133

def test_Version_raise_invalid_tag_exception():
	v_string = "v01.22.43-beta"
	ver = Version()

	with pytest.raises(Exception) as exc:
		assert ver.parse_version_number(v_string)

	assert str(exc.value) == f'Version string {v_string} is not a valid version tag.'	
