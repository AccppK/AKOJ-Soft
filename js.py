import os
import json
from datetime import datetime
from os.path import getsize, join, getmtime

def generate_software_list(folder_path):
    software_data = []
    
    for filename in os.listdir(folder_path):
        filepath = join(folder_path, filename)
        if os.path.isfile(filepath) and not filename.startswith('.'):
            # 获取文件信息
            size_mb = getsize(filepath) / (1024 * 1024)
            mtime = datetime.fromtimestamp(getmtime(filepath)).strftime('%Y-%m-%d')
            
            # 智能识别文件类型
            ext = filename.split('.')[-1].lower()
            file_type, description = {
                'exe': ('Windows程序', '可执行应用程序'),
                'msi': ('Windows安装包', 'Microsoft安装程序'),
                'dmg': ('MacOS镜像', '磁盘映像文件'),
                'zip': ('压缩文件', 'ZIP格式压缩包'),
                # 可继续添加其他扩展名...
            }.get(ext, (ext.upper() + '文件', ''))
            
            software_data.append({
                "name": filename,
                "type": file_type,
                "size": f"{size_mb:.1f}MB" if size_mb >= 1 else f"{int(size_mb*1024)}KB",
                "description": description,
                "version": "1.0.0",  # 自动生成或从文件名提取
                "update": mtime
            })
    
    # 保存为JSON文件
    with open('software-list.json', 'w', encoding='utf-8') as f:
        json.dump({"software": software_data}, f, ensure_ascii=False, indent=2)
    
    print(f"生成成功！共处理 {len(software_data)} 个文件")

# 使用示例
generate_software_list('./soft')