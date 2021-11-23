import pytest
from relay import Relay


def test_relay_interface():
    r1 = Relay()
    assert isinstance(r1, Relay)
    assert r1.driver.connected == False
    r1.disconnect()
    assert r1.driver.connected == False
    r1.connect()
    assert r1.driver.connected == True
    r1.reconnect(7)
    assert r1.driver.seconds == 7

    r2 = Relay(name="relay2")
    assert isinstance(r2, Relay)
    assert r2.driver.connected == False
    r2.disconnect()
    assert r2.driver.connected == False
    r2.connect()
    assert r2.driver.connected == True
    r2.reconnect(9)
    assert r2.driver.seconds == 9
