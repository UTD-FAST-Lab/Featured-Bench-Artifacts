import os
import configparser


def generate_template(iteration):
    template = """    if (i >= size) {{
        printf("File is too small...\\n");
        return;
    }}
    printf("This is iteration %d\\n", i);
    
    if (i == {CRASH}) {{
        printf("Crash!\\n");
        int *p = NULL;
        *p = 10;
    }}
        RECUR_I{CRASH}(data, size, i + 1);
    """.format(CRASH=iteration)
    
    return template

def generate_c_program(settings):
    print(settings)
    code = """"""
    code = generate_template(settings[0])
    
    return code

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config_recuri.ini')
    
    settings_list = []
    
    for section in config.sections():
        iteration = int(config.get(section, 'iteration'))
        
        settings_list.append((iteration, 'i'))
    
    if not os.path.exists('program'):
        os.makedirs('program')
    
    for settings in settings_list:
        generated_code = generate_c_program(settings)
        with open(f'program/RECUR_I{settings[0]}.c', 'w+') as f:
            f.write(generated_code)
            print(f'Generated program RECUR_I{settings[0]}.c...')
        
