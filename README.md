Discord bot using PaLM Generative Ai for Diversity, Inclusion and Equity in the workplace

requires:
python3
discord.py
dotenv
google.generativeai

Steps to run:
1. create venv: python -m venv path/to/venv
2. use venv: source path/to/venv/bin/activate
3. install libaries:
    - pip install google.generativeai
    - pip install discord.py
    - pip install dotenv
5. rename .env.example to .env
    - replace palm_key and discord token with your keys
6. run: python ai.py
