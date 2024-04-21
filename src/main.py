from os import (path, listdir, mkdir)
from shutil import (copy, rmtree)
from generate_page import generate_page

def main():
    public_dir = './public'
    static_dir = './static'
    
    if path.exists(public_dir):
        rmtree(public_dir)
        mkdir(public_dir)
        
        files = listdir(static_dir)

        for file in files:
            if file.endswith('.png') or file.endswith('.jpeg'):
                mkdir(public_dir + '/images')
                copy(path.join(static_dir, file), public_dir + '/images')
            else:
                copy(path.join(static_dir, file),(public_dir))

    else:
        mkdir(public_dir)
        files = listdir(static_dir)

        for file in files:
            if file.endswith('.png') or file.endswith('.jpeg'):
                mkdir(public_dir + '/images')
                copy(path.join(static_dir, file), public_dir + '/images')
            else:    
                copy(path.join(static_dir, file),(public_dir))
        
    generate_page('./content', './template.html', public_dir)
        
main()