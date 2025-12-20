from sqlalchemy import Table, Column, BigInteger, ForeignKey
from app.database import Base

# Tabela associativa para relacionamento many-to-many entre User e Claim
user_claims = Table(
    'user_claims',
    Base.metadata,
    Column('user_id', BigInteger, ForeignKey('users.id'), primary_key=True),
    Column('claim_id', BigInteger, ForeignKey('claims.id'), primary_key=True)
)