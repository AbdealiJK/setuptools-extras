import sys

from setuptools_extras.misc.utilities import popen


class Package:
    """
    A template to hold information relating to a package.
    """

    def __init__(self):
        name = None
        version = None


class PackageManager:
    """
    An abstract class used to unify the interface of various package managers.
    This is used as an abstraction layer to interact with a package manager
    so that it can be used by python packages for easier dependency handling.
    """

    def __init__(self, name):
        self._name = name

    def package_to_cli(self, package):
        """
        Convert the package into a string that can be used to identify it in
        the CLI.
        """
        raise NotImplementedError

    def install_command(self, packages):
        """
        Create the installation command that can be run to install packages.
        """
        raise NotImplementedError

    def check_install_command(self, package):
        """
        Create the command to check if a package is installed or not.
        """
        raise NotImplementedError

    def install(self, packages):
        """
        Install the given packages using the package manager.
        """
        with popen(self.install_command(packages),
                   stdout=sys.stdout,
                   stderr=sys.stderr) as process:
            process.wait()
            return process.exitcode

    def check_install(self, package):
        """
        Check if a package is installed or not using the package manager.
        """
        raise NotImplementedError
