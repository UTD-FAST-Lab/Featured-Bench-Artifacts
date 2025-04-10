import os
import configparser
import json
import argparse


def generate_template(length, conditions):
    template = """    if (size < {LENGTH}) {{
        printf("File is too small...");
        return;
    }}\n""".format(LENGTH=length)
    
    for i, condition in enumerate(conditions):
        indent = "    " * (i + 1)
        MAGIC = condition.get('value')
        template += f"""{indent}if ({MAGIC}) {{\n"""
    
    template += "{indent}printf(\"Found magic symbol!\");\n{indent}int *ptr = NULL;\n{indent}*ptr = 10;\n".format(indent="    " * (len(conditions) + 1))
    for i in range(len(conditions)-1):
        indent = "    " * (len(conditions)-i)
        template += f"""{indent}}}\n"""
    template += """    } else {
        printf("Not magic symbol, continue...");
    }\n"""

    return template


def generate_c_program(settings):
    length = settings[0]
    conditions = settings[2]

    code = generate_template(length, conditions)
    
    return code

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate C program")
    parser.add_argument("group", help="Group name")
    parser.add_argument("--out", help="Output location")

    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    
    if args.group == 'checksumd':
        config.read('config/config_checksumd.ini')
    elif args.group == 'checksumc':
        config.read('config/config_checksumc.ini')
    
    settings_list = []
    
    for section in config.sections():
        length = int(config.get(section, 'length'))
        count = int(config.get(section, 'count'))
        conditions = config.get(section, 'conditions')
        
        settings_list.append((length, count, json.loads(conditions)))
    
    if not os.path.exists(args.out):
        os.makedirs(args.out)
    
    for settings in settings_list:
        generated_code = generate_c_program(settings)
        with open(f'{args.out}/CHECKSUM_C{settings[1]}_D{len(settings[2])}.c', 'w+') as f:
            f.write(generated_code)
            print(f'Genrated program CHECKSUM_C{settings[1]}_D{len(settings[2])}.c...')
        
