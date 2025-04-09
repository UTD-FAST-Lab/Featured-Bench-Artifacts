import os
import configparser

def generate_full(i, base, index, interval, bbranch):
    global branch_count
    code = ""
    magic_num = int(interval[0] + (interval[1] - interval[0]) / base)

    code += "{indent}if (hash < {magic_num}) {{\n".format(indent=" " * (i+1) * 4, magic_num=magic_num)
    if i == index - 1:
        branch_count = branch_count + 1
        code += "{indent}printf(\"this is branch {branch}\\n\");\n".format(indent=" " * (i+2) * 4, branch=branch_count)
        if (branch_count) == bbranch:
            code += "{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent=" " * (i+2) * 4)
    else:
        code += generate_full(i+1, base, index, (interval[0], magic_num), bbranch)
    code += "{indent}}} else {{\n".format(indent=" " * (i+1) * 4)
    if i == index - 1:
        branch_count = branch_count + 1
        code += "{indent}printf(\"this is branch {branch}\\n\");\n".format(indent=" " * (i+2) * 4, branch=branch_count)
        if (branch_count) == bbranch:
            code += "{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent=" " * (i+2) * 4)
    else:
        code += generate_full(i+1, base, index, (magic_num, interval[1]), bbranch)
    code += "{indent}}}\n".format(indent=" " * (i+1) * 4)
    return code

def generate_c_program(settings):
    base = settings[0]
    index = settings[1]
    bbranch = settings[2]
    code = generate_full(0, base, index, (0, base**index), bbranch)
    return code

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config_comwe.ini')
    
    settings_list = []
    
    for section in config.sections():
        base = int(config.get(section, 'base'))
        index = int(config.get(section, 'index'))
        bbranch = int(config.get(section, 'bbranch'))

        settings_list.append((base, index, bbranch))
    
    if not os.path.exists('program'):
        os.makedirs('program')
    
    for settings in settings_list:
        branch_count = 0
        generated_code = generate_c_program(settings)
        with open(f'program/COMP_W2_D{settings[1]}_ω{settings[0]}_B{settings[2]}.c', 'w+') as f:
            f.write(generated_code)
            print(f'Genrated program COMP_W2_D{settings[1]}_ω{settings[0]}_B{settings[2]}.c...')