from setuptools import setup, find_packages

setup(
    name="agent_starter_pack",
    version="0.1",
    packages=find_packages(),
    package_dir={'': 'src'},  # Important! Tells Python where to find packages
)