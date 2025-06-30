import os
import json
import datetime
from pathlib import Path

# 文件类型映射
FILE_TYPES = {
    ".exe": {"name": "Windows应用", "class": "windows"},
    ".dmg": {"name": "Mac应用", "class": "mac"},
    ".deb": {"name": "Debian包", "class": "linux"},
    ".rpm": {"name": "RedHat包", "class": "linux"},
    ".apk": {"name": "Android应用", "class": "android"},
    ".sh": {"name": "Shell脚本", "class": "script"},
    ".py": {"name": "Python脚本", "class": "script"},
    ".jar": {"name": "Java应用", "class": "other"},
    ".zip": {"name": "压缩文件", "class": "archive"},
    ".gz": {"name": "压缩文件", "class": "archive"},
    ".msi": {"name": "Windows安装包", "class": "windows"},
    ".appimage": {"name": "Linux应用", "class": "linux"},
    ".tar": {"name": "压缩文件", "class": "archive"},
    ".7z": {"name": "压缩文件", "class": "archive"},
    ".rar": {"name": "压缩文件", "class": "archive"},
    ".iso": {"name": "光盘映像", "class": "archive"},
}

def convert_size(size):
    """转换文件大小为可读格式"""
    if size < 1024:
        return f"{size} B"
    elif size < 1024**2:
        return f"{size/1024:.1f} KB"
    elif size < 1024**3:
        return f"{size/(1024**2):.1f} MB"
    else:
        return f"{size/(1024**3):.1f} GB"

def get_software_list():
    """获取软件列表并生成JSON数据"""
    soft_dir = Path("soft")
    
    # 确保soft目录存在
    if not soft_dir.exists():
        soft_dir.mkdir(parents=True, exist_ok=True)
        print(f"已创建目录: {soft_dir}")
    
    files = []
    for file in soft_dir.iterdir():
        if file.is_file():
            # 获取文件扩展名
            ext = file.suffix.lower()
            
            # 获取文件类型信息
            file_type = FILE_TYPES.get(ext, {"name": "未知类型", "class": "other"})
            
            # 获取文件大小
            size = file.stat().st_size
            
            # 获取修改时间
            mtime = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            
            files.append({
                "name": file.name,
                "type": file_type["name"],
                "class": file_type["class"],
                "size": convert_size(size),
                "modified": mtime.strftime("%Y-%m-%d %H:%M"),
                "url": f"soft/{file.name}"  # 相对路径
            })
    
    # 按修改时间排序（最新在前）
    files.sort(key=lambda x: x["modified"], reverse=True)
    
    return files

def create_template_html():
    """创建模板HTML文件"""
    template_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>软件资源库</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #3498db;
            --secondary: #2c3e50;
            --light: #ecf0f1;
            --dark: #34495e;
            --success: #2ecc71;
            --warning: #f39c12;
            --danger: #e74c3c;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            background: linear-gradient(135deg, var(--secondary), var(--dark));
            color: white;
            padding: 2rem 0;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 6px 15px rgba(0,0,0,0.2);
            position: relative;
            overflow: hidden;
        }
        
        header::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
            transform: rotate(30deg);
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            position: relative;
            z-index: 2;
        }
        
        .subtitle {
            font-size: 1.1rem;
            opacity: 0.9;
            position: relative;
            z-index: 2;
        }
        
        .stats {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
            min-width: 180px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255,255,255,0.5);
            transition: transform 0.3s ease;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
        }
        
        .stat-card h3 {
            color: var(--primary);
            font-size: 2.2rem;
            margin-bottom: 5px;
        }
        
        .card {
            background: rgba(255, 255, 255, 极客时间
            border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            overflow: hidden;
            margin-bottom: 2rem;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255,255,255,0.5);
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th {
            background: linear-gradient(to right, var(--primary), #2980b9);
            color: white;
            padding: 16px 20px;
            text-align: left;
            font-weight: 600;
        }
        
        th:first-child {
            border-top-left-radius: 10px;
        }
        
        th:last-child {
            border-top-right-radius: 10px;
        }
        
        td {
            padding: 14px 20px;
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }
        
        tr:last-child td {
            border-bottom: none;
极客时间
        tr:hover {
            background-color: rgba(52, 152, 219, 0.05);
        }
        
        .file-type {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            color: white;
        }
        
        .windows { background: var(--primary); }
        .mac { background: var(--danger); }
        .linux { background: var(--warning); }
        .android { background: var(--success); }
        .script { background: #9b59b6; }
        .archive { background: #7f8c8d; }
        .other { background: #95a极客时间 }
        
        .download-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: var(--success);
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .download-btn:hover {
            background: #27ad60;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(46, 204, 113, 0.3);
        }
        
        .search-box {
            margin: 20px auto;
            max-width: 500px;
            position: relative;
        }
        
        .search-box input {
            width: 100%;
            padding: 12px 20px 12px 45px;
            border-radius: 50px;
            border: 1px solid #ddd;
            font-size: 1rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        
        .search-box input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.2);
        }
        
        .search-icon {
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: #7f8c8d;
        }
        
        footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1.5rem;
            color: #7f8c8d;
            font-size: 0.9rem;
        }
        
        .empty-state {
            text-align: center;
            padding: 40px 20px;
            color: #7f8c8d;
        }
        
        .empty-state i {
            font-size: 4rem;
            margin-bottom: 20px;
            color: #bdc3c7;
        }
        
        @media (max-width: 768px) {
            .stat-card {
                min-width: 140px;
                padding: 15px;
            }
            
            th, td {
                padding: 12px 15px;
            }
            
            .hide-mobile {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><i class="fas fa-box-open"></i> 软件资源库</h1>
            <p class="subtitle">所有软件资源均存储在本站服务器</p>
        </header>
        
        <div class="stats">
            <div class="stat-card">
                <h3 id="file-count">0</h3>
                <p>软件总数</p>
            </div>
            <div class="stat-card">
                <h3 id="last-updated">--</h3>
                <p>最后更新</p>
            </div>
        </div>
        
        <div class="search-box">
            <i class="fas fa-search search-icon"></i>
            <input type="text" id="search-input" placeholder="搜索软件名称...">
        </div>
        
        <div class="card">
            <table id="software-table">
                <thead>
                    <tr>
                        <th>软件名称</th>
                        <th>类型</th>
                        <th class="hide-mobile">大小</th>
                        <th class="hide-mobile">修改时间</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- 数据将通过JS填充 -->
                </tbody>
            </table>
            
            <div id="empty-state" class="empty-state" style="display: none;">
                <i class="fas fa-inbox"></i>
                <h3>没有找到软件</h3>
                <p>请检查soft目录是否包含文件或尝试其他搜索词</p>
            </div>
        </div>
        
        <footer>
            <p>© 2023 软件资源库 | 自动生成于 <span id="gen-time"></span></p>
        </footer>
    </div>

    <!-- 嵌入式数据占位符 -->
    <!-- EMBEDDED_DATA_PLACEHOLDER -->
    
    <script>
        // 使用嵌入式数据
        function loadEmbeddedData() {
            try {
                if (typeof embeddedSoftwareData === 'undefined') {
                    throw new Error("未找到嵌入式数据");
                }
                
                const data = embeddedSoftwareData;
                console.log('加载嵌入式数据成功');
                
                // 更新统计信息
                document.getElementById('file-count').textContent = data.file_count;
                document.getElementById('last-updated').textContent = data.last_updated;
                document.getElementById('gen-time').textContent = new Date().toLocaleString();
                
                // 填充表格
                renderTable(data.files);
                setupSearch(data.files);
                
            } catch (error) {
                console.error('加载嵌入式数据失败:', error);
                showErrorState(error);
            }
        }
        
        function renderTable(files) {
            const tbody = document.querySelector('#software-table tbody');
            tbody.innerHTML = '';
            
            if (!files || files.length === 0) {
                document.getElementById('empty-state').style.display = 'block';
                document.getElementById('empty-state').innerHTML = `
                    <i class="fas fa-exclamation-circle"></i>
                    <h3>软件库为空</h极客时间
                    <p>请将软件文件放入soft目录并运行generate.py</p>
                `;
                return;
            }
            
            document.getElementById('empty-state').style.display = 'none';
            
            files.forEach(file => {
                const row = document.createElement('tr');
                
                row.innerHTML = `
                    <td>${file.name}</td>
                    <td><span class="file-type ${file.class}">${file.type}</span></td>
                    <td class="hide-mobile">${file.size}</td>
                    <td class="hide-mobile">${file.modified}</td>
                    <td><a href="${file.url}" class="download-btn"><i class="fas fa-download"></i> 下载</a></td>
                `;
                
                tbody.appendChild(row);
            });
        }
        
        function setupSearch(files) {
            const searchInput = document.getElementById('search-input');
            
            searchInput.addEventListener('input', () => {
                const searchTerm = searchInput.value.toLowerCase().trim();
                
                if (searchTerm === '') {
                    renderTable(files);
                    return;
                }
                
                const filtered = files.filter(file => 
                    file.name.toLowerCase().includes(searchTerm)
                );
                
                renderTable(filtered);
            });
        }
        
        function showErrorState(error) {
            const emptyState = document.getElementById('empty-state');
            emptyState.style.display = 'block';
            emptyState.innerHTML = `
                <i class="fas fa-exclamation-triangle"></i>
                <h3>数据加载失败</h3>
                <p>错误信息: ${error.message}</p>
                <p>请检查以下可能原因:</p>
                <ul style="text-align: left; margin: 15px auto; max-width: 500px;">
                    <li>确保已运行generate.py生成HTML文件</li>
                    <li>检查文件路径是否正确</li>
                    <li>查看浏览器控制台获取详细错误信息</li>
                </ul>
            `;
        }

        // 页面加载时获取嵌入式数据
        document.addEventListener('DOMContentLoaded', loadEmbeddedData);
    </script>
</body>
</html>
"""
    
    with open("template.html", "w", encoding="utf-8") as f:
        f.write(template_content)
    print("已创建模板文件: template.html")

def generate_html_with_embedded_data():
    """生成包含嵌入式JSON数据的HTML文件"""
    # 确保模板文件存在
    if not Path("template.html").exists():
        print("未找到模板文件，正在创建...")
        create_template_html()
    
    software_list = get_software_list()
    
    data = {
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "file_count": len(software_list),
        "files": software_list
    }
    
    # 读取HTML模板
    with open("template.html", "r", encoding="utf-8") as f:
        html_template = f.read()
    
    # 将数据嵌入HTML
    embedded_html = html_template.replace(
        "<!-- EMBEDDED_DATA_PLACEHOLDER -->",
        f"<script>const embeddedSoftwareData = {json.dumps(data, ensure_ascii=False)};</script>"
    )
    
    # 写入最终的HTML文件
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(embedded_html)
    
    print(f"成功生成HTML文件: {len(software_list)}个软件已嵌入")
    print(f"HTML文件路径: {Path('index.html').resolve()}")

if __name__ == "__main__":
    print("开始生成软件索引...")
    generate_html_with_embedded_data()
    print("完成! 请打开 index.html 查看结果")
