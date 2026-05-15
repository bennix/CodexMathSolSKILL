# Codex Math Visual Solver Skill / Codex 数学可视化解题技能

## 中文说明

`math-visual-solver` 是一个面向 Codex 的数学解题技能，适合处理中文数学题、几何题、函数题、图形可视化、LaTeX PDF 排版，以及支持 LaTeX 公式显示的 Manim MP4 动画。

它的目标不是只给答案，而是生成可教学、可验证、可交付的解题材料：

- 中文题意复述与条件梳理
- 图形化解题策略
- 两种方法求解与交叉验证
- MetaPost 静态几何图
- 中文 LaTeX PDF
- Manim 动态动画 MP4，公式使用 `MathTex` 渲染

### 仓库结构

```text
.
├── README.md
├── install.sh
├── install_math_visual_solver.command
└── math-visual-solver/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   └── workflow.md
    └── scripts/
        └── scaffold_math_pdf.py
```

### 在 Codex 中安装

#### 方法一：命令行安装

```bash
git clone https://github.com/bennix/CodexMathSolSKILL.git
cd CodexMathSolSKILL
./install.sh
```

安装目标默认为：

```bash
~/.codex/skills/math-visual-solver
```

如果你的 Codex 使用了自定义目录，可以先设置 `CODEX_HOME`：

```bash
CODEX_HOME=/path/to/codex-home ./install.sh
```

安装后请重启 Codex。

#### 方法二：macOS 双击安装

在 Finder 中双击：

```text
install_math_visual_solver.command
```

如果 macOS 阻止运行，请右键该文件，选择 **Open / 打开**。

### 如何使用

在 Codex 对话中直接写 `$math-visual-solver`：

```text
使用 $math-visual-solver 解析这张题图：请中文讲解、两种方法验证、画几何图、生成 PDF，并输出支持 LaTeX 公式显示的 Manim MP4。
```

也可以写得更短：

```text
用 $math-visual-solver 解这题，生成 LaTeX PDF 和 LaTeX 公式动画 MP4。
```

### 生成动画需要的本机依赖

如果要输出 Manim MP4，目标机器需要具备：

- Python
- Manim Community Edition
- TeX / LaTeX
- `dvisvgm`
- `ffmpeg`

在 macOS/Homebrew 上可以参考：

```bash
brew install texlive dvisvgm ffmpeg
python3 -m venv .venv-manim
.venv-manim/bin/pip install manim
```

PDF 生成通常需要：

- `xelatex` 或 `lualatex`
- `mpost`
- 中文字体，例如 macOS 自带的 Songti SC

### 验证安装

重启 Codex 后，在新对话中输入：

```text
使用 $math-visual-solver 解一道简单二次函数题，并生成中文说明。
```

如果 Codex 加载了该技能，它会按中文、可视化、两种方法验证、LaTeX/PDF/动画工作流来处理。

## English

`math-visual-solver` is a Codex skill for math problem solving, visual explanation, Chinese math questions, geometry diagrams, LaTeX PDF typesetting, and Manim MP4 animations with LaTeX-rendered formulas.

It is designed to produce teachable and verifiable solution artifacts, not just final answers:

- Chinese problem restatement and condition extraction
- Visual solving strategy
- Two independent solution methods with cross-checking
- MetaPost static geometry figures
- Chinese LaTeX PDF output
- Manim MP4 animation output with formulas rendered through `MathTex`

### Repository Layout

```text
.
├── README.md
├── install.sh
├── install_math_visual_solver.command
└── math-visual-solver/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   └── workflow.md
    └── scripts/
        └── scaffold_math_pdf.py
```

### Install in Codex

#### Option 1: command line

```bash
git clone https://github.com/bennix/CodexMathSolSKILL.git
cd CodexMathSolSKILL
./install.sh
```

The default install target is:

```bash
~/.codex/skills/math-visual-solver
```

If your Codex uses a custom home directory, set `CODEX_HOME`:

```bash
CODEX_HOME=/path/to/codex-home ./install.sh
```

Restart Codex after installation.

#### Option 2: macOS double-click installer

Double-click:

```text
install_math_visual_solver.command
```

If macOS blocks the script, right-click it and choose **Open**.

### Usage

Mention `$math-visual-solver` in a Codex prompt:

```text
Use $math-visual-solver to solve this math problem visually in Chinese, verify it with two methods, generate a PDF, and output a Manim MP4 with LaTeX-rendered formulas.
```

For an uploaded image:

```text
Use $math-visual-solver to parse this problem image, explain it in Chinese, draw the geometry, verify by two methods, generate a LaTeX PDF, and output a LaTeX-capable Manim MP4.
```

### Local Dependencies for Animation

To render Manim MP4 videos, the target machine needs:

- Python
- Manim Community Edition
- TeX / LaTeX
- `dvisvgm`
- `ffmpeg`

On macOS with Homebrew:

```bash
brew install texlive dvisvgm ffmpeg
python3 -m venv .venv-manim
.venv-manim/bin/pip install manim
```

PDF generation usually needs:

- `xelatex` or `lualatex`
- `mpost`
- a CJK font, such as Songti SC on macOS

### Verify Installation

After restarting Codex, try:

```text
Use $math-visual-solver to solve a simple quadratic function problem and generate a Chinese visual explanation.
```

If the skill is loaded, Codex should follow the visual, Chinese, two-method verification, LaTeX/PDF, and optional Manim animation workflow.
