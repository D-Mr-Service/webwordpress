import os

def generate_requirements():
    os.system("pip freeze > requirements.txt")

generate_requirements()
