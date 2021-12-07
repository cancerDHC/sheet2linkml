"""
test_command_line.py: Test the command line interfaces of this program.
"""

import subprocess

def execute_sheet2linkml(args) -> (int, str, str):
    """
    Execute sheet2linkml as a command-line tool with the provided arguments.

    :param args: A list of arguments to send to sheet2linkml
    :return: A tuple containing the error code, captured STDOUT and captured STDERR respectively
    """

    result = subprocess.run(['sheet2linkml'] + args, capture_output=True, encoding='utf-8')

    return result.returncode, result.stdout, result.stderr


class TestCommandLine:
    """
    Test execution of the `sheet2linkml` script at the command line.
    """

    def test_help(self):
        """
        Test whether sheet2linkml accepts `--help` and provides useful information.
        """
        (errno, stdout, stderr) = execute_sheet2linkml(['--help'])

        assert errno == 0
        assert 'Usage: sheet2linkml' in stdout
        assert '--help' in stdout
        assert 'Show this message and exit.' in stdout
        assert 'ERROR' not in stderr
