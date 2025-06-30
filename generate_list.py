import os
import json
from os.path import getsize, join

def generate_software_list(folder_path):
    software_data = []
    
    for filename in os.listdir(folder_path):
        filepath = join(folder_path, filename)
        if os.path.isfile(filepath) and not filename.startswith('.'):
            # 获取文件大小
            size_bytes = getsize(filepath)
            size_str = f"{round(size_bytes/1024/1024, 1)}MB" if size_bytes >= 1024*1024 else f"{round(size_bytes/1024, 1)}KB"
            
            # 确定文件类型
            ext = filename.split('.')[-1].lower()
            file_type = {
                'exe': 'Windows程序',
                'msi': 'Windows安装包',
                'dmg': 'MacOS应用',
                'pkg': 'MacOS安装包',
                'zip': '压缩文件',
                'rar': '压缩文件',
                '7z': '压缩文件',
                'apk': 'Android应用',
                'ipa': 'iOS应用'
            }.get(ext, '文件')
            
            software_data.append({
                "name": filename,
                "type": file_type,
                "size": size_str
            })
    
    # 保存为JSON文件
    with open('software-list.json', 'w', encoding='utf-8') as f:
        json.dump({"software": software_data}, f, ensure_ascii=False, indent=2)
    
    print("software-list.json 已生成！")

# 使用示例
generate_software_list('./soft')