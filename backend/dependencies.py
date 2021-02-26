from fastapi import Header, HTTPException


# x-auth-key
async def handle_auth_key(x_auth_key: str = Header(...)):
    if x_auth_key != "fake+password":
        return HTTPException(status_code=400)
    