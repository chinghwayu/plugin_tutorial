from abc import ABCMeta, abstractmethod
from stevedore import driver
from plugin_tutorial.plugin import register_plugin


class RelayBase(metaclass=ABCMeta):
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


class Relay:
    def __init__(self, name="relay1", **kwargs) -> None:
        namespace = "myrelay"
        if name == "relay1":
            kwargs = {}
            register_plugin(
                name=name,
                namespace=namespace,
                entry_point="plugin_tutorial.relay:RelayOne",
            )
        elif name == "relay2":
            kwargs = {}
            register_plugin(
                name=name,
                namespace=namespace,
                entry_point="plugin_tutorial.relay:RelayTwo",
            )
        self._relay_mgr = driver.DriverManager(
            namespace=namespace,
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


class RelayOne(RelayBase):
    def __init__(self):
        super().__init__()

    def disconnect(self):
        self.disconnected = True
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
        self.disconnected = True
        print("Disconnected Two")

    def connect(self):
        self.connected = True
        print("Connected Two")

    def reconnect(self, seconds: int = 5):
        self.seconds = seconds
        self.disconnect()
        print(f"Two paused for {seconds} seconds...")
        self.connect()
