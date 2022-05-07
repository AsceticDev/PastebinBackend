from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from pastebinBackend.extensions import apispec
from pastebinBackend.api.resources import UserResource, UserList, PasteResource, PasteList
from pastebinBackend.api.schemas import UserSchema, PasteSchema


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:user_id>", endpoint="user_by_id")
api.add_resource(UserList, "/users", endpoint="users")

api.add_resource(PasteResource, "/pastes/<int:paste_id>", endpoint="paste_by_id")
api.add_resource(PasteList, "/pastes", endpoint="pastes")

@blueprint.before_app_first_request
def register_views():
    # Components
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.components.schema("PasteSchema", schema=PasteSchema)

    # Routes
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)
    apispec.spec.path(view=PasteResource, app=current_app)
    apispec.spec.path(view=PasteList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
