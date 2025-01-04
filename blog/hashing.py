from passlib.context import CryptContext

# Create a CryptContext instance to handle password hashing and verification.
# The "schemes" parameter specifies the hashing algorithm to use, in this case, "bcrypt".
# The "deprecated" parameter set to "auto" ensures that deprecated algorithms are automatically upgraded.
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Define a `Hash` class to handle password hashing and verification.
class Hash():
    # Method to hash a plain-text password using bcrypt.
    @staticmethod
    def bcrypt(password: str):
        # The `hash` method of CryptContext hashes the provided password.
        return pwd_cxt.hash(password)

    # Method to verify if a plain-text password matches a hashed password.
    @staticmethod
    def verify(plain_password, hashed_password):
        # The `verify` method checks the plain-text password against the hashed password.
        return pwd_cxt.verify(plain_password, hashed_password)
