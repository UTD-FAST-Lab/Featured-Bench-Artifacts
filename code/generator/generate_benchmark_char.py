import os

def replace_program_in_c_file(program):
    FUNC_path = 'template_char/FUNC.c'
    if os.path.exists(FUNC_path):
        with open(FUNC_path, 'r') as FUNC_file:
            FUNC_content = FUNC_file.read()
    FUNC_path = 'template_char/FUNC.c'
    if os.path.exists(FUNC_path):
        with open(f'program/{program}', 'r') as program_file:
            program_content = program_file.read()

    func_name = os.path.splitext(program)[0]
    updated_FUNC_content = FUNC_content

    if 'RECUR' in func_name:
        updated_FUNC_content = updated_FUNC_content.replace('FUNC(data, size)', 'FUNC(data, size, 0)')
        updated_FUNC_content = updated_FUNC_content.replace('FUNC(unsigned char *data, long size)', 'FUNC(unsigned char *data, long size, int i)')
        
    updated_FUNC_content = updated_FUNC_content.replace('// INSERT PROGRAM HERE', program_content)
    updated_FUNC_content = updated_FUNC_content.replace('FUNC', func_name)
    
    output_dir = os.path.join('benchmark', func_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, program)  
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(updated_FUNC_content)

    makefile_path = 'template_char/Makefile'
    if os.path.exists(makefile_path):
        with open(makefile_path, 'r') as makefile:
            makefile_content = makefile.read()
        updated_makefile_content = makefile_content.replace('FUNC', func_name)
        with open(os.path.join(output_dir, 'Makefile'), 'w') as makefile:
            makefile.write(updated_makefile_content)
            
    
if __name__ == '__main__':   
    for filename in os.listdir('program'):
        if filename.endswith('.c'):
            replace_program_in_c_file(filename)
            print(f'Genrated benchmark {filename}...')
