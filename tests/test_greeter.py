from foundit_hello import Hello
from foundit_hello.cli import main


def test_default_greeting():
    assert Hello().greet() == "Hello, world."


def test_excited_greeting():
    assert Hello(name="Ada", excited=True).greet() == "Hello, Ada!"


def test_cli(capsys):
    assert main(["Ada", "--excited"]) == 0
    assert capsys.readouterr().out.strip() == "Hello, Ada!"


def test_cli_defaults(capsys):
    assert main([]) == 0
    assert capsys.readouterr().out.strip() == "Hello, world."
