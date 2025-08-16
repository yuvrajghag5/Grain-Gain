# # Combined app.py
# from flask import Flask, Response, render_template, request, jsonify, send_from_directory
# import cv2
# import torch
# import sys
# from pathlib import Path
# from flask_cors import CORS
# import numpy as np
# import pandas as pd
# import Test
# from models.common import DetectMultiBackend
# from utils.general import check_img_size, non_max_suppression, scale_boxes
# from utils.plots import Annotator, colors
# from utils.torch_utils import select_device



# app = Flask(__name__, template_folder='.', static_folder='.')
# from flask_cors import CORS
# # CORS(app, resources={r"/*": {"origins": "*"}})


# @app.route('/')
# def index():
#     return render_template('Sign-in.html')

# def get_all_food_items():
#     veg_df = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts\veggie_list.pkl')
#     non_veg_df = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\nonveg_list.pkl')
#     return pd.concat([veg_df, non_veg_df])['Name'].tolist()

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     user_input = request.form.get('user_input')
#     rec_type = request.form.get('type', 'veg')
#     try:
#         if rec_type == 'veg':
#             recommendations = Test.veggie_recommender(user_input)
#         elif rec_type == 'veg-to-nonveg':
#             recommendations = Test.recommend_non_veg_for_veg_item(user_input)
#         else:
#             recommendations = Test.recommend_veg_for_non_veg_item(user_input)

#         return jsonify({'status': 'success', 'recommendations': [{'name': name} for name in recommendations]})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# @app.route('/food-items', methods=['GET'])
# def get_foods():
#     try:
#         return jsonify({'status': 'success', 'items': get_all_food_items()})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True, port=5500)
