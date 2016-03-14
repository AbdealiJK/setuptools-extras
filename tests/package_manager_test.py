import os
import tempfile
import sys
import unittest
from unittest import mock

from setuptools_extras.package_manager import PackageManager


class DummyManager(PackageManager):

    def package_to_cli(self, package):
        return str(package)

    def install_command(self, packages):
        return ["echo"]+ list(map(self.package_to_cli, packages))


class PackageManagerTest(unittest.TestCase):

    def setUp(self):
        self.uut = DummyManager(name="echo")

    def test_install_command(self):
        command = self.uut.install_command(['pkg1', 'pkg2'])
        self.assertEqual(command, ["echo", "pkg1", "pkg2"])

    @mock.patch('setuptools_extras.package_manager.popen')
    def test_install(self, mock_popen):
        process_mock = mock.MagicMock(exitcode=0)
        contextmanager_mock = mock.MagicMock(
            __enter__ = mock.Mock(return_value=process_mock),
            __exit__ = mock.Mock())
        mock_popen.return_value = contextmanager_mock

        exitcode = self.uut.install(['pkg1', 'pkg2'])

        self.assertEqual(mock_popen.call_count, 1)
        self.assertEqual(exitcode, 0)
        self.assertIn((['echo', 'pkg1', 'pkg2'],), mock_popen.call_args,
                      "popen() was called with unexpected args.")
