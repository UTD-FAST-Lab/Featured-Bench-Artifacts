import os
import configparser
import json


def generate_str_template(length, conditions):
    template = """    if (size < {LENGTH}) {{
        printf("File is too small...");
        return;
    }}\n""".format(LENGTH=length)
    
    for i, condition in enumerate(conditions):
        indent = "    " * (i + 1)
        START = condition.get('start')
        LENGTH = condition.get('len')
        MAGIC = condition.get('value')
        template += f"""{indent}if (strncmp((char *)(data + {START}), "{MAGIC}", {LENGTH}) == 0) {{\n"""
    
    template += "{indent}printf(\"Found magic symbol!\");\n{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent="    " * (len(conditions) + 1))
    for i in range(len(conditions)-1):
        indent = "    " * (len(conditions)-i)
        template += f"""{indent}}}\n"""
    template += """    } else {
        printf("Not magic symbol, continue...");
    }\n"""
    
    return template
    
def generate_char_template(length, conditions):
    template = """    if (size < {LENGTH}) {{
        printf("File is too small...");
        return;
    }}\n""".format(LENGTH=length)
    
    for i, condition in enumerate(conditions):
        indent = "    " * (i + 1)
        START = condition.get('start')
        MAGIC = condition.get('value')
        template += f"""{indent}if ((data[{START}]) == '{MAGIC}') {{\n"""
    
    template += "{indent}printf(\"Found magic symbol!\");\n{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent="    " * (len(conditions) + 1))
    for i in range(len(conditions)-1):
        indent = "    " * (len(conditions)-i)
        template += f"""{indent}}}\n"""
    template += """    } else {
        printf("Not magic symbol, continue...");
    }\n"""

    return template

def generate_num_template(length, conditions):
    template = """    if (size < {LENGTH}) {{
        printf("File is too small...");
        return;
    }}\n""".format(LENGTH=length)
    
    for i, condition in enumerate(conditions):
        START = condition.get('start')
        LENGTH = condition.get('len')
        template += f"    unsigned int target_bytes_{i} = 0;\n"
        template += f"    for (long i = 0; i < {LENGTH}; ++i) {{\n"
        template += f"        target_bytes_{i} |= data[{START}+i] << (8*({LENGTH}-i-1));\n    }}\n"
    
    for i, condition in enumerate(conditions):
        indent = "    " * (i + 1)
        MAGIC = condition.get('value')
        template += f"""{indent}if (target_bytes_{i} == {MAGIC}) {{\n"""
    
    template += "{indent}printf(\"Found magic symbol!\");\n{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent="    " * (len(conditions) + 1))
    for i in range(len(conditions)-1):
        indent = "    " * (len(conditions)-i)
        template += f"""{indent}}}\n"""
    template += """    } else {
        printf("Not magic symbol, continue...");
    }\n"""

    return template

def generate_c_program(settings):
    ttype = settings[0]
    length = settings[1]
    conditions = settings[2]
    
    code = """"""
    
    if ttype == 'num':
        code = generate_num_template(length, conditions)
    elif ttype == 'char':
        code = generate_char_template(length, conditions)
    elif ttype == 'str':
        code = generate_str_template(length, conditions)
    
    return code

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config_magicd.ini')
    # # Unblock the following line to generate programs for MAGICL
    # config.read('config/config_magicl.ini')
    # # Unblock the following line to generate programs for MAGICS
    # config.read('config/config_magics.ini')
    
    settings_list = []
    
    for section in config.sections():
        ttype = config.get(section, 'type')
        length = int(config.get(section, 'length'))
        conditions = config.get(section, 'conditions')
        
        settings_list.append((ttype, length, json.loads(conditions)))
    
    if not os.path.exists('program'):
        os.makedirs('program')
    
    for settings in settings_list:
        generated_code = generate_c_program(settings)
        condition = settings[2]
        print(f'condition: {condition[0].get("start")}')
        with open(f'program/MAGIC_S{condition[0].get("start")}_L{len(condition[0].get("value"))}_D{len(settings[2])}.c', 'w+') as f:
            f.write(generated_code)
            print(f'Genrated program MAGIC_S{condition[0].get("start")}_L{len(condition[0].get("value"))}_D{len(settings[2])}.c...')
        
