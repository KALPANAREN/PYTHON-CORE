# ORM-Style Model From Database Schema

def create_model_class(table_name, columns):
    """
    columns = {
        "id": int,
        "name": str,
        "age": int
    }
    """

    def __init__(self, **kwargs):
        for field in columns:
            setattr(self, field, kwargs.get(field))

    attrs = {
        "__init__": __init__,
        "__tablename__": table_name,
        "__annotations__": columns,
    }

    return type(table_name.capitalize(), (), attrs)

User = create_model_class(
    "users",
    {"id": int, "name": str, "age": int}
)

u = User(id=1, name="Ada", age=30)
print(u.name)

# JSON Schema → Runtime Data Model

def model_from_schema(name, schema):
    """
    schema = {
        "title": str,
        "price": float
    }
    """

    def __init__(self, **data):
        for field, field_type in schema.items():
            value = data.get(field)
            if not isinstance(value, field_type):
                raise TypeError(f"{field} must be {field_type}")
            setattr(self, field, value)

    return type(name, (), {"__init__": __init__})

Product = model_from_schema(
    "Product",
    {"title": str, "price": float}
)

p = Product(title="Laptop", price=999.0)

# API Endpoint Class Generator

def create_endpoint(name, handler_func, path):
    def handle(self, request):
        return handler_func(request)

    return type(
        name,
        (),
        {
            "path": path,
            "handle": handle,
        }
    )

def get_users(request):
    return {"users": []}

UsersEndpoint = create_endpoint(
    "UsersEndpoint",
    get_users,
    "/users"
)

endpoint = UsersEndpoint()
print(endpoint.handle({}))

# Plugin System (Runtime Behavior Injection)

def build_plugin(name, behavior):
    def run(self, data):
        return behavior(data)

    return type(
        name,
        (),
        {"run": run}
    )

UpperPlugin = build_plugin(
    "UpperPlugin",
    lambda x: x.upper()
)

p = UpperPlugin()
print(p.run("hello"))

# Config-Driven Service Class

def create_service(name, config):
    def process(self, value):
        return value * self.multiplier

    attrs = {
        "multiplier": config["multiplier"],
        "process": process,
    }

    return type(name, (), attrs)

PaymentService = create_service(
    "PaymentService",
    {"multiplier": 1.2}
)

svc = PaymentService()
print(svc.process(100))

