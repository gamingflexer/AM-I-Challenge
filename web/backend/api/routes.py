from .views import *


# pageview test
def initialize_routes(api):
    api.add_resource(helloworld, '/hello')
