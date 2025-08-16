# app.py
from flask import Flask, Response, render_template, send_from_directory, request, jsonify  
import cv2
import torch
import sys
from pathlib import Path
from flask_cors import CORS
import app1
import Test
# Add the YOLO directory to path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# Import YOLO functions
from models.common import DetectMultiBackend
from utils.general import check_img_size, non_max_suppression, scale_boxes
from utils.plots import Annotator, colors
from utils.torch_utils import select_device
import numpy as np
import pandas as pd

class Description:
    descriptions = {
        0: "human",
        1: "two-wheeled vehicle",
        2: "four-wheeled vehicle",
        3: "two-wheeled motor vehicle",
        4: "flying vehicle",
        5: "large motor vehicle",
        6: "rail vehicle",
        7: "heavy motor vehicle",
        8: "watercraft",
        9: "traffic control device",
        10: "fire control device",
        11: "traffic control sign",
        12: "parking device",
        13: "seating furniture",
        14: "avian species",
        15: "feline species",
        16: "canine species",
        17: "equine species",
        18: "ovine species",
        19: "bovine species",
        20: "large mammal",
        21: "bear species",
        22: "striped mammal",
        23: "long-necked mammal",
        24: "carrying device",
        25: "rain protection device",
        26: "hand-carrying device",
        27: "clothing accessory",
        28: "traveling device",
        29: "throwing object",
        30: "winter sports equipment",
        31: "winter sports equipment",
        32: "sports equipment",
        33: "flying object",
        34: "baseball equipment",
        35: "baseball equipment",
        36: "skating equipment",
        37: "surfing equipment",
        38: "tennis equipment",
        39: "container",
        40: "glass container",
        41: "drinking container",
        42: "eating utensil",
        43: "cutting utensil",
        44: "eating utensil",
        45: "eating container",
        46: "pro-1.1 fiber-2.6 cal-89",
        47: "pro-0.3 fiber-2.4 cal-52",
        48: "food item",
        49: "pro-0.9 fiber-2.4 cal-47",
        50: "pro-2.8 fiber-2.6 cal-34",
        51: "pro-0.9 fiber-2.8 cal-41",
        52: "food item",
        53: "food item",
        54: "food item",
        55: "food item",
        56: "furniture",
        57: "furniture",
        58: "plant",
        59: "furniture",
        60: "furniture",
        61: "sanitary fixture",
        62: "electronic device",
        63: "computer",
        64: "input device",
        65: "remote control",
        66: "input device",
        67: "communication device",
        68: "cooking appliance",
        69: "cooking appliance",
        70: "cooking appliance",
        71: "sanitary fixture",
        72: "refrigeration appliance",
        73: "reading material",
        74: "timekeeping device",
        75: "decorative container",
        76: "cutting tool",
        77: "stuffed toy",
        78: "hair styling device",
        79: "oral hygiene device"
    }
from flask_cors import CORS
app = Flask(__name__, template_folder='.', static_folder='.')
# CORS(app, resources={r"/*": {"origins": "*"}})


# Initialize YOLO model
weights = 'yolov9-c.pt'
device = select_device('')
model = DetectMultiBackend(weights, device=device)
stride = model.stride
imgsz = check_img_size((640, 640), s=stride)

def process_frame(frame):
    # Prepare image for YOLO
    im = cv2.resize(frame, (640, 640))
    im = im.transpose((2, 0, 1))[::-1]
    im = np.ascontiguousarray(im)
    im = torch.from_numpy(im).to(device)
    im = im.float() / 255.0
    if len(im.shape) == 3:
        im = im[None]

    # Inference
    pred = model(im, augment=False, visualize=False)
    pred = pred[0][1]

    # NMS
    pred = non_max_suppression(pred, conf_thres=0.25, iou_thres=0.45, max_det=1000)

    # Process predictions
    for i, det in enumerate(pred):
        if len(det):
            det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], frame.shape).round()
            annotator = Annotator(frame, line_width=3)
            for *xyxy, conf, cls in reversed(det):
                c = int(cls)
                # Get description from Description class
                description = Description.descriptions.get(c, "unknown")
                label = f"{model.names[c]} - {description}"
                annotator.box_label(xyxy, label, color=colors(c, True))

    return frame

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = process_frame(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('Sign-in.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# if __name__ == '__main__':
#     app.run(debug=True, port=5500)

# @app.route('/')
# def index():
#     return render_template('Search.html')






# recommendations

def get_all_food_items():
    new_df = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts\veggie_list.pkl')
    veg_df = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\veg_list.pkl')
    non_veg_df = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\nonveg_list.pkl')
    return pd.concat([veg_df, non_veg_df])['Name'].tolist()

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    rec_type = request.form.get('type', 'veg')
    try:
        if rec_type == 'veg':
            recommendations = Test.veggie_recommender(user_input)
        elif rec_type == 'veg-to-nonveg':
            recommendations = Test.recommend_non_veg_for_veg_item(user_input)
        else:
            recommendations = Test.recommend_veg_for_non_veg_item(user_input)

        return jsonify({'status': 'success', 'recommendations': [{'name': name} for name in recommendations]})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/food-items', methods=['GET'])
def get_foods():
    try:
        return jsonify({'status': 'success', 'items': get_all_food_items()})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})











#home page search bar

import mysql.connector
from mysql.connector import Error


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="graingain"
    )
    cursor = db.cursor()
    print("Database connected successfully!")
except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")

# @app.route('/')
# def index():
#     return render_template('Home.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    try:
        if query:
            # Using parameterized query to prevent SQL injection
            sql_query = """
                SELECT * FROM all_nutritional_data 
                WHERE Name LIKE %s 
                LIMIT 10
            """
            cursor.execute(sql_query, (f"%{query}%",))
            
            # Get column names
            columns = [desc[0] for desc in cursor.description]
            
            # Fetch results and create list of dictionaries
            results = []
            for row in cursor.fetchall():
                result_dict = dict(zip(columns, row))
                results.append(result_dict)
                
            return jsonify({"success": True, "results": results})
        return jsonify({"success": True, "results": []})
    
    except mysql.connector.Error as err:
        return jsonify({"success": False, "error": str(err)}), 500

@app.route('/api/products', methods=['GET'])
def get_products_by_category():
    try:
        # Get category from query parameters
        category = request.args.get('category', '').strip()
        
        if not category:
            return jsonify({
                'success': False,
                'error': 'Category parameter is required'
            }), 400


        # Define category mappings
        category_mappings = {
            'Vegetables': ['Vegetable', 'Vegetables'],
            'Fruits': ['Fruit', 'Fruits'],
            'Lentils': ['Lentil', 'Lentils', 'Pulse', 'Pulses'],
            'Dairy': ['Dairy', 'Milk Product'],
            'Meat': ['Meat', 'Poultry'],
            'Fish': ['Fish', 'Seafood'],
            'Grains': ['Grain', 'Cereal', 'Bread'],
            'Nuts': ['Nut', 'Nuts'],
            'Seeds': ['Seed', 'Seeds']
        }
        
        # Get the category variations to search for
        category_terms = category_mappings.get(category, [category])
        
        # Create the SQL query with parameter placeholders
        placeholders = ' ,'.join(['%s'] * len(category_terms))
        query = f"""
        SELECT *  
        FROM vegetable_nutrition_data
        """
        

        cursor.execute(query)
        
        # Fetch all matching products
        products = cursor.fetchall()
        
        # Convert any None values to 'N/A'
        product_list = []
        for product in products:
            print(product)

            product_dict = {
                key: 'N/A' if value is None else value 
                for key, value in product.items()
            }
            product_list.append(product_dict)
        


        
        return jsonify({
            'success': True,
            'products': product_list
        })

    except Error as e:
        # Log the MySQL specific error
        print(f"MySQL Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Database error'
        }), 500
        
    except Exception as e:
        # Log the general error
        print(f"Error in get_products_by_category: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5500)