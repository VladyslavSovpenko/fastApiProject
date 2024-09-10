from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    def create_hash(self, password):
        return pwd_context.hash(password)

    def verify_hash(self, password, hashed_password):
        return pwd_context.verify(password, hashed_password)
