from flask import abort, make_response, request
from flask_restful import Resource
from models import CastMember, Production, db


class CastMemberResource(Resource):
    def get(self, id):
        cast_member = self.get_cast_member(id)
        return make_response(cast_member.to_dict(), 200)

    def patch(self, id):
        cast_member_json = request.get_json()
        cast_member = self.get_cast_member(id)

        if cast_member_json.get("name"):
            cast_member.name = cast_member_json.get("name")
            db.session.commit()
            return make_response(cast_member.to_dict(), 200)

    def delete(self):
        cast_member = self.get_cast_member(id)
        db.session.delete(cast_member)
        db.session.commit()
        return "", 204

    def get_cast_member(self, id):
        cast_member = CastMember.query.get(id)
        if not cast_member:
            abort(404, "Cast member not found.")
        return cast_member


class CastMembersResource(Resource):
    def get(self):
        members = CastMember.query.all()
        return make_response([m.to_dict() for m in members], 200)

    def post(self):
        cast_member_json = request.get_json()
        production = Production.query.get(cast_member_json.get("production_id"))
        if production:
            cast_member = CastMember(
                name=cast_member_json.get("name"),
                production_id=cast_member_json.get("production_id"),
            )
            db.session.add(cast_member)
            db.session.commit()
            return cast_member.to_dict(), 201
