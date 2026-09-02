# foundit-hello

A tiny example package demonstrating Python packaging.

## Install

```console
pip install foundit-hello
```

## Usage

```console
$ hello
Hello, world.
$ hello Ada --excited
Hello, Ada!
```

Or from Python:

```python
from foundit_hello import Hello

Hello(name="Ada", excited=True).greet()  # "Hello, Ada!"
```
