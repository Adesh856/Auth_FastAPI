from ...auth import JWTTokenAuthMiddleware

auth = JWTTokenAuthMiddleware(required=False)