from dataclasses import dataclass


@dataclass
class Hello:
    name: str = "world"
    excited: bool = False

    def greet(self) -> str:
        punctuation = "!" if self.excited else "."
        return f"Hello, {self.name}{punctuation}"
