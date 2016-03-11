import os
import tempfile

from contextlib import contextmanager
from subprocess import PIPE, Popen


@contextmanager
def make_temp(suffix="", prefix="tmp", dir=None):
    """
    Creates a temporary file with a closed stream and deletes it when done.

    :return: A contextmanager retrieving the file path.
    """
    temporary = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=dir)
    os.close(temporary[0])
    try:
        yield temporary[1]
    finally:
        os.remove(temporary[1])


@contextmanager
def popen(command, **kwargs):
    """
    This function creates a context manager that sets up the process
    (using POpen), returns to caller, closes streams and waits for
    process to exit on leaving.

    The process is opened in ``universal_newlines`` mode by default and with
    PIPEs for stdin, stderr, and stdout.
    If a custom kwarg is given for stdin, stderr, or stdout, it is expected to
    have a ``.close()`` method which is called when leaving.

    :param command: The command to run using POpen.
    :param kwargs:  Additional keyword arguments to pass to
                    ``subprocess.Popen`` that is used to spawn the process.
    :return:        A context manager yielding the process started from the
                    command.
    """
    stdout = kwargs.pop('stdout', PIPE)
    stderr = kwargs.pop('stderr', PIPE)
    stdin = kwargs.pop('stdin', PIPE)
    process = Popen(command, stdout=stdout, stderr=stderr, stdin=stdin,
                    universal_newlines=kwargs.pop('universal_newlines', True),
                    **kwargs)
    stdout = process.stdout if process.stdout else stdout
    stderr = process.stderr if process.stderr else stderr
    stdin = process.stdin if process.stdin else stdin
    try:
        yield process
    finally:
        stdout.close()
        stderr.close()
        stdin.close()
        process.wait()


def popen_call(command, stdin=None, **kwargs):
    """
    Run a command using POpen and return the read stdout and stderr data.
    This function waits for the process to exit (is synchronous).

    :param command: The command to run using POpen.
    :param stdin:   Initial input to send to the process.
    :param kwargs:  Additional keyword arguments to pass to ``popen()``.
    :return:        A tuple with ``(stdoutstring, stderrstring)``. Same
                    as the value returned from ``POpen.communicate()``
    """
    with popen(command, **kwargs) as p:
        return p.communicate(stdin)
