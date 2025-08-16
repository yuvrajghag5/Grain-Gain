# from flask import Flask, render_template, request
# import mysql.connector

# app = Flask(__name__)

# # Connect to MySQL
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="graingain"
# )
# cursor = db.cursor()

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     search_query = ''
#     results = []

#     if request.method == 'POST':
#         search_query = request.form.get('search')
#         query = "SELECT * FROM vegetable_nutrition_data WHERE Name LIKE %s LIMIT 10"
#         cursor.execute(query, (f"%{search_query}%", f"%{search_query}%"))
#         results = cursor.fetchall()

#     return render_template('index.html', results=results, query=search_query)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import mysql.connector
from flask_cors import CORS  # Add this for handling CORS if needed

app = Flask(__name__)
CORS(app)  # Enable CORS

# Connect to MySQL
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

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    try:
        if query:
            # Using parameterized query to prevent SQL injection
            sql_query = """
                SELECT * FROM vegetable_nutrition_data 
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

if __name__ == '__main__':
    app.run(debug=True)










