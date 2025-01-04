from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog.token import verify_token  # Importing the function to validate the JWT token.
from typing import Annotated  # For better type annotation and clarity.

# Initialize OAuth2PasswordBearer with the token URL.
# This is the endpoint that clients will use to obtain the access token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Function to get the current authenticated user based on the provided token.
# The token is passed through the 'Authorization: Bearer <token>' header.
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # Debugging statement to print the received token.
    print(f"Received token in get_current_user: {token}")

    # Create an HTTPException to be raised if the token is invalid.
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,  # HTTP 401 Unauthorized status.
        detail="Could not validate credentials",  # Detailed error message.
        headers={"WWW-Authenticate": "Bearer"},  # Hint to the client that a Bearer token is expected.
    )

    # Use the `verify_token` function to validate the token and return the decoded user information.
    return verify_token(token, credentials_exception)
