#!/usr/bin/env python3
import re
import os

def translate_file(src_path, dst_path, title_fr, translations):
    with open(src_path, 'r') as f:
        content = f.read()
    
    content = re.sub(r'<title>.*?</title>', f'<title>{title_fr}</title>', content)
    
    for orig, trans in translations:
        content = content.replace(orig, trans)
    
    credit = '[ Traduction par Tedsig42 ]\n'
    if '</pre></div></body>' in content:
        content = content.replace('</pre></div></body>', credit + '</pre></div></body>')
    elif '</pre></div>' in content:
        content = content.replace('</pre></div>', credit + '</pre></div>')
    
    with open(dst_path, 'w') as f:
        f.write(content)
    
    print(f"Translated: {os.path.basename(src_path)}")

# ... (translations from volumes 4 and 5)
