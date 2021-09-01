import os
from dotenv import load_dotenv
load_dotenv()

class SetUp:
    debug = int(os.getenv('DEBUG'))
    secret_key = os.getenv('SECRET_KEY')

    def set_allowed_host(self):
        host=[]
        if self.debug == 0:
            host.append(os.getenv('HOST1'))
            host.append(os.getenv('HOST2'))
        return host