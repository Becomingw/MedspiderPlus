@echo off
setlocal

:: 获取当前批处理脚本所在的目录
set "current_dir=%~dp0"

:: 设置Miniconda Python解释器的路径
set "python_exe=%current_dir%python.exe"

:: 设置要运行的Python脚本路径
set "python_script=%current_dir%main.py"

:: 启动Python脚本
"%python_exe%" "%python_script%"

endlocal
