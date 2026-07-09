from setuptools import setup, find_packages

setup(
    name="weekly-report",       # 别人安装后，你的软件名字
    version="1.0.0",            # 版本号
    packages=find_packages(where="src"), # 告诉它代码在 src 文件夹里
    package_dir={"": "src"},
    install_requires=[          # 自动读取并安装依赖库
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0"
    ],
    entry_points={              # 核心魔法：注册全局命令行指令！
        "console_scripts": [
            "weekly-report=cli:main", 
        ],
    },
)