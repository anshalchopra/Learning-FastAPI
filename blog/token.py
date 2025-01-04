from datetime import datetime, timedelta
from typing import Optional
from blog.schema import TokenData  # Import TokenData model (for returning email after verifying token)
from fastapi.params import Depends
from jose import jwt, JWTError  # Import jose for encoding and decoding JWT tokens

# Secret key for signing the JWT tokens (must be kept secret in production)
SECRET_KEY = "218c55d66c80bbb2f72820582d0d4c6b322657b6ff53e9fa6890ea7cd163b46f"
# Algorithm used to sign the JWT token (HS256 is symmetric encryption)
ALGORITHM = "HS256"
# Time after which the access token expires (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Function to create a new access token
def create_access_token(data: dict):
    # Copy the input data to avoid modifying the original data
    to_encode = data.copy()
    # Set the token's expiration time by adding 15 minutes from the current UTC time
    expire = datetime.utcnow() + timedelta(minutes=15)
    # Update the data dictionary to include the expiration time (exp claim)
    to_encode.update({"exp": expire})
    # Encode the JWT token using the data, secret key, and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # Return the generated token
    return encoded_jwt


# Function to verify the validity of an access token
def verify_token(token: str, credentials_exception):
    print(f"verify_token token: {token}")  # Print the received token for debugging purposes
    try:
        # Decode the JWT token using the secret key and the algorithm to retrieve the payload
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extract the 'sub' claim (subject), which in this case is the user's email
        email: str = payload.get("sub")
        # If the email is not found in the payload, raise the credentials exception
        if email is None:
            raise credentials_exception
        # Create a TokenData object with the email from the token
        token_data = TokenData(email=email)
    except JWTError:
        # If decoding or any JWT-related error occurs, raise the credentials exception
        raise credentials_exception
    # Return the token data (e.g., the user's email)
