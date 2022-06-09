import os
from dotenv import load_dotenv

load_dotenv()

# get environment variables
def get_env():
    return {
        "svc": os.environ['svc']
    }
