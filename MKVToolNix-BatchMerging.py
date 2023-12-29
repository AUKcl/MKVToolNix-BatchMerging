#    MKVToolNix-BatchMerging
#    Automate Rapid Batch Concatenation of TV Shows or TV Animations using mkvtoolnix, supporting Windows, macOS, Linux.
#    Copyright (C) <2023>  <AUKcl>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    
#    AUKcl's email:kaixuan135@outloook.com

import subprocess
import os

def generate_and_replace_lines(base_line, target_string, num_lines):
    lines = []

    # 将第一行内容添加到列表中
    lines.append(base_line)

    # 生成并添加替换后的行内容
    for i in range(2, num_lines + 1):
        replaced_line = base_line.replace(target_string, f"{target_string[:-2]}{i:02d}")
        lines.append(replaced_line)

    # 获取脚本所在目录并创建跨平台的文件路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(script_dir, "output.txt")

    # 将所有行内容写入文件
    with open(output_file_path, "w", newline='', encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")

# 提示用户输入第一行命令和需替换的目标字符
base_line = input("请输入第一行命令：")
target_string = input("请输入需替换的目标字符：")

# 询问用户要封装的集数
num_lines = int(input("请输入要封装的集数："))

# 调用函数生成并替换行内容
generate_and_replace_lines(base_line, target_string, num_lines)

# 逐行读取output.txt文件内容，并作为命令执行
with open("output.txt", "r", encoding='utf-8') as f:
    for line in f:
        command = line.strip()  # 移除行末尾的换行符
        subprocess.run(command, shell=True)