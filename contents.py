import os
import shutil

def getContents(folder_path):
    files = os.listdir(folder_path)
    
    images = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]
    texts = [f for f in files if f.endswith('.txt')]
    
    file_sets = []
    
    for image in images:
        base_name = os.path.splitext(image)[0]
        text_file = f"{base_name}.txt"
        
        if text_file in texts:
            image_path = os.path.join(folder_path, image)
            text_path = os.path.join(folder_path, text_file)
            
            image_mtime = os.path.getmtime(image_path)
            text_mtime = os.path.getmtime(text_path)
            
            set_mtime = min(image_mtime, text_mtime)
            
            file_sets.append((image_path, text_path, set_mtime))
    
    if not file_sets:
        return None, None  

    oldest_set = sorted(file_sets, key=lambda x: x[2])[0]
    
    return oldest_set[0], oldest_set[1]


def moveContents(file_path):
    base_path = os.path.dirname(__file__)
    target_directory = os.path.join(base_path, 'contents', 'posted')

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    shutil.move(file_path, target_directory)
