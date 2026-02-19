# Introduction to Artificial Intelligence (BGU) – Project Portfolio

This repository contains a comprehensive suite of projects completed as part of the **Introduction to Artificial Intelligence** course at **Ben-Gurion University (BGU)**.

The assignments span a wide range of AI methodologies — from classical state-space search and adversarial reasoning to reinforcement learning and modern LLM-based agentic workflows.

---

## 🚀 Projects Overview

---

## 1️⃣ Heuristic Search – The Color Block Sorting Robot

**Objective:**  
Solve a complex 3D combinatorial puzzle using the **A\* Search Algorithm**.

### 🧩 Problem Description
A robot must sort a vertical tower of colored cubes using two operators:

- **Spin** – 90° rotation of the entire tower  
- **Flip** – Reverse a sub-stack from the bottom  

The goal is to reach a target configuration using the minimal number of moves.

### 🔹 Technical Highlights
- Custom state-space representation for 3D cube configurations  
- Implemented a **Base Heuristic** based on adjacent color pairs  
- Designed an **Advanced Heuristic** optimized for runtime efficiency while preserving optimality  
- Full A\* implementation with priority queue and cost tracking  

**Tools:** Python 3.10+

---

## 2️⃣ Adversarial Search – IsoKnight Game Engine

**Objective:**  
Develop an AI agent capable of playing **IsoKnight**, a two-player competitive strategy game.

### 🎮 Game Mechanics
- Played on an **m × n grid**
- Players move a "Knight" piece (L-shaped moves)
- Cells cannot be revisited
- The board gradually shrinks as moves are made

The player who runs out of legal moves loses.

### 🔹 Technical Highlights
- Implemented the **Minimax algorithm**
- Integrated **Alpha-Beta Pruning** for efficient deep search
- Supported boards up to **6×6**
- Designed a heuristic based on:

```python
P1_moves - P2_moves
```
## 3️⃣ Automated Planning – Harmony Community Garden

**Objective:**  
Solve multi-agent coordination problems using **PDDL (Planning Domain Definition Language)**.

---

### 🌱 Scenario

Coordinate three specialized volunteers:

- **Cultivator**
- **Planter**
- **Waterer**

The objective is to transform a neglected plot into a thriving community garden by generating a valid and optimal sequence of actions.

---

### 🔹 Technical Highlights

- Defined complex **Preconditions** and **Effects** for domain actions:
  - `till-soil`
  - `sow-seeds`
  - `water-garden`
- Modeled action dependencies (e.g., planting requires soil to be tilled first)
- Implemented multi-agent coordination constraints within the planning domain
- Used a **Domain-Independent Planner** to generate optimal action sequences
- Designed modular and flexible domain/problem files supporting multiple town layouts

---

**Tools:** PDDL + Planner Engine

---

## 4️⃣ Reinforcement Learning – Cliff Walking & The Gambler

**Objective:**  
Apply **Markov Decision Processes (MDPs)** and **Temporal-Difference Learning** to solve sequential decision-making and optimization problems.

---

### 🧗 Cliff Walking

Implemented a reinforcement learning agent to safely navigate a hazardous gridworld environment.

#### 🔹 Implementation Details
- Implemented **Q-Learning**
- Trained an agent to avoid falling off the cliff while minimizing total cost
- Used **Epsilon-Greedy action selection** to balance exploration and exploitation
- Tracked episode rewards and convergence behavior

The agent learns an optimal policy through trial-and-error interaction with the environment.

---

### 🎲 Modified Gambler’s Problem

Implemented a dynamic programming solution to compute the optimal betting strategy under stochastic transitions.

#### 🔹 Implementation Details
- Implemented **Value Iteration**
- Solved **Bellman Optimality Equations** until convergence
- Modeled betting outcomes using custom dice rules:
  - Sum < 7 → Loss
  - Sum = 7 → Special outcome
  - Sum > 7 → Win
- Computed optimal policy across all capital states

The algorithm iteratively updates state-value estimates until reaching a stable optimal solution.

---

### 🔹 Technical Highlights

- Implemented and solved **Bellman Equations**
- Designed convergence detection logic
- Tuned hyperparameters for learning stability
- Analyzed policy behavior under different reward structures
- Structured experiments for reproducibility

---

**Tools:**  
Python • NumPy • Gymnasium (OpenAI Gym)

---

---

## 5️⃣ Agentic AI – LLM Multi-Agent System

**Objective:**  
Build a modern, agentic architecture using **LangGraph** to bridge LLM reasoning and custom AI algorithms.

---

### 🏗 Architecture Overview

The system consists of three interacting agents:

#### 🔹 Executor Agent
- Uses custom AI implementations as callable tools  
- Solves problems deterministically (e.g., A\* search cost computation)  
- Acts as a symbolic ground-truth engine  

#### 🔹 LLM Solver Agent
- Attempts to solve the same problems using raw LLM reasoning  
- Relies on prompt-based reasoning without deterministic search  

#### 🔹 LLM Judge
- Compares outputs from both agents  
- Analyzes discrepancies  
- Produces structured summaries of differences  
- Evaluates reasoning quality and correctness  

---

### 🔹 Technical Highlights

- Orchestrated multi-agent workflows using **LangGraph**
- Implemented structured tool-calling pipelines
- Integrated LLM providers (Gemini / Ollama)
- Designed evaluation logic bridging symbolic and neural reasoning
- Built modular agent graph architecture for extensibility
- Enabled automated comparison between algorithmic and LLM-based solutions

---
---

## 🛠 Skills & Technologies

### 💻 Languages
- Python 3.10+
- PDDL

### 📦 Frameworks & Libraries
- LangGraph
- Gymnasium (OpenAI Gym)
- NumPy

### 🧠 Core Concepts Covered
- A* Search
- Heuristic Design
- Minimax
- Alpha-Beta Pruning
- Markov Decision Processes (MDPs)
- Q-Learning
- Value Iteration
- Bellman Equations
- Agentic Workflows
- LLM Tool-Calling Architectures

---

## 📁 Repository Structure

```bash
/heuristic_search
/AlphaBetaPrunning
/Planning
/RL_MDP
/Agentic_Ai
```
---
### 🎓 Academic Context

Developed by Roii Agassi

B.Sc. in Software and Information Systems Engineering
Ben-Gurion University of the Negev (BGU)
