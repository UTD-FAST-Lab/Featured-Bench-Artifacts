import os
import configparser
import argparse

def generate_template_data(iteration):
    template = """    for (unsigned int i = 0; i < size; i++) {{
        printf(\"this is iteration %d\\n", i);
        if (data[i] == 'a') {{
            if (i == {UPPER}) {{
                printf("Crash!\\n");
                int *p = NULL;
                *p = 10;
            }}\n""".format(UPPER=iteration)
    template += """        } else {
            break;
        }\n    }"""
    
    return template
    
def generate_c_program(settings):
    print(settings)
    code = """"""
    code = generate_template_data(settings[0])
    
    return code

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate C program")
    parser.add_argument("--out", help="Output location")

    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    config.read('config/config_loopdi.ini')
    
    settings_list = []
    
    for section in config.sections():
        iteration = int(config.get(section, 'iteration'))
        
        settings_list.append((iteration, 'i'))
    
    if not os.path.exists(args.out):
        os.makedirs(args.out)
    
    for settings in settings_list:
        generated_code = generate_c_program(settings)
        with open(f'{args.out}/LOOPD_I{settings[0]}.c', 'w+') as f:
            f.write(generated_code)
            print(f'Generated program LOOP_I{settings[0]}.c...')
        
