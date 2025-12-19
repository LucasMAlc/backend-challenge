from sqlalchemy import select
from models import User, Role, Claim, user_claims

# Consulta usando SQLAlchemy Expression Language
query = (
    select(
        User.id.label('user_id'),
        User.name.label('user_name'),
        User.email.label('user_email'),
        Role.description.label('role_description'),
        Claim.description.label('claim_description')
    )
    .select_from(User)
    .join(Role, User.role_id == Role.id)
    .outerjoin(user_claims, User.id == user_claims.c.user_id)
    .outerjoin(Claim, (user_claims.c.claim_id == Claim.id) & (Claim.active == True))
    .order_by(User.name, Claim.description)
)
