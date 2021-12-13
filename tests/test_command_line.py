"""
test_command_line.py: Test the command line interfaces of this program.
"""
import re
import subprocess
import logging
import os


def execute_sheet2linkml(args) -> (int, str, str):
    """
    Execute sheet2linkml as a command-line tool with the provided arguments.

    :param args: A list of arguments to send to sheet2linkml
    :return: A tuple containing the error code, captured STDOUT and captured STDERR respectively
    """

    result = subprocess.run(
        ["sheet2linkml"] + args, capture_output=True, encoding="utf-8"
    )

    return result.returncode, result.stdout, result.stderr


class TestCommandLine:
    """
    Test execution of the `sheet2linkml` script at the command line.
    """

    def test_help(self):
        """
        Test whether sheet2linkml accepts `--help` and provides useful information.
        """
        (errno, stdout, stderr) = execute_sheet2linkml(["--help"])

        print(stderr)

        assert errno == 0
        assert "Usage: sheet2linkml" in stdout
        assert "--help" in stdout
        assert "Show this message and exit." in stdout
        assert "ERROR" not in stderr

    def test_execution(self, tmp_path):
        """
        Test whether sheet2linkml can be used to process a particular Google Sheet into LinkML, which is located at
        https://docs.google.com/spreadsheets/d/1HpsF12vl_CeIzV2TEtANeysnh7cy6YOUDdv6fMXT00I/edit?usp=sharing
        """

        output_path = os.path.join(tmp_path, "schema.yaml")

        print(f"Writing execution test output to '{output_path}'")

        (errno, stdout, stderr) = execute_sheet2linkml(
            [
                "--google-sheet-id",
                "1HpsF12vl_CeIzV2TEtANeysnh7cy6YOUDdv6fMXT00I",
                "-o",
                output_path,
            ]
        )

        print(stderr)
        assert (
            'INFO: Google Sheet loaded: GSheetModel with an underlying Google Sheet titled "Test schema for sheet2linkml" containing 8 worksheets'
            in stderr
        )
        assert (
            'INFO: Generating LinkML for GSheetModel with an underlying Google Sheet titled "Test schema for sheet2linkml" containing 8 worksheets'
            in stderr
        )
        assert (
            'INFO: Generating LinkML for Enum named Subject.breed from worksheet "O_CCDH Enums" containing 8 values'
            in stderr
        )

        assert stdout == ""
        assert errno == 0

        assert os.path.exists(output_path)

        # Ensure that we get the same output from sheet2linkml as we expected.
        def make_schema_comparable(lines):
            """
            Some parts of the schema are not comparable, so we remove them before comparing them.
            """

            output = ""
            for line in lines:
                if line.startswith("generation_date:"):
                    continue
                if re.match("^\\s*code_set_version: ", line):
                    continue
                output += line

            return output

        dirname = os.path.dirname(__file__)
        with open(
            os.path.join(
                dirname,
                "testing-schema-on-gsheet/1HpsF12vl_CeIzV2TEtANeysnh7cy6YOUDdv6fMXT00I.yaml",
            ),
            "r",
        ) as f:
            expected_schema = make_schema_comparable(f.readlines())

        with open(output_path, "r") as f:
            obtained_schema = make_schema_comparable(f.readlines())

        assert obtained_schema != ""
        assert obtained_schema == expected_schema
