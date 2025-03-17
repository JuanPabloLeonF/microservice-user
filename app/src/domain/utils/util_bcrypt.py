import bcrypt

class UtilsBcrypt:

    @staticmethod
    def hashPassword(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verifyPassword(password: str, hashedPassword: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashedPassword.encode('utf-8'))