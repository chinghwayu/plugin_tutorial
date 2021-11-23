try:
    # For python 3.8 and later
    import importlib.metadata as importlib_metadata
except ImportError:
    # For everyone else
    import importlib_metadata

from stevedore import ExtensionManager


def register_plugin(name, namespace, entry_point) -> None:
    """Registers a plugin dynamically without needing to install as a package.

    Args:
        name (str): Name of plugin to be referenced.
        namespace (str): Name of plugin namespace.
        entry_point (str): Entry point in the form: some.module:some.attr

    """
    ep = importlib_metadata.EntryPoint(name, entry_point, namespace)
    e = ExtensionManager(namespace)
    if namespace in e.ENTRY_POINT_CACHE:
        entry_points = e.ENTRY_POINT_CACHE.get(namespace)
        if name not in [entry_point.name for entry_point in entry_points]:
            entry_points.append(ep)
            e.ENTRY_POINT_CACHE[namespace] = entry_points
    else:
        e.ENTRY_POINT_CACHE[namespace] = [ep]
    ep.load()
