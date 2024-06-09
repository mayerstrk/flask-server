from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def main():
    # Get the IP address of the client making the request
    client_ip = request.remote_addr
    return f"Hello World, you are calling me from {client_ip}\n"


if __name__ == "__main__":
    # Run the app on all available IPs (makes it accessible on your local network) and on port 5000
    app.run(host="0.0.0.0", port=5000)
