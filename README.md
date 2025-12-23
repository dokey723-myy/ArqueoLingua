# ArqueoLingua: 考古学西语解码器 🏛️📜

> "不要把西班牙语当语言学，把它当**密码**来破译。"

**ArqueoLingua** 是一个专为考古学研究者设计的极简 Python 工具，旨在帮助零西语基础的学者快速阅读关于 **Caral (卡拉尔)**、**Maya (玛雅)** 和 **Olmec (奥尔梅克)** 的学术文本。

## 🎯 核心理念 (The Logic)

这个工具不教你“你好，再见”，而是基于**李新伟/张光直的文明比较视角**，通过三层逻辑过滤，直接提取文献中的核心信息：

1.  **Layer 1: 同源词扫描 (Cognate Scanner)** 🟢
    *   自动识别拉丁词根（如 `-ción` -> `-tion`），利用英语学术背景直接猜词。
2.  **Layer 2: 考古雷达 (Archaeo Radar)** 🔴
    *   内置高频考古术语库（如 `pirámide`, `ofrenda`, `shicras`），直接匹配并注释。
3.  **Layer 3: 句法骨架 (Syntax Skeleton)** 🔵
    *   识别动词过去时态（`-ó`），快速定位句子的核心动作。

## 🚀 快速开始

### 1. 环境准备
确保你的电脑安装了 Python 3。
建议安装 `colorama` 库以获得最佳视觉体验：
```bash
pip install colorama
