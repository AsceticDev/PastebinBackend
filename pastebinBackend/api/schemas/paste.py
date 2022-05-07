from pastebinBackend.models import Paste
from pastebinBackend.extensions import ma,db

class PasteSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    author = ma.Nested('pastebinBackend.api.schemas.user.UserSchema', dump_only=True, exlude=["pastes"])
    timeCreated = ma.DateTime(dump_only=True)

    class Meta:
        model = Paste
        dqla_session = db.session
        include_fk = True
        load_instance = True