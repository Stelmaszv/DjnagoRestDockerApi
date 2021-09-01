import os
from dotenv import load_dotenv
load_dotenv()

class SetUp:
    debug = int(os.getenv('DEBUG'))
    secret_key = os.getenv('SECRET_KEY')
    heroku = os.getenv('heroku')

    def set_allowed_host(self):
        host=[]
        if self.heroku==0:
            if self.debug == 0:
                host.append(os.getenv('HOST1'))
                host.append(os.getenv('HOST2'))
        else:
            if self.debug == 1:
                host.append(os.getenv('HOST3'))
        return host