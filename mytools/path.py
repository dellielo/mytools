import os 
import shutil 

def mkdir_and_remove(output_dir): 
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=False)

def get_files_in_folder_according_ext(path, ext_to_compare):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            basename = os.path.basename(file)
            _, ext = os.path.splitext(basename)
            # ext = FileHelper.getFileExtenstion(file)
            if(ext.lower() in ext_to_compare):
                yield os.path.join(path, file), file,  ext

def get_files_in_folder_endswith(path, end_to_compare):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            basename = os.path.basename(file)
            _, ext = os.path.splitext(basename)
            if file.endswith(end_to_compare):
                yield os.path.join(path, file), file,  ext

def get_just_filename(pathname):
    basename = os.path.basename(pathname)
    filename, _ = os.path.splitext(basename)
    return filename

