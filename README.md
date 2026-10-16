# 张远民简历

本仓库保存整理后的个人简历文件。

## 文件说明

- [`resume/Zhang_Yuanmin_Resume.pdf`](resume/Zhang_Yuanmin_Resume.pdf)：单页 A4 PDF，可直接下载、打印或投递。
- [`resume/Zhang_Yuanmin_Resume_HD.png`](resume/Zhang_Yuanmin_Resume_HD.png)：高清图片版本。
- [`resume/build_resume_pdf.py`](resume/build_resume_pdf.py)：PDF 生成源文件，可修改文字与版式后重新生成。
- [`resume/portrait.png`](resume/portrait.png)：简历使用的形象照。

## 重新生成

源文件使用 Python 和 ReportLab。运行前安装依赖：

```bash
python -m pip install reportlab
python resume/build_resume_pdf.py
```

生成后的 PDF 会保存至 `resume/Zhang_Yuanmin_Resume.pdf`。
