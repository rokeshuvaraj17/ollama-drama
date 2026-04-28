# CS5704 Software Testing Study Chatbot

## Overview
This project implements a customized study chatbot using Ollama to assist students in preparing for software testing concepts in CS5704.

## Features
- Explains core software testing concepts
- Provides structured answers with examples
- Highlights key exam insights
- Includes follow-up questions for learning reinforcement

## Topics Covered
- Definition of testing
- Why testing is hard
- Black-box vs White-box testing
- Equivalence classes and boundary value analysis
- Unit testing and assertions
- Cyclomatic complexity
- Coverage metrics (statement, branch, path)
- Testing strategies (unit, integration, validation, system)
- LLMs for testing (benefits and challenges)

## Setup Instructions

### 1. Install Ollama
https://ollama.com

### 2. Create the chatbot model
```bash
ollama create cs5704-tutor -f Modelfile