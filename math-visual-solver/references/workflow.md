# Math Visual Solver Workflow

## Problem Analysis

Use this checklist before writing the final answer:

- Restatement: transcribe the problem accurately in Chinese. Preserve numbering and subquestions.
- Objects: list points, lines, curves, functions, variables, domains, and parameters.
- Goals: separate "prove" targets from numerical targets.
- Visual invariants: look for rotation, reflection, translation, homothety, similarity, congruence, equal angles, parallel lines, cyclic quadrilaterals, area ratios, coordinates, vectors, and complex-plane structure.
- Verification plan: choose two independent methods, for example synthetic geometry plus coordinates, algebra plus graphing, calculus plus inequality, or vector proof plus transformation proof.

## Solution Structure

Recommended Chinese section titles:

```tex
\section*{原题复述}
\section*{解题策略}
\section*{方法一：几何变换法}
\section*{方法二：坐标或向量验证}
\section*{互相印证}
\section*{更快捷的思路}
\section*{结论}
```

For non-geometry problems, rename method titles to match the domain, such as `代数法`, `函数图像法`, `微积分法`, `数形结合法`, `不等式法`.

## Manim Community Edition

Use Manim when an animation helps the explanation:

```bash
manim -pql scene.py SceneName
manim -pqh scene.py SceneName
manim -s -ql scene.py SceneName
```

For deliverable MP4 animations with formulas, prefer a LaTeX-capable render:

```bash
# Use the project venv if present; otherwise use the available manim executable.
export PATH=/opt/homebrew/bin:$PATH
TEXLIVE_PREFIX="$(brew --prefix texlive 2>/dev/null || true)"
if [ -n "$TEXLIVE_PREFIX" ]; then
  export TEXMFCNF="$TEXLIVE_PREFIX/share/texmf-dist/web2c"
  export TEXMFROOT="$TEXLIVE_PREFIX/share"
fi
manim -qm --media_dir media_latex scene.py SceneName

cp media_latex/videos/scene/720p30/SceneName.mp4 SceneName_LaTeX.mp4
```

Adjust the TeX paths to the local TeX installation when not using Homebrew. If Manim fails while converting LaTeX to SVG, check `dvisvgm --version`, `latex --version`, and `kpsewhich -var-value=TEXMFROOT`.

Common scene pattern:

```python
from manim import *

class VisualProof(Scene):
    def construct(self):
        title = Text("几何关系的动态说明", font="Noto Sans CJK SC").scale(0.6)
        equation = MathTex(r"x^2+x-1=0", font_size=36)
        self.play(Write(title))
        self.play(Write(equation))
        self.wait()
```

Guidelines:

- Use `ValueTracker` for moving points or changing parameters.
- Use `always_redraw` for dependent segments, labels, and intersections.
- Use `Rotate`, `Transform`, `Angle`, `RightAngle`, `DashedLine`, and color coding to make the strategy visible.
- Use `MathTex` for equations, ratios, fractions, radicals, variables, and mathematical point/length labels such as `AF=CG`, `GN=2NE`, or `x=\frac{\sqrt5-1}{2}`.
- Use `Text` for Chinese prose. For mixed Chinese/formula lines, build a `VGroup` from `Text` and `MathTex` fragments instead of putting raw TeX into `Text`.
- Render formula-heavy animations at `-qm` or higher so fractions and radicals remain legible.
- Export a still frame for the PDF only when MetaPost is not the better static tool. Prefer MetaPost for crisp contest-style geometry.

Before delivering an MP4:

```bash
test -s SceneName_LaTeX.mp4
ffprobe -v error -show_entries format=duration,size \
  -show_entries stream=codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 SceneName_LaTeX.mp4
ffmpeg -y -ss 00:00:03 -i SceneName_LaTeX.mp4 -frames:v 1 -update 1 preview_03s.jpg
```

Open at least one preview frame and verify that formulas are actual LaTeX-rendered glyphs, not plain text fallbacks or missing boxes.

## MetaPost for Static PDF Figures

Use MetaPost for exact static diagrams. Keep figures close to the proof text.

Minimal figure file:

```metapost
prologues := 3;
outputtemplate := "%j-%c.mps";
beginfig(1);
  pair A,B,C,D,E,F,G;
  A := (0,0); D := (5,0);
  B := (1.1,3.2); C := B + (D-A);
  draw A--B--C--D--cycle withpen pencircle scaled 1;
  label.bot(btex $A$ etex, A);
  label.bot(btex $D$ etex, D);
  label.lft(btex $B$ etex, B);
  label.rt(btex $C$ etex, C);
endfig;
end
```

Compile:

```bash
mpost figures.mp
```

Embed in LaTeX near the relevant text:

```tex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=.62\linewidth]{figures-1.mps}
  \caption{旋转构造与关键交点}
\end{figure}
```

## Chinese LaTeX Requirements

Use `ctexart` or `ctexrep`. Prefer LuaLaTeX or XeLaTeX for Chinese text.

Do not leave Markdown syntax in the `.tex` file:

- Convert `# 标题` to `\section*{标题}`.
- Convert `**重点**` to `\textbf{重点}`.
- Convert Markdown lists to `enumerate` or `itemize`.
- Convert code fences to `verbatim` only when code must appear.
- Convert image links to `figure` environments.

Useful packages:

```tex
\documentclass[UTF8,zihao=-4]{ctexart}
\usepackage[a4paper,margin=2.2cm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{graphicx}
\usepackage{float}
\usepackage{xcolor}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
```

## Verification

Before final delivery:

1. Compile MetaPost: `mpost figures.mp`.
2. Compile LaTeX twice: `lualatex main.tex` or `xelatex main.tex`.
3. Search the `.tex` source for leftover Markdown markers: `rg '#|\*\*|```|!\[' main.tex`.
4. Inspect rendered pages or convert the PDF to PNG. Check Chinese glyphs, formula layout, figure placement, and labels.
5. Report exact commands run and any missing local dependencies.
