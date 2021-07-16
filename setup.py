from setuptools import find_packages
from setuptools import setup

setup(
    name="plugin-tutorial",
    packages=find_packages(),
    version="1.0.0",
    description="Plugin Tutorial",
    author="Ching-Hwa Yu",
    license='BSD',
    author_email="chinghwayu@gmail.com",
    url="https://github.com/chinghwayu/plugin_tutorial",
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Environment :: Console",
    ],
    entry_points={
        "plugin_tutorial": [
            "relay1 = relay:RelayOne",
            "relay2 = relay:RelayTwo",
        ],
    },
)
