import sys
import importlib
import socket
import functools
import time

import pytest
import jaraco.functools
from jaraco.context import ExceptionTrap


missing = ExceptionTrap(ImportError).raises


@missing
def pywin32_missing():
    importlib.import_module('win32service')


collect_ignore = (
    [
        'jaraco/net/devices/linux.py',
        'jaraco/net/devices/win32.py',
        'jaraco/net/devices/darwin.py',
    ]
    + [
        # modules only import on Windows
        'jaraco/net/dns.py',
        'jaraco/net/whois_svc.py',
    ]
    * pywin32_missing()
    + [
        # fabric fails on Python 3.11
        'fabfile.py',
    ]
    * (sys.version_info > (3, 11))
)


@pytest.fixture(autouse=True)
def retry_ntp_query(request, monkeypatch):
    """
    ntp.query is flaky (by design), so be resilient during tests.
    """
    if not request.node.name.endswith('net.ntp.query'):
        return

    from jaraco.net import ntp

    retry = jaraco.functools.retry(
        retries=4,
        trap=socket.timeout,
        cleanup=functools.partial(time.sleep, 4),
    )
    monkeypatch.setattr(ntp, 'query', retry(ntp.query))
