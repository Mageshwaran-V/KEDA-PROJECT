apiVersion: v1
kind: ConfigMap
metadata:
  name: sum-config
data:
  server.py: |
    from flask import Flask
    import os

    app = Flask(__name__)

    @app.route('/')
    def calculate_sum():
        a = int(os.environ.get('A', 10))
        b = int(os.environ.get('B', 20))
        d = int(os.environ.get('D', 30))
        c = a + b + d # Compute the sum
        return f"Values: A={a}, B={b},D={d} Sum (C): {c}"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

