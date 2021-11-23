from abc import ABCMeta, abstractmethod
from stevedore import driver


class RelayBase(metaclass=ABCMeta):
    """Base class for relay plugins"""

    def __init__(self) -> None:
        """Define base attributes."""
        self.connected = False

    @abstractmethod
    def disconnect(self) -> None:
        """Disconnects relay."""

    @abstractmethod
    def connect(self) -> None:
        """Connects relay."""

    @abstractmethod
    def reconnect(self, seconds: int) -> None:
        """Disconnects for specified time and reconnects.

        Args:
            seconds (int): Amount of time to sleep between disconnect and connect.
        """


class RelayOne(RelayBase):
    def __init__(self):
        super().__init__()

    def disconnect(self):
        self.connected = False
        print("Disconnected One")

    def connect(self):
        self.connected = True
        print("Connected One")

    def reconnect(self, seconds: int = 5):
        self.seconds = seconds
        self.disconnect()
        print(f"One paused for {seconds} seconds...")
        self.connect()


class RelayTwo(RelayBase):
    def __init__(self):
        super().__init__()

    def disconnect(self):
        self.connected = False
        print("Disconnected Two")

    def connect(self):
        self.connected = True
        print("Connected Two")

    def reconnect(self, seconds: int = 5):
        self.seconds = seconds
        self.disconnect()
        print(f"Two paused for {seconds} seconds...")
        self.connect()


class Relay:
    def __init__(self, name="", **kwargs) -> None:
        self._relay_mgr = driver.DriverManager(
            namespace="plugin_tutorial",
            name=name,
            invoke_on_load=True,
            invoke_kwds=kwargs,
        )

    @property
    def driver(self):
        return self._relay_mgr.driver

    def disconnect(self) -> None:
        self.driver.disconnect()

    def connect(self) -> None:
        self.driver.connect()

    def reconnect(self, seconds: int = 5) -> None:
        self.driver.reconnect(seconds)
