import secrets
import string
from passlib.context import CryptContext

# Contexto para hash de senhas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_password(length: int = 12) -> str:
    """
    Gera uma senha aleatória segura.
    
    A senha contém letras maiúsculas, minúsculas, dígitos e caracteres especiais.
    
    Args:
        length: Tamanho da senha (padrão: 12)
        
    Returns:
        str: Senha gerada
        
    Example:
        >>> senha = generate_password()
        >>> len(senha)
        12
        >>> senha = generate_password(16)
        >>> len(senha)
        16
    """
    # Define os caracteres permitidos
    alphabet = string.ascii_letters + string.digits + "!@#$%&*"
    
    # Gera senha aleatória de forma segura
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password


def hash_password(password: str) -> str:
    """
    Cria hash da senha usando bcrypt.
    
    Args:
        password: Senha em texto plano
        
    Returns:
        str: Hash da senha
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha corresponde ao hash.
    
    Args:
        plain_password: Senha em texto plano
        hashed_password: Hash da senha
        
    Returns:
        bool: True se a senha é válida
    """
    return pwd_context.verify(plain_password, hashed_password)