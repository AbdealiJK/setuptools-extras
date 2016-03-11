import os
import sys
import unittest

from setuptools_extras.misc.utilities import popen, popen_call, make_temp


class RunPOpenTest(unittest.TestCase):

    @staticmethod
    def get_test_command(scriptname):
        return [sys.executable,
                os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "run_popen_testfiles",
                             scriptname)]

    def test_create_with_stdin(self):
        command = self.get_test_command("test_interactive_program.py")

        with popen(command) as p:
            p.stdin.write("33\n")
            p.stdin.flush()
            p.wait()
            self.assertEqual(p.stdout.readline(), "Type in a number:33\n")
            self.assertEqual(p.stdout.readline(), "Exiting program.\n")

    def test_create_with_invalid_kwarg(self):
        with self.assertRaises(TypeError):
            with popen("some_command", weird_parameter=30) as p:
                pass

    def test_run_stdout(self):
        command = self.get_test_command("test_program.py")
        stdout, stderr = popen_call(command)

        self.assertEqual(stdout, "non-interactive program.\nExiting...\n")
        self.assertEqual(stderr, "")

    def test_run_stdin(self):
        command = self.get_test_command("test_input_program.py")
        stdout, stderr = popen_call(command, "1 2 3 4")

        self.assertEqual(stdout, "10\n")
        self.assertEqual(stderr, "")

    def test_run_stderr(self):
        command = self.get_test_command("test_input_program.py")
        stdout, stderr = popen_call(command, "1 p 5")

        self.assertEqual(stderr, "INVALID INPUT\n")
        self.assertEqual(stdout, "")
