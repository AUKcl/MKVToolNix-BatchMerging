# MKVToolNix-BatchMerging

## 描述
使用mkvtoolnix自动化快速批量合成电视剧或TV动画，暂只支持Windows

## 依赖
- [MKVToolNix](https://mkvtoolnix.download/downloads.html)
- [Python](https://www.python.org/downloads/)

## 前置准备
将需要批量合成的视频、音频及字幕文件按照下列格式重命名

**例子 (电视剧):**

<pre>
  <code>
TV
├── A_title
│   ├── Season 1
│   │   ├── A S01E01.mp4
│   │   ├── A S01E01.flac
│   │   ├── A S01E01.ass
│   │   ├── A S01E02.mp4
│   │   ├── A S01E02.flac
│   │   ├── A S01E02.ass
│   │   ├── A S01E03.mp4
│   │   ├── A S01E03.flac
│   │   ├── A S01E03.ass
│   │   └── A S01E04.mp4
│   │   ├── A S01E04.flac
│   │   ├── A S01E04.ass
│   └── Season 2
│   │   ├── A S02E01.mp4
│   │   ├── A S02E01.flac
│   │   ├── A S02E01.ass
│   │   ├── A S02E02.mp4
│   │   ├── A S02E02.flac
│   │   ├── A S02E02.ass
│   │   ├── A S02E03.mp4
│   │   ├── A S02E03.flac
│   │   ├── A S02E03.ass
│   │   └── A S02E04.mp4
│   │   ├── A S02E04.flac
│   │   ├── A S02E04.ass
├── B_title
│   └─── Season 1
  </code>
</pre>

## 使用方法
1. 打开`mkvtoolnix-gui.exe`
2. 添加第一集视频、音频、字幕，并按需设置好（这将作为后续文件的设置模版）
3. 前往`菜单栏>混流>显示命令行>复制到剪贴板`
4. 打开CMD
5. 切换到脚本目录,例如：
    ```
    cd C:\MKVToolNix-BatchMerging
    ```
6. 运行python脚本
   ```
   python MKVToolNix-BatchMerging.py
   ```
7. 脚本询问初始命令，此时粘贴第三步获取到命令
8. 脚本询问后续命令需替换初始命令中的哪部分，如：`S01E01`，后续将按升序替换集字符
9. 脚本询问当前季共需合成多少集，根据具体情况填写，如：第一季共13集，填写`13`，若只有前10集，则填写`10`，不可出现跳集
10. 脚本开始运行，此时脚本目录会生成`output.txt`
11. 脚本根据`output.txt`内容自动执行命令，完成封装

## 许可证
GPLv3 © [AUKcl](https://github.com/AUKcl/MKVToolNix-BatchMerging/blob/main/LICENSE.md)
