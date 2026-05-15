---
name: math-visual-solver
description: Use when solving, explaining, visualizing, animating, or typesetting any math problem, especially Chinese math questions, geometry diagrams, LaTeX-capable Manim MP4 animations, MetaPost visuals, two-method verification, Markdown-to-LaTeX cleanup, or PDF delivery.
---

# Math Visual Solver

## Core Rule

For every math problem, produce a visual, Chinese, verification-oriented solution. Do not stop at a bare answer unless the user explicitly asks for only the answer.

## Required Output Structure

1. Restate the original problem in Chinese.
2. Extract known conditions, target conclusions, hidden constraints, and likely traps.
3. Give a visual strategy before algebra: describe the diagram, moving points, rotations, symmetries, auxiliary lines, or coordinate model.
4. Solve by two independent methods whenever feasible.
5. Cross-check that both methods give the same result; explain any discrepancy before finalizing.
6. Add a faster or more elegant method when one exists.
7. Produce clean Chinese LaTeX suitable for PDF output when the user asks for a document, handout, or PDF. When the user asks for animation/video, produce a Manim MP4 whose formulas are rendered with LaTeX.

## Visual Tool Choice

- Use MetaPost for precise static geometry in PDFs, especially contest geometry, labeled points, intersections, rotations, angle marks, and length relations.
- Use Manim Community Edition for dynamic explanations, animations, moving points, transformations, rotations, loci, or "形象化表示". The upstream project describes Manim as an animation engine for explanatory math videos.
- In Manim animations, render mathematical expressions with `MathTex`, not plain `Text`. Use `Text` only for Chinese prose or non-formula labels. If a line mixes Chinese and formulas, compose it from `Text` plus `MathTex` fragments.
- Use both when useful: Manim for animation/storyboard, MetaPost for final print figures embedded in the PDF.

## Manim MP4 Workflow

When producing an animation:

1. Create the scene source in the working folder and name the deliverable MP4 clearly, for example `<SceneName>_LaTeX.mp4`.
2. Use `MathTex` for all displayed formulas, equations, ratios, roots, fractions, and symbolic labels. Keep Chinese text in a CJK-capable `Text` font.
3. Ensure the local render stack has Manim, a TeX engine, `dvisvgm`, and `ffmpeg`. If a dependency is missing, install it when allowed; otherwise write the source and report the missing dependency.
4. Render with Manim to MP4, preferring at least 720p for formula readability.
5. Verify the MP4 before delivery: check the file is non-empty, inspect codec/resolution/duration with `ffprobe`, extract representative frames with `ffmpeg`, and visually confirm LaTeX formulas render correctly.

Read `references/workflow.md` for exact Manim commands, TeX environment notes, and verification commands.

## PDF Workflow

When producing a Chinese LaTeX PDF:

1. Create a working folder for the problem.
2. Run `scripts/scaffold_math_pdf.py <folder> --title "<title>"` from this skill to create `main.tex`, `figures.mp`, and `README.txt`.
3. Put all prose in LaTeX, not Markdown. The rendered PDF must not show Markdown markers such as `#`, `**`, raw backticks, or Markdown image syntax.
4. Write formulas as LaTeX math, using `\( ... \)`, `\[ ... \]`, `align`, `cases`, or theorem-like environments as appropriate.
5. Put every MetaPost figure immediately after the paragraph that introduces it. Do not dump all figures at the end.
6. Compile with LuaLaTeX/XeLaTeX plus MetaPost, then inspect the PDF or rendered pages before claiming completion.

Read `references/workflow.md` when creating an actual solution artifact, especially for Manim MP4 commands, TeX/`dvisvgm` setup, MetaPost embedding, and PDF verification.

## Quality Bar

- The answer must be teachable: show why the construction was chosen.
- Geometry proofs must name the transformation or congruence/similarity used, not merely state it.
- Computation-heavy solutions must define variables and domains.
- If the original image is ambiguous, state assumptions and preserve them in the PDF.
- If a requested tool is unavailable locally, still write the source files and report the missing compiler/renderer clearly.
