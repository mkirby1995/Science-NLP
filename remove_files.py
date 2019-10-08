import os

def remove_files(filetype, path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if filetype in file:
                os.remove(os.path.join(r, file))


remove_files('.txt', 'txt_files/')
remove_files('.json', './')
#remove_files('.pdf', 'pdf_files/')
