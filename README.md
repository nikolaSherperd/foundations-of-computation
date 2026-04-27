# Foundations of Computation

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat&logo=c&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=c%2B%2B&logoColor=white)
![Vim](https://img.shields.io/badge/Vim-019733?style=flat&logo=vim&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-555555?style=flat&logo=gnubash&logoColor=white)

The acquisition of deep technical mastery in the modern era suffers from a fundamental fragmentation. Traditional computer science curricula often divorce theory from practice, while bootcamp-style accelerated learning frequently produces "abstraction-dependent" developers — practitioners who can manipulate high-level APIs but lack the foundational reasoning to troubleshoot systems at the hardware and mathematical level.

This repository documents my effort to rebuild mathematical and computational foundations from first principles.

Rather than relying on high-level libraries, I focus on implementing and visualizing core ideas directly in Python, C, and C++. The goal is conceptual clarity, not performance.

---

## Tier 0: Foundations of Technical Mastery (The Bedrock)

**Total Duration**: 9–12 months  
**Prerequisites**: None  
**Objective**: Eliminate abstraction dependency. Achieve mathematical fluency and low-level memory mastery.

### Mathematics: The Language of Computation

Mathematics in this tier is treated as a practical tool for modeling reality. The curriculum moves from intuition to rigor to application.

- **Linear Algebra**  
  The engine of modern computing (graphics, machine learning, optimization).  
  - **Intuition**: 3Blue1Brown – Essence of Linear Algebra series  
  - **Rigor**: MIT 18.06 (Gilbert Strang) – vector spaces, null spaces, eigenvalues, SVD  
  - **Application**: Mathematics for Machine Learning (Imperial College London)

- **Calculus & Optimization**  
  Essential for understanding gradients, neural network training, and backpropagation.  
  Focus: Multivariate calculus, partial derivatives, chain rule, Lagrange multipliers.

- **Probability & Statistics**  
  The language of uncertainty in AI, robotics, and data-driven systems.  
  Focus: Random variables, Bayesian inference, Gaussian distributions, maximum likelihood estimation.

- **Discrete Mathematics**  
  The mathematics of digital structures.  
  Focus: Logic, set theory, combinatorics, graph theory, proof by induction.  
  Resources: A Walk Through Combinatorics, MIT/Princeton lecture series.

### Systems Programming: The C Language

C is chosen because it forces explicit management of machine resources.

- **Primary Text**: The C Programming Language (K&R) — valued for its brevity and precision.  
- **Key Concepts**: Pointers, manual memory management (`malloc`/`free`), stack vs heap, pointer arithmetic.  
- **Approach**: No IDEs initially. Use CLI tools only — GCC, GDB, Valgrind — to fully understand the compilation and debugging process.

---

## Early Progress (Weeks 1–4): Mathematical Intuition

During the first four weeks, the focus is on building strong visual and intuitive understanding before diving into rigor.

**End Project**: Python truth table generator + Manim visualizations for 2D/3D vector transformations.

### Topics Covered So Far

- **Boolean Logic**  
  Scripts that generate truth tables for complex Boolean expressions. These were written to better understand how symbolic logic maps to actual computation.

- **Linear Algebra**  
  Basic vector operations and linear transformations implemented from scratch to reinforce geometric intuition.

- **Visualization**  
  Manim scenes used to animate vectors, transformations, and coordinate changes. Visualization serves as a powerful thinking tool to expose and correct misunderstandings.

---

## Motivation

I believe strong research and technical work depends on a deep understanding of fundamentals. This repository reflects my intentional effort to build that understanding through direct implementation and visualization.

---

## Repository Structure

```bash
.
├── Mathematical_Foundations/     # Core mathematical implementations and visualizations
│   ├── Boolean_Logic/            # Truth table generators
│   ├── Linear_Algebra/           # Vector operations and transformations
│   └── Visualization/            # Manim animations
├── C_Implementations/            # Low-level C/C++ versions (planned)
├── common/                       # Shared utilities and helpers
├── Makefile                      # Build and run scripts (when applicable)
└── README.md
