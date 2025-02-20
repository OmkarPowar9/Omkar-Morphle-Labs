from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER", "codespace")

    # Get current server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get htop output using top command
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Name: Omkar Powar
    User: {username}
    Server Time (IST): {ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")}
    
    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
