# from flask import Flask, request, jsonify, render_template
# import subprocess
# import os 
# os.chdir(r'C:\Users\yuvra\Documents\project\yolov9')


# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('Camera.html')

# @app.route('/run-script', methods=['POST'])
# def run_script():
#     try:
#         # Run the detect_dual.py script with the specified arguments
#         result = subprocess.run(
#             ['python', 'detect_dual.py', '--weights', 'yolov9-c.pt', '--conf', '0.5', '--source', '0', '--device', '0'],
#             capture_output=True,
#             text=True
#         )
#         return jsonify({'output': result.stdout, 'error': result.stderr})
#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)