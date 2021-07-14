# weather_api

Create virtual env - <code>python3 -m venv env</code></br>
Install requirements - <code>pip3 install -r requirements.txt</code></br>

Create redis user <code> set user:1 User </code><br>
<code> set password:1 password </code>

In weather_app run <code>celery -A weather_app worker --loglevel=info </code>

