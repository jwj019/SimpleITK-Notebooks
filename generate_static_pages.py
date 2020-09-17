from notebooktoall.transform import transform_notebook
import os

files = []
ipynb_dir = os.path.abspath('./Python')
html_dir = os.path.abspath('./Python_html')

for path in os.listdir(ipynb_dir):
    full_path = os.path.join(ipynb_dir, path)
    if os.path.isfile(full_path):
        files.append(full_path)

notebooks = [i for i in files if i.endswith('.ipynb')]

if not os.path.exists(html_dir):
    os.makedirs(html_dir)

os.chdir(html_dir)
for notebook in notebooks: 
    transform_notebook(ipynb_file=notebook, export_list=["html"])