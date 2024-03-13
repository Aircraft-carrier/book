import sys
import os

# 获取当前文件的目录路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将整个项目文件夹路径添加到 Python 解释器的搜索路径中
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_dir)

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # 跨域请求伪造

db = SQLAlchemy()
cors = CORS()