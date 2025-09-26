from os import path, remove, mkdir
import pytest
from guachi import ConfigMapper


@pytest.fixture(autouse=True)
def cleanup_guachi():
	try:
		if path.exists('/tmp/guachi'):
			remove('/tmp/guachi')
		else:
			mkdir('/tmp/guachi')
	except Exception:
		pass
	yield
	try:
		if path.exists('/tmp/guachi'):
			remove('/tmp/guachi')
		else:
			mkdir('/tmp/guachi')
	except Exception:
		pass


def test_access_mapped_configs_empty_dict():
	mapped_options = {
		'guachi.db.host': 'db_host',
		'guachi.db.port': 'db_port',
		'guachi.web.host': 'web_host',
		'guachi.web.port': 'web_port',
		}
	mapped_defaults = {
		'db_host': 'localhost',
		'db_port': 27017,
		'web_host': 'localhost',
		'web_port': '8080',
		}
	foo = ConfigMapper('/tmp/guachi')
	foo.set_ini_options(mapped_options)
	foo.set_default_options(mapped_defaults)
	foo.set_config({})

	# try as much operations as we can and assert them
	assert foo() == {}
	assert foo.path == '/tmp/guachi/guachi.db'
	assert foo.get_ini_options() == {}
	assert foo.get_default_options() == {}
	assert foo.get_dict_config() == mapped_defaults
	assert foo.stored_config() == mapped_defaults
	assert foo.integrity_check()


def test_access_mapped_configs_dict():
	mapped_options = {
		'guachi.db.host': 'db_host',
		'guachi.db.port': 'db_port',
		'guachi.web.host': 'web_host',
		'guachi.web.port': 'web_port',
		}
	mapped_defaults = {
		'db_host': 'localhost',
		'db_port': 27017,
		'web_host': 'localhost',
		'web_port': '8080',
		}
	foo = ConfigMapper('/tmp/guachi')
	foo.set_ini_options(mapped_options)
	foo.set_default_options(mapped_defaults)
	config_dict = {
		'db_host': 'remotehost',
		'db_port': 12345,
		'web_host': 'remoteweb',
		'web_port': '9090',
		}
	foo.set_config(config_dict)
	assert foo.get_dict_config() == config_dict
	assert foo.stored_config() == config_dict
	assert foo.integrity_check()