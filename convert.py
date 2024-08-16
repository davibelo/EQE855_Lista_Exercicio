import pypandoc
import re

def convert_tex_to_md(input_file, output_file):
    # Convert .tex to .md using pypandoc with no wrapping
    output = pypandoc.convert_file(input_file, 'md', format='latex', extra_args=['--wrap=none'])
    
    # Remove unnecessary escape characters
    output = re.sub(r'\\([#*.])', r'\1', output)
    output = re.sub(r'\\\$', r'$', output)
    
    # Remove consecutive blank lines
    output = re.sub(r'\n\s*\n', '\n', output)
    
    # Write the output to the .md file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Converted {input_file} to {output_file}")

if __name__ == '__main__':
    input_file = 'temp.tex'  # Specify your input .tex file here
    output_file = 'temp.md'  # Specify your output .md file here
    convert_tex_to_md(input_file, output_file)
