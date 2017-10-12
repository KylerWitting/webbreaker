import pytest
import re
from click.testing import CliRunner

# Set up click fixture


def test_webbreaker():
    from webbreaker.__main__ import cli as webbreaker

    runner = CliRunner()
    result = runner.invoke(webbreaker)
    assert "SYNOPSIS" in result.output
    assert "DESCRIPTION" in result.output
    assert "COMMANDS" in result.output
    assert "UPPER-LEVEL COMMANDS" in result.output
    assert "LOWER-LEVEL COMMANDS" in result.output
    assert result.exit_code == 0


def test_webinspect():
    from webbreaker.__main__ import cli as webbreaker

    runner = CliRunner()
    result = runner.invoke(webbreaker, ['webinspect'])
    print(result.output)
    # r = re.search('\/.*\/(.*)', path)

    assert result.exit_code == 0
    assert 0  # Check print


def test_fortify():
    from webbreaker.__main__ import cli as webbreaker

    runner = CliRunner()
    result = runner.invoke(webbreaker, ['fortify'])
    print(result.output)

    assert result.exit_code == 0
    assert 0  # Check print


def test_agent():
    from webbreaker.__main__ import cli as webbreaker

    runner = CliRunner()
    result = runner.invoke(webbreaker, ['admin'])
    print(result.output)

    assert result.exit_code == 0
    assert 0  # Check print
# def options_test_size():
#     runner = CliRunner()
#     try:
#         # test 'medium' - should pass
#         res = runner.invoke(webinspect, ['scan', '--size=medium'])
#         assert res.exit_code == 0
#         # test 'large' - should pass
#         res = runner.invoke(webinspect, ['scan', '--size=large'])
#         assert res.exit_code == 0
#         # test 'really_big' - should fail
#         res = runner.invoke(webinspect, ['scan', '--size=pretty_big'])
#         assert res.exit_code == 2
#     except AssertionError:
#         click.echo('Test failure in options_test_size()\nCLI output is: \n\n' + res.output)
#         exit(1)
#
# def options_test_x():
#     runner = CliRunner()
#     try:
#         # test 'fpr' - should pass
#         res = runner.invoke(webinspect, ['scan', '-x', 'fpr'])
#         assert res.exit_code == 0
#         # test 'xml' - should pass
#         res = runner.invoke(webinspect, ['scan', '-x', 'xml'])
#         assert res.exit_code == 0
#         # test 'scan' - should pass
#         res = runner.invoke(webinspect, ['scan', '-x', 'scan'])
#         assert res.exit_code == 0
#         # test 'pdf' - should fail
#         res = runner.invoke(webinspect, ['scan', '-x', 'pdf'])
#         assert res.exit_code == 2
#     except AssertionError:
#         click.echo('Test failure in options_test_x()\nCLI output is: \n\n' + res.output)
#         exit(1)
#
# def options_test_scan_mode():
#     runner = CliRunner()
#     try:
#         # test crawl - should pass
#         res = runner.invoke(webinspect, ['scan', '--scan_mode=crawl'])
#         assert res.exit_code == 0
#         # test scan - should pass
#         res = runner.invoke(webinspect, ['scan', '--scan_mode=scan'])
#         assert res.exit_code == 0
#         # test all - should pass
#         res = runner.invoke(webinspect, ['scan', '--scan_mode=all'])
#         assert res.exit_code == 0
#         # test ddos - should fail
#         res = runner.invoke(webinspect, ['scan', '--scan_mode=ddos'])
#         assert res.exit_code == 2
#     except AssertionError:
#         click.echo('Test failure in options_test_scan_mode()\nCLI output is: \n\n' + res.output)
#         exit(1)
#
#
#
#
# def test_choice_options():
#     options_test_size()
#     options_test_x()
#     options_test_scan_mode()
#
#
#
# # Desired Future Tests
#
# # def test_defaults():
# #       Test that scan_name == '-'
# #       Test that settings == 'Default'
# #       Test that x == 'fpr'
# #       Test that allowed_hosts == start_urls (only one argument)
# #       Test that allowed_hosts == start_urls (multiple arguments)
#
#
# # def test_multiple_arguments:
# #       Test that start_urls accepts multiple arguments
# #       Test that list_scans accepts multiple arguments
# #       Test that allowed_hosts accepts multiple arguments
#
#
#
# if __name__ == '__main__':
#     test_help()
#     test_choice_options()