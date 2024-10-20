from flask import Flask
from prometheus_client import make_wsgi_app, Gauge
from prometheus_client import CollectorRegistry
import psutil

app = Flask(__name__)

# Create a Prometheus registry
registry = CollectorRegistry()

cpu_usage_gauge = Gauge('system_cpu_usage', 'CPU usage percentage', registry=registry)
memory_usage_gauge = Gauge('system_memory_usage', 'Memory usage percentage', registry=registry)

@app.route('/metrics')
def metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    cpu_usage_gauge.set(cpu_usage)
    memory_usage_gauge.set(memory_usage)

    return make_wsgi_app(registry)

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
