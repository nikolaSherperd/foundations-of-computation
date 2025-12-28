# Foundations of Computation
The acquisition of deep technical mastery in the moden era suffers from a fundamental fragmentation. Traditional computer science curricula ofen divorce theory from practice, while the bootcamp-styled accelerated learning frequently produces "abstraction-independent" developers—practitioners who can manipulate high level APIs but lack the foundational reasoning to troubleshoot systems at the hardware and mathematical level.


This repository documents my effort to rebuild mathematical and computational foundations from first principles.

Rather than relying on high-level libraries, I focus on implementing and visualizing core ideas directly in Python, C/C++. The goal is conceptual clarity, not performance.

## Contents

### Tier 0: Foundations of Technical Mastery (The Bedrock)
Total Duration: 9-12 months

Prerequisites: None

Objective: Eliminate abstaction dependency. Achieve mathematical fluency and low-level
memory mastery


##   2.2 Detailed Curriculum and Resource Mapping
###  2.2.1 Mathematics: The Language of Computation
     Mathematics in this tier is not treated as an abstract intellectual exercise but as a tool for
     modeling reality. The curriculum moves from intuition to rigor to application.


●  Linear Algebra: The study of vector spaces is the engine of modern computing.
   -  Intuition: The 3Blue1Brown Essence of Linear Algebra series 1 provides the
      geometric intuition required to visualize transformations.
      
   -  Rigor: MIT 18.06 (Gilbert Strang) 1 provides the theorem-proof foundation,
      covering vector spaces, null spaces, eigenvalues, and Singular Value
      Decomposition (SVD).
      
   -  Application: Mathematics for Machine Learning (Imperial College London) 1
      bridges the gap to optimization.


●  Calculus & Optimization: Understanding gradients is non-negotiable for training
   neural networks.
   -  Focus: Multivariate calculus, partial derivatives, the chain rule (backpropagation),
      and Lagrange multipliers.


●  Probability & Statistics: The language of uncertainty in robotics and AI.
   -  Focus: Random variables, Bayesian inference, Gaussian distributions, and
      maximum likelihood estimation.1


●  Discrete Mathematics: The mathematics of digital structures.
   -  Focus: Logic, set theory, combinatorics, graph theory, and proof by induction.
      Resources include A Walk Through Combinatorics 1 and MIT/Princeton lecture
      series.


## 2.2.2 Systems Programming:
         The C Language is chosen not for its modern popularity, but because it forces the programmer to manage
         the machine's resources explicitly.
●  Text: The C Programming Language (K&R) 1 remains the de�nitive text for its brevity and
   precision.
●  Key Concepts: Pointers, manual memory management (malloc/free), stack vs. heap
   representation, and pointer arithmetic. The curriculum explicitly forbids the use of IDEs
   initially, mandating CLI tools (GCC, GDB, Valgrind) to demystify the compilation process.


##  WEEK 1:
##  For the first four weeks of this tier, i'd be exploring the following subject matters;
   The objective is to establish a visual intuition of vectors and logic... 

### Boolean Logic
Scripts that generate truth tables for complex Boolean expressions. These were written to better understand how symbolic logic maps to computation.

### Linear Algebra
Basic vector operations and linear transformations implemented explicitly to reinforce geometric intuition.

### Visualization
Manim scenes used to visualize vectors, transformations, and coordinate changes. Visualization is used as a thinking tool to expose misunderstandings.

## Motivation
I believe strong research work depends on deep understanding of fundamentals. This repository reflects an intentional effort to build that understanding through implementation and visualization.
