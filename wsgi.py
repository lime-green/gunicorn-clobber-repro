import json


def application(environ, start_response):
    if environ["QUERY_STRING"] == "read_body=1":
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        environ["wsgi.input"].read(request_body_size)

    data = b"a" * 100 * 1024
    response_headers = [
        ("Content-Length", str(len(data))),
    ]
    start_response("200 OK", response_headers)
    return [data]
