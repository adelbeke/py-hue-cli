from setuptools import setup

setup(
    name="py-hue",
    version="1.0.0",
    py_modules=["hue", "bridge", "lights"],
    install_requires=[
        "requests",
        "inquirer",
    ],
    entry_points={
        "console_scripts": [
            "py-hue=hue:main",
        ],
    },
)
