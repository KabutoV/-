# 张远民简历

本仓库保存整理后的个人简历文件。

## 文件说明

- [`resume/Zhang_Yuanmin_Resume.pdf`](resume/Zhang_Yuanmin_Resume.pdf)：单页 A4 PDF，可直接下载、打印或投递。
- [`resume/Zhang_Yuanmin_Resume_HD.png`](resume/Zhang_Yuanmin_Resume_HD.png)：高清图片版本。
- [`resume/build_resume_pdf.py`](resume/build_resume_pdf.py)：PDF 生成源文件，可修改文字与版式后重新生成。
- [`resume/resume.html`](resume/resume.html)：新版无衬线字体排版源文件。
- [`resume/portrait.png`](resume/portrait.png)：简历使用的形象照。

## 重新生成

推荐使用 WeasyPrint 从 HTML 重新生成新版 PDF：

```bash
python -m pip install weasyprint
weasyprint resume/resume.html resume/Zhang_Yuanmin_Resume.pdf
```

也可以直接运行 `python resume/build_resume_pdf.py`；该脚本会使用同一 HTML 源文件生成 PDF。
