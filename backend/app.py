try:
    import unzip_requirements
except ImportError:
    pass

import os
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api import app
from api.queries import query, publicSpace
from api.mutations import mutation

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,
    query,
    publicSpace,
    snake_case_fallback_resolvers,
    mutation
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    db_user = os.environ['DB_USER']
    db_pw = os.environ['DB_PASSWORD']
    print(db_user, db_pw)
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
