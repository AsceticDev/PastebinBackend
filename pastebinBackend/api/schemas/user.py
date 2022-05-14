from pastebinBackend.models import User
from pastebinBackend.extensions import ma, db


class UserSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    password = ma.String(load_only=True, required=True)
    pastes = ma.List(ma.Nested("pastebinBackend.api.schemas.paste.PasteSchema"), exclude=["author"], dump_only=True)

    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        exclude = ("_password",)
