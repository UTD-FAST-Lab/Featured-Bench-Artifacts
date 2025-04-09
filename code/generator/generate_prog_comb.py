import math
import os
import configparser


def generate_full(i, width, depth, interval, bbranch):
    global branch_count
    code = ""
    magic_num = int((interval[1] - interval[0]) / width) + interval[0]
    for j in range(width):
        if j == 0:
            
            code += "{indent}if (hash < {magic_num}) {{\n".format(indent=" " * (i+1) * 4, magic_num=magic_num)

            if i == depth - 1:
                branch_count = branch_count + 1
                code += "{indent}printf(\"this is branch {branch}\\n\");\n".format(indent=" " * (i+2) * 4, branch=branch_count)
                if (branch_count) == bbranch:
                    code += "{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent=" " * (i+2) * 4)
            else:
                code += generate_full(i+1, width, depth, (interval[0], magic_num), bbranch)
            code += "{indent}}} else if (hash < {magic_num}) {{\n".format(indent=" " * (i+1) * 4, magic_num=magic_num+(width**(depth-i-1))*(j+1))
        elif j == width - 1:
            if i == depth - 1:
                branch_count = branch_count + 1
                code += "{indent}printf(\"this is branch {branch}\\n\");\n".format(indent=" " * (i+2) * 4, branch=branch_count)
                if (branch_count) == bbranch:
                    code += "{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent=" " * (i+2) * 4)
            else:
                code += generate_full(i+1, width, depth, (magic_num+(width**(depth-i-1))*(j-1), interval[1]), bbranch)
            code += "{indent}}}\n".format(indent=" " * (i+1) * 4)
        else:
            if i == depth - 1:
                branch_count = branch_count + 1
                code += "{indent}printf(\"this is branch {branch}\\n\");\n".format(indent=" " * (i+2) * 4, branch=branch_count)
                if (branch_count) == bbranch:
                    code += "{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent=" " * (i+2) * 4)
            else:
                code += generate_full(i+1, width, depth, (magic_num+(width**(depth-i-1))*(j-1), magic_num+(width**(depth-i-1))*j), bbranch)
            code += "{indent}}} else if (hash < {magic_num}) {{\n".format(indent=" " * (i+1) * 4, magic_num=magic_num+(width**(depth-i-1))*(j+1))

    return code

def generate_c_program(settings):
    width = settings[0]
    depth = settings[1]
    bbranch = settings[2]
    
    code = generate_full(0, width, depth, (0, width**depth), bbranch)

    return code

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config_comb.ini')
    
    settings_list = []
    
    for section in config.sections():
        width = int(config.get(section, 'width'))
        depth = int(config.get(section, 'depth'))
        bbranch = int(config.get(section, 'bbranch'))

        settings_list.append((width, depth, bbranch))
    
    if not os.path.exists('program'):
        os.makedirs('program')
    
    for settings in settings_list:
        branch_count = 0
        generated_code = generate_c_program(settings)
        with open(f'program/COMP_W{settings[0]}_D{settings[1]}_B{settings[2]}.c', 'w+') as f:
            f.write(generated_code)
            print(f'Generated program COMP_W{settings[0]}_D{settings[1]}_B{settings[2]}.c...')
