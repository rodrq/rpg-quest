from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.datastructures import MutableHeaders

class TokenToAuthorizationMiddleware(BaseHTTPMiddleware):
    #Custom middleware to format cookie token to Authorization bearer
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        token_cookie = request.cookies.get("token")
        if token_cookie:
            new_header = MutableHeaders(request._headers)
            new_header["Authorization"]= f"Bearer {token_cookie}" 
            request._headers = new_header
            request.scope.update(headers=request.headers.raw)
            
        response = await call_next(request)

        return response

