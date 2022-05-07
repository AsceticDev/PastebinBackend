from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pastebinBackend.api.schemas import PasteSchema 
from pastebinBackend.models import Paste
from pastebinBackend.extensions import db
from pastebinBackend.commons.pagination import paginate


class PasteResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      summary: Get a paste
      description: Get a single paste by ID
      parameters:
        - in: path
          name: paste_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  paste: PasteSchema
        404:
          description: paste does not exists
    put:
      tags:
        - api
      summary: Update a paste 
      description: Update a single paste by ID
      parameters:
        - in: path
          name: paste_id 
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              PasteSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: paste updated
                  paste: PasteSchema
        404:
          description: paste does not exists
    delete:
      tags:
        - api
      summary: Delete a paste 
      description: Delete a single paste by ID
      parameters:
        - in: path
          name: paste_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: paste deleted
        404:
          description: paste does not exists
    """

    method_decorators = [jwt_required()]

    def get(self, paste_id):
        schema = PasteSchema()
        paste = Paste.query.get_or_404(paste_id)
        return {"paste": schema.dump(paste)}

    def put(self, paste_id):
        schema = PasteSchema(partial=True)
        paste = Paste.query.get_or_404(paste_id)
        paste = schema.load(request.json, instance=paste)

        db.session.commit()

        return {"msg": "paste updated", "paste": schema.dump(paste)}

    def delete(self, paste_id):
        paste = Paste.query.get_or_404(paste_id)
        db.session.delete(paste)
        db.session.commit()

        return {"msg": "paste deleted"}


class PasteList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      summary: Get a list of pastes 
      description: Get a list of paginated pastes 
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/PasteSchema'
    post:
      tags:
        - api
      summary: Create a paste
      description: Create a new paste 
      requestBody:
        content:
          application/json:
            schema:
              PasteSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: paste created
                  paste: PasteSchema
    """

    method_decorators = [jwt_required()]

    def get(self):
        schema = PasteSchema(many=True)
        query = Paste.query
        return paginate(query, schema)

    def post(self):
        schema = PasteSchema()
        paste = schema.load(request.json)

        db.session.add(paste)
        db.session.commit()

        return {"msg": "paste created", "paste": schema.dump(paste)}, 201

