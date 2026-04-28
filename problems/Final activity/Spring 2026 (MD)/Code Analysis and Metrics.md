[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
2/24/2026

Announcements

PM1.2 due tomorrow (2/25) before midnight
Design Activities
PM1.3
Demo slides due next Thursday (3/5) before class (12:30pm 🚨)
Report, project repo, and retrospective (individual) due next Friday (3/6) before midnight
Final Demo timing changed to 8 minutes 🚨

‹#›

Demo Rubric



‹#›

Report Rubric



‹#›

Code Analysis and Metrics

Implementation Overview
Code Quality Metrics
Software Analysis
AI for Writing Code

Learning Outcomes

By the end of the course, students should be able to:
Implement a software system following the software life cycle phases
Develop software engineering skills working on a team project
Identify processes related to phases of the software lifecycle
Explain the differences between software engineering processes
Discuss research questions and studies related to software engineering
Communicate (via demo and writing) details about a developed software application

‹#›

Warm-Up

Find a partner to discuss the following question:
What is the most interesting software product you have implemented (written some code for)?

‹#›

Implementation

Goal: translate software design into a concrete system (i.e. write code)
• Can use any programming language, but some languages are better suited to certain types of programs than others
• SE/implementation is a team activity!
• Software Artifacts: source code, documentation, configuration files, media, executables, bug database, source code repository, issue trackers…

‹#›

Design to Implementation





‹#›

Implementation in Practice

Tools and processes support productive programming among software development teams.
Software engineers spend limited time actually coding!



‹#›

Code Quality

Software metrics provide a systematic way to characterize the quality of software based on a set of clearly defined rules.
Why study code quality?
Assists in the evaluation and analysis of design;
Provides an indication of the complexity of code to enhance development and maintenance;
Improving code quality
Predicting errors
Optimizing programs
Enforce consistent coding styles
Measuring complexity
Evaluating team and process productivity
Facilitates more effective testing.

‹#›

Code Metrics

Lines of Code
Weighted Methods per Class
Halstead Complexity
Cyclomatic Complexity
Inheritance Tree Depth (object-oriented)
Number of Children (object-oriented)

‹#›

Maintainability Index (MI): is a composite metric that incorporates a number of traditional source code metrics into a single number that indicates relative maintainability. 

Lines of Code

The number of lines of code in a given program.
Using less code for the same functionality improves readability and maintainability.
More lines of code = more maintenance

‹#›

Lines of Code (cont.)

LOC is difficult to measure.
How do we actually count lines of code?
i.e. comments, multi-line statements, blanks,…
Example: How many lines of code is this?

wc -l

sloc test.py

cloc test.py

5

‹#›

Different tools provide different results, which may be more drastic for more advanced programs!
How do you handle comments, multi-line statements, blank lines, across multiple files, etc…?

Weighted Methods per Class (WMC)

Metric to indicate the sum of complexities for methods defined in a class.
Simple: the # of methods in a class
Advanced: Weighted sum

‹#›

Halstead’s Metrics

Metrics of the software should reflect the programming language.
Calculations: 

Ƞ = Ƞ1log2Ƞ1 + Ƞ2log2Ƞ2
Length: N = N1 + N2
Volume: V = N \* log2Ƞ
Difficulty: D = Ƞ1 / 2 \* N2 / Ƞ2
Effort: E = D \* V

The distinct operators (what action to perform) are: main, (), {}, int, scanf, &, =, +, /, printf, ,, ; (12)
The distinct operands (what to apply actions to) are: a, b, c, avg, "%d %d %d", 3, "avg = %d" (7)

‹#›

Cyclomatic Complexity

The number of independent paths in a program.
Also known as McCabe's Cyclomatic Complexity
Measures the number of linear segments in a method (branches)
Useful for measuring the minimum number of test cases for comprehensive testing
Calculate:
Number of decisions + 1

‹#›

Cyclomatic Complexity Examples

public static String evenOdd(int num) {
if (num == 0) {
return "Even";
} else if (num == 2) {
return "Even";
} else if (num == 4) {
return "Even";
} else if (num == 6) {
return "Even";
} else if (num == 8) {
return "Even";
} else {
return "Odd";
}
}











6

‹#›

Cyclomatic Complexity Examples…

public static String evenOdd(int num) {
if (num == 0 || num == 2 || num == 4 || num == 6 || num == 8) {
return "Even";
}
return "Odd";
}











6

public static String evenOdd(int num) {
if (num % 2 == 0) {
return "Even";
}
return "Odd";
}



2

‹#›

Object-Oriented Metrics

Inheritance Tree Depth: Maximum length from node to a root in class hierarchy tree.
Number of Children: Number of direct descendants (subclasses) for each class.

‹#›

Depth: 2
#Children: 3

Depth/Children: Design Tradeoffs

Objects with a large number of children (depth and direct) are:
Difficult to modify
Require more testing
More complex and error-prone
BUT, have greater reuse of defined methods and make overall program easier to modify!

‹#›

Which Metric?

Lots of code metrics have been proposed
Halstead's measures
Cyclomatic complexity
Many object-oriented measures
…

But nothing works better (predicting effort and errors) than counting lines of code (LOC)!
El Emam: "Confounding Effects of Class Size on the Validity of Object-Oriented Metrics" [2001]
Herraiz: "Beyond Lines of Code: Do We Need More Complexity Metrics?" [2010]

‹#›

“The impossible holy grail” [Fenton]

‹#›

[Sharma]

A survey of 78 software engineers found…

Code Analysis Tools

Manual analysis of code is very valuable, but also inefficient.
Ideally, peer code reviews should be combined with automated tools.
Many automated tools can programmatically analyze large software systems.
Static Analysis
Dynamic Analysis

‹#›

Static Analysis

The process of automatically examining source code without executing the application.
analysis tools, code metrics, linters, code clone detection, etc.
Why static analysis?
Improves code quality
Finds errors more effectively and efficiently
Reduces technical debt and software costs
Increases productivity

‹#›

How to do static analysis?

Convert your code into a program representation
Text matching
Regex, diffs, longest common subsequence, etc…
But typically ineffective and inaccurate for code
Abstract Syntax Tree (AST)\*
Call Graphs\*
Control Flow Graphs (CFG)
Program Dependency Graph\*
Tokenization\*

‹#›

Abstract Syntax Trees

Tree representation for the source code structure
Node: construct (i.e. statement or loop)
Edge: construct relationship

‹#›

Call Graphs

A directed graph representing caller-callee relationship between methods/functions
Node: methods/functions
Edges: calls
Facilitates program
comprehension and
optimization.
Program crash context
Detect anomalies of program execution…





‹#›

Program Dependency Graph

A directed graph representing dependencies among code.
Contain both control dependence and data dependence edges.
– Control dependence: A control depends on B if B’s execution decides whether or not A is executed
– Data dependence: A data depends on B if A uses variable defined in B

‹#›

Program Dependency Graph (cont.)

TODO: Which statement(s) does “z = x + y;” depend on? What about “x = y + x;”?

int x = 1;
int y = 2;
while (x > 0) {
x = y + x;
}
z = x + y;













‹#›

Tokenization

‹#›

Tokenization (cont.)



‹#›

Tokenization (cont.)

‹#›

Tokenization



‹#›

Dynamic Analysis

The investigation of the properties of a
running software system.
Loggers, debuggers, etc.
Why dynamic analysis?
Gap between run-time and code structure
Collect runtime execution information
Finds bugs in application
Allows for program transformation, optimization
Modify program behaviors on the fly

‹#›

How to do dynamic analysis?

Instrumentation
Modify code or runtime to monitor specific components in a system and collect data
Instrumentation approaches:
Source code modification
Byte code modification
VM modification

‹#›

Source Code Modification

Given a program’s source code, how can we modify the code to record which method is called by main() in what order?

public class Test {
public static void main(String[] args) {
if (args.length == 0) return;
if (args.length % 2 == 0) printEven();
else printOdd();
}
public static void printEven() {System.out.println(“Even”);}
public static void printOdd() {System.out.println(“Odd”);}
}

‹#›

Source Code Instrumentation

Call site instrumentation: Call print(...) before each method call
Method entry instrumentation: Call print(...) at entry of each method

public class Test {
public static void main(String[] args) {
if (args.length == 0) return;
if (args.length % 2 == 0) printEven();
else printOdd();
}
public static void printEven() {
System.out.println(“printEven() is called”);
System.out.println(“Even”);
}
public static void printOdd() {
System.out.println(“printOdd() is called”);
System.out.println(“Odd”);
}
}

public class Test {
public static void main(String[] args) {
if (args.length == 0) return;
if (args.length % 2 == 0) {
System.out.println(“printEven() is called”);
printEven();
} else {
System.out.println(“printOdd() is called”);
printOdd();
}
}
public static void printEven() {System.out.println(“Even”);}
public static void printOdd() {System.out.println(“Odd”);}
}

‹#›

What does all this have to do with SE?

Not much for day-to-day activities…
Development tools! Many tools use these techniques to automate and support software engineering work.
static analysis tools, dynamic analysis tools, debuggers, code optimizers, linters, test runners, CI/CD build tools, memory management, logging, stack trace and error reporting, configuration, test case generation, automated program repair, bots,...

‹#›

AI in SE



AI in SE (cont.)



Discussion

Find a partner to discuss the following questions:
Do you use AI tools for writing code? If so, which one(s) and how?
How likely do you think it is that AI will replace human programmers?

‹#›

Brief History

AI for Code Generation in Pre-LLM era:
2016: Code summarization
2019: Code search, better summarization
Code completion tools used smaller-scale version of current code generation processes!

[Luan]

2020: Beta version of GPT-3
2021: Initial Codex model and data
2023: GPT-4, GitHub Copilot

Motivations For and Against Usage



[Liang]

Large Language Models

AI code generation is possible due to recent advancements in machine learning, generative AI, and NLP:
LLMs are trained on billions of input tokens
Natural language, code, etc.
Allows models to learn patterns
Reasoning capabilities, but not actual reasoning
Models can interpret input prompts, then predict the next token to generate code.

How does AI code generation work?

Step 1: Write a prompt
User: 🙋‍♂️ "Write a Python function to calculate the factorial of a number."
Step 2: Tokenization
Input: "Write a Python function to calculate the factorial of a number."
Tokens: ["Write", "a", "Python", "function", "to", "calculate", "the", "factorial", "of", "a", "number", "."]
Step 3: Prediction Loop
LLM 🤖 (Hmm…Python functions usually start with “def”)
LLM: 🧠 "def"
LLM: 🧠 "def" + "factorial"
LLM: 🧠 "def factorial" + "("
LLM: 🧠 "def factorial(" + "n"
LLM: 🧠 "def factorial(n)" + ":"...
Step 4: Attention/Refinement
Step 5: Code Generation

[Gemini- “Explain how llm code generation works”]

AI Code Generation Approaches

LLM Code Generation: Conversational, predict tokens based on patterns in data
Agentic AI: Autonomous AI-powered agents break down complex tasks
Augmented Generation: Inject context from knowledge base into model reasoning
Fine-tuning: Aligning models to perform specific tasks based on exemplars

[Pandey]

Vibe Coding



Is there anything wrong with this?

[Review] Code-and-Fix

Based on a given a project specification:
Write code
Improve it
GOTO 1

‹#›

When should you use Code-and-Fix?
Maybe small 1-person projects and/or course assignments
Never 🛑

Vibe Coding (cont.)

Based on a given a project specification:
[AI] Writes code
[Ask AI to] Improve it
GOTO 1

‹#›

When should you use vibe coding?
Maybe small 1-person projects and/or course assignments
Never 🛑

Developer AI Sentiment and Usage



AI Sentiment and Usage (cont.)



Decrease in sentiment/trust from last year!

2.7%

40.3%

26.6%

7.9%

23.6%

48.3%

18.7%

3.0%

5.2%

1.2%

2024

2024

Developer AI Workflow



Developer AI Workflow (cont.)



Humans vs. AI

ChatGPT generates more complex and longer programs than humans [Azeem]

Open Challenges

AI lacks project context 👨‍💻
Current benchmarks are inaccurate 📊
For example, the most widely recognized benchmark (HumanEval) is:
Mostly Python,
Leetcode-style programs,
Suffers from data leakage,
Limited unit tests,...
More complex debugging and understanding 🤔
Reviewing AI code increases cognitive effort [Tang]
Security risks 🔒
45% of AI generated code contains known vulnerabilities [Veracode]
Ethical concerns (i.e., Licensing/Attribution) 📜

Class Activity

Discussion Presentation Sign-Ups
Reminder:
Each student will lead a discussion on a research paper
Class will be expected to provide a reflection based on the research topic (and participate in the discussion).
Please sign-up for one presentation slot
Select a paper in the provided topic tab
Or you can also select a different paper to present, must be approved by the instructor
More details/example in class Thursday

‹#›

http://gobble.cs.vt.edu/5704-discussion

References

RS Pressman. “Software engineering: a practitioner's approach”.
Tushar Sharma, et al. “Do We Need Improved Code Quality Metrics?”, 2020
Rachel Potvin, et al. “Why Google Stores Billions of Lines of Code in a Single Repository”. 2016
Welker, Kurt D. "The software maintainability index revisited." CrossTalk 14 (2001): 18-21.
Vukelja, Ljiljana, Lothar Müller, and Klaus Opwis. "Are engineers condemned to design? A survey on software engineering and UI design in Switzerland." Human-Computer Interaction–INTERACT 2007: 11th IFIP TC 13 International Conference, Rio de Janeiro, Brazil, September 10-14, 2007, Proceedings, Part II 11. Springer Berlin Heidelberg, 2007.
Zhang, Cheng, and David Budgen. "What do we know about the effectiveness of software design patterns?." IEEE Transactions on Software Engineering 38.5 (2011): 1213-1231.
Na Meng and Barbara Ryder
Chris Parnin
Sarah Heckman

‹#›

