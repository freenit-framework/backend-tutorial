from freenit.api import register_endpoints


def create_api(app):
    from .blog import blueprint as blog
    register_endpoints(
        app, '/api/v0',
        [
            blog,
        ])
