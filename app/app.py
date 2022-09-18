from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app_code = Flask('app_code')
metrics = PrometheusMetrics(app_code)

@app_code.route('/')
def index():
    return 'Olá mundo!'

@app_code.route('/healthcheck', methods=['GET'])
def healthy():
    return '{ status: OK }'

@app_code.route('/limpar', methods=['GET'])
def limpar():
    return 'limpa aplicacao!'

@app_code.route('/popular', methods=['GET'])
def popular():
    return 'popular aplicacao'


def verificar_banco()


if __name__ == 'app_code':
    app_code.run(host='0.0.0.0', port=8010) 
