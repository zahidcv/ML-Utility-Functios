import os
import cv2
import shutil
# Specify the input and output directories
input_dir = r'C:\Users\HP\Downloads\dummy bornomala'
output_dir = r'C:\Users\HP\Downloads\dummy bornomala output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
for folder_name in os.listdir(input_dir):
#     print()
    print(folder_name)
#     print()
    
    path_to_folder = os.path.join(input_dir, folder_name)
    output_image_folder = os.path.join(output_dir, folder_name)
    if os.path.isdir(output_image_folder):
        shutil.rmtree(output_image_folder)
        
    os.makedirs(output_image_folder)
    
    for img_name in os.listdir(path_to_folder):
#         print(img_name)
        
        path_to_image = os.path.join(path_to_folder, img_name)
#         print(path_to_image)
        print('imread')
        image = cv2.imread(path_to_image)
        
        print('resize')
        res_image = cv2.resize(image, (224, 224))
        
       
        
        
        
        
            
        output_image_path = os.path.join(output_image_folder,  img_name)
        print(output_image_path)
        cv2.imwrite(output_image_path, res_image)
        
        
        
