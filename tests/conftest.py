"""Tests suite for `volttron-interoperability`."""
import sys

from volttrontesting.fixtures.volttron_platform_fixtures import *


p = Path(__file__)
if p.parent.parent.parent.resolve().as_posix() not in sys.path:
    sys.path.insert(0, p.parent.parent.resolve().as_posix())

