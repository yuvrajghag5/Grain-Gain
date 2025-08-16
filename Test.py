# Write a function that use pickel and predict the output of recomandation system i have already created pikle file and model
# import the required libraries
import pickle
import pandas as pd
import numpy as np
# Load the pickled model and data
# model = pickle.load(open('.pkl','rb'))
# data = pd.read_csv('data.csv')
# # Predict the output
# output = model.predict(data)
# print(output)
def veggie_recommender(user_input):
    
    model = pickle.load(open(r'C:\Users\yuvra\Documents\project\recommender\artifacts\vegsimilarity.pkl','rb'))
    new_df = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts\veggie_list.pkl')
    index = new_df[new_df['Name'] == user_input].index[0]
    distance = sorted(list(enumerate(model[index])), reverse=True , key = lambda x: x[1])
    output=[]
    for i in distance[1:4]:
        output.append(new_df.iloc[i[0]].Name)
    return output





#for veg to non_veg 
    
# def recommend_non_veg_for_veg_item(veg_item_name):
#     veg= pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_nonveg-veg\veg_list.pkl')
#     nonveg= pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_nonveg-veg\nonveg_list.pkl')
#     similarity = pickle.load(open(r'C:\Users\yuvra\Documents\project\recommender\artifacts_nonveg-veg\vegsimilarity.pkl','rb'))
#     similarity_matrix = pickle.load(open(r'C:\Users\yuvra\Documents\project\recommender\artifacts_nonveg-veg\non_vegsimilarity.pkl', 'rb'))
#     index = veg[veg['Name'] == veg_item_name].index[0]
    
    # # Get top 3 recommendations based on similarity
    # recommendations = []
    # for i in range(3):
    #     recommendations.append(nonveg.iloc[similarity_matrix[index].argsort()[::-1][i]]['Name'])
    # output=[]
    # for rec in recommendations:
    #     output.append(rec)
    # return output

def recommend_non_veg_for_veg_item(veg_item_name):
    # Load data
    veg = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\veg_list.pkl')
    nonveg = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\nonveg_list.pkl')
    similarity = pickle.load(open(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\vegsimilarity.pkl', 'rb'))

    # Check if similarity matrix is valid
    if similarity is None or not isinstance(similarity, (np.ndarray, pd.DataFrame)):
        raise ValueError("Error: Similarity matrix is None or invalid!")

    # Ensure veg_item_name exists in dataset
    matching_rows = veg[veg['Name'] == veg_item_name]
    if matching_rows.empty:
        return f"Error: '{veg_item_name}' not found in the dataset."

    index = matching_rows.index[0]
    veg_protein = veg.loc[index, 'Protein (g)']

    # Ensure the index is within bounds of the similarity matrix
    if index >= similarity.shape[0]:
        return f"Error: Index {index} out of range for similarity matrix."

    # Get the top 3 most similar non-vegetarian items
    recommended_indices = np.argsort(similarity[index])[-3:][::-1]
    
    # Check if recommendations are valid
    if len(recommended_indices) == 0:
        return "Error: No recommendations found."

    recommendations = nonveg.iloc[recommended_indices]

    # Prepare recommendation results
    results = []
    for _, item in recommendations.iterrows():
        nonveg_protein = item['Protein (g)']
        quantity_multiplier = veg_protein / nonveg_protein if nonveg_protein > 0 else 1
        quantity_grams = round(100 * quantity_multiplier)  

        results.append(f"{item['Name']} - Recommended quantity: {quantity_grams}g")

    return results



    







# for non veg to veg
def recommend_veg_for_non_veg_item(nonveg_item_name):
    # Load data
    veg = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\veg_list.pkl')
    nonveg = pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\nonveg_list.pkl')
    similarity = pickle.load(open(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\non_vegsimilarity.pkl', 'rb'))

    
    if similarity is None or not isinstance(similarity, (np.ndarray, pd.DataFrame)):
        raise ValueError("Error: Similarity matrix is None or invalid!")

   
    matching_rows = nonveg[nonveg['Name'] == nonveg_item_name]
    if matching_rows.empty:
        return f"Error: '{nonveg_item_name}' not found in the dataset."

    index = matching_rows.index[0]
    nonveg_protein = nonveg.loc[index, 'Protein (g)']

   
    if index >= similarity.shape[0]:
        return f"Error: Index {index} out of range for similarity matrix."

    # Get the top 3 most similar vegetarian items
    recommended_indices = np.argsort(similarity[index])[-3:][::-1]
    
    
    if len(recommended_indices) == 0:
        return "Error: No recommendations found."

    recommendations = veg.iloc[recommended_indices]

    
    results = []
    for _, item in recommendations.iterrows():
        veg_protein = item['Protein (g)']
        quantity_multiplier = nonveg_protein / veg_protein if veg_protein > 0 else 1
        quantity_grams = round(100 * quantity_multiplier)  

        results.append(f"{item['Name']} - Recommended quantity: {quantity_grams}g")

    return results












# def recommend_veg_for_non_veg_item(nonveg_item_name):
    
#     veg= pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\veg_list.pkl')
#     nonveg= pd.read_pickle(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\nonveg_list.pkl')
#     similarity = pickle.load(open(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\non_vegsimilarity.pkl','rb'))
#     similarity_matrix = pickle.load(open(r'C:\Users\yuvra\Documents\project\recommender\artifacts_veg-nonveg\vegsimilarity.pkl', 'rb'))
#     # index = nonveg[nonveg['Name'] == nonveg_item_name].index[0]

#     # # Get top 3 recommendations based on similarity
#     # recommendations = []
#     # for i in range(3):
#     #     recommendations.append(veg.iloc[similarity_matrix[index].argsort()[::-1][i]]['Name'])
#     # output=[]
#     # for rec in recommendations:
#     #     output.append(rec.lower())
#     # return output



#     index = nonveg[nonveg['Name'] == nonveg_item_name].index[0]
#     # index = nonveg_row.index[0]
#     nonveg_protein = index['Protein (g)'].values[0]

#     recommended_indices = similarity[index].argsort()[-3:][::-1]
#     recommendations = veg.iloc[recommended_indices]
    
#     print(f"Vegetarian recommendations for '{nonveg_item_name}':")
#     for i, (_, item) in enumerate(recommendations.iterrows(), 1):
       
#         veg_protein = item['Protein (g)']  # Assuming you have protein data
#         quantity_multiplier = nonveg_protein / veg_protein if veg_protein > 0 else 1
#         quantity_grams = round(100 * quantity_multiplier)  
        
#         print(f"{i}. {item['Name']} - Recommended quantity: {quantity_grams}g")









    

if __name__=="__main__":
    user_input = 'Ostrich'
    print(recommend_veg_for_non_veg_item(user_input))