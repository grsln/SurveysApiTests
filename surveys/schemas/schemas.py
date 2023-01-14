from voluptuous import PREVENT_EXTRA, Schema

SchemaCreateUser = Schema(
    {
        "username": str,
        "email": str,
        "id": int,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

SchemaLoginUnsuccessful = Schema({"password": list}, required=True, extra=PREVENT_EXTRA)

SchemaLoginSuccessful = Schema(
    {"access": str, "refresh": str}, required=True, extra=PREVENT_EXTRA
)

SchemaUpdateUser = Schema(
    {
        "username": str,
        "email": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)
