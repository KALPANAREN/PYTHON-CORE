from typing import Any, Callable, Optional, Type

class Field:
    """
    A reusable data descriptor for validated, typed attributes.

    Features:
    - Type enforcement
    - Custom validator hook
    - Optional read-only after first set
    - Default value support
    - Clear error messages
    - Instance-safe storage
    """

    def __init__(
        self,
        *,
        expected_type: Type,
        default: Any = None,
        validator: Optional[Callable[[Any], None]] = None,
        readonly: bool = False,
    ):
        self.expected_type = expected_type
        self.default = default
        self.validator = validator
        self.readonly = readonly
        self.private_name = None  # assigned in __set_name__

    def __set_name__(self, owner, name):
        # Avoid attribute name conflicts across classes
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner=None):
        if instance is None:
            return self  # Accessed on class, return descriptor itself

        if self.private_name not in instance.__dict__:
            if self.default is not None:
                return self.default
            raise AttributeError(f"{self.private_name} has not been set")

        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if self.readonly and self.private_name in instance.__dict__:
            raise AttributeError("Field is read-only once set")

        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )

        if self.validator:
            self.validator(value)

        instance.__dict__[self.private_name] = value

    def __delete__(self, instance):
        raise AttributeError("Field cannot be deleted")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"type={self.expected_type.__name__}, "
            f"readonly={self.readonly})"
        )

def positive(value: int):
    if value <= 0:
        raise ValueError("Value must be positive")

class User:
    id = Field(expected_type=int, readonly=True)
    name = Field(expected_type=str)
    age = Field(expected_type=int, validator=positive, default=18)


u = User()
u.id = 1001
u.name = "Ada"
u.age = 30

print(u.id, u.name, u.age)
