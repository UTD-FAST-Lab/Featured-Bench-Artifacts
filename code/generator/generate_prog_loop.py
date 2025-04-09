import os
import configparser


def generate_template(iteration):
    template = """    for (unsigned int i = 0; i < size; i++) {{
        if (i == {UPPER}) {{
            printf(\"this is iteration %d\\n", i);
            int *p = NULL;
            *p = 10;\n""".format(UPPER=iteration)
    template += """        } else {
            printf(\"this is iteration %d\\n", i);
        }\n    }"""
    
    return template
    
def generate_c_program(settings):
    print(settings)
    code = """"""
    code = generate_template(settings[0])
    
    return code

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config_loopi.ini')
    
    settings_list = []
    
    for section in config.sections():
        iteration = int(config.get(section, 'iteration'))
        
        settings_list.append((iteration, 'i'))
    
    if not os.path.exists('program'):
        os.makedirs('program')
    
    for settings in settings_list:
        generated_code = generate_c_program(settings)
        with open(f'program/LOOP_I{settings[0]}.c', 'w+') as f:
            f.write(generated_code)
            print(f'Generated program LOOP_I{settings[0]}.c...')
        
