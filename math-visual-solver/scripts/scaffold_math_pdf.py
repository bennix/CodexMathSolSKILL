#!/usr/bin/env python3
"""Create a Chinese LaTeX + MetaPost math-solution scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path


MAIN_TEX = r"""\documentclass[UTF8,zihao=-4]{ctexart}
\usepackage[a4paper,margin=2.2cm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{graphicx}
\usepackage{float}
\usepackage{xcolor}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}

\title{%TITLE%}
\author{}
\date{}

\begin{document}
\maketitle

\section*{原题复述}
在这里准确复述题目。

\section*{解题策略}
先说明图形、变量、关键构造和两种验证方法。

\begin{figure}[H]
  \centering
  \includegraphics[width=.62\linewidth]{figures-1.mps}
  \caption{题目图形与关键构造}
\end{figure}

\section*{方法一}
写出第一种解法。

\section*{方法二}
写出第二种解法，并尽量独立于方法一。

\section*{互相印证}
说明两种方法如何得到同一结论。

\section*{更快捷的思路}
如果存在更短解法，写在这里；否则说明本题关键在前述构造。

\section*{结论}
完整回答所有小问。

\end{document}
"""


FIGURES_MP = r"""prologues := 3;
outputtemplate := "%j-%c.mps";

beginfig(1);
  pair A,B,C,D;
  A := (0,0);
  D := (5cm,0);
  B := (1cm,3cm);
  C := B + (D-A);

  draw A--B--C--D--cycle withpen pencircle scaled 1;
  label.bot(btex $A$ etex, A);
  label.lft(btex $B$ etex, B);
  label.rt(btex $C$ etex, C);
  label.bot(btex $D$ etex, D);
endfig;

end
"""


README = """Build order:
1. mpost figures.mp
2. lualatex main.tex
3. lualatex main.tex

Before delivery, inspect the PDF and search main.tex for leftover Markdown:
rg '#|\\*\\*|```|!\\[' main.tex
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Output folder for the LaTeX project")
    parser.add_argument("--title", default="数学题可视化解答", help="Chinese PDF title")
    args = parser.parse_args()

    out = Path(args.folder).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    (out / "main.tex").write_text(MAIN_TEX.replace("%TITLE%", args.title), encoding="utf-8")
    (out / "figures.mp").write_text(FIGURES_MP, encoding="utf-8")
    (out / "README.txt").write_text(README, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
