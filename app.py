from flask import Flask, render_template, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "message": "Application is running"})

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found", "status": 404}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "status": 500}), 500

if __name__ == '__main__':
    app.run(debug=True)
