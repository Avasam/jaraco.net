#!/usr/bin/env python
# Generated by jaraco.develop 2.14
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools

with io.open('README.txt', encoding='utf-8') as readme:
	long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []

windows_scripts = [
	'whois-bridge-service = jaraco.net.whois:Service.handle_command_line',
	'wget = jaraco.net.http:wget',
	] if sys.platform == 'win32' else []

setup_params = dict(
	name='jaraco.net',
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="Networking tools by jaraco",
	long_description=long_description,
	url="https://bitbucket.org/jaraco/jaraco.net",
	packages=setuptools.find_packages(),
	install_requires=[
		'jaraco.util>=5.0',
		'more_itertools',
		'BeautifulSoup4',
		'keyring>=0.6',
		'lxml',
		'requests',
		'feedparser',
		'six>=1.4',
		'backports.method_request',
		'jaraco.timing',
		'jaraco.text',
		'jaraco.collections',
		'jaraco.logging',
	],
	setup_requires=[
		'setuptools_scm',
	] + pytest_runner + sphinx,
	tests_require=[
		'pytest',
		'cherrypy',
		'svg.charts',
	],
	license='MIT',
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points = {
		'console_scripts': [
			'whois-bridge = jaraco.net.whois:serve',
			'scanner = jaraco.net.scanner:scan',
			'fake-http = jaraco.net.http.servers:Simple.start',
			'fake-http-auth = jaraco.net.http.servers:AuthRequest.start',
			'serve-local = jaraco.net.http.static:serve_local',
			'fake-smtp = jaraco.net.smtp:start_simple_server',
			'udp-send = jaraco.net.udp:Sender',
			'udp-echo = jaraco.net.udp:EchoServer',
			'dns-forward-service = jaraco.net.dns:ForwardingService.handle_command_line',
			'dnsbl-check = jaraco.net.dnsbl:Service.handle_command_line',
			'ntp = jaraco.net.ntp:handle_command_line',
			'remove-known-spammers = jaraco.net.email:remove_known_spammers',
			'tcp-test-connect = jaraco.net.tcp:test_connect',
			'tcp-echo-server = jaraco.net.tcp:start_echo_server',
			'http-headers = jaraco.net.http:headers',
			'build-dir-index = jaraco.net.site:make_index_cmd',
			'content-type-reporter = jaraco.net.http.content:ContentTypeReporter.run',
			'web-tail = jaraco.net.tail:handle_command_line',
			'rss-launch = jaraco.net.rss:launch_feed_enclosure',
			'rss-download = jaraco.net.rss:download_enclosures',
		] + windows_scripts,
	},
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
