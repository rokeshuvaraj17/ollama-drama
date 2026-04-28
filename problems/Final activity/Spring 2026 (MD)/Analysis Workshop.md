[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
2/26/2026

Analysis Workshop

Sample Research Discussion
Workshop

Learning Outcomes

By the end of the course, students should be able to:
Implement a software system following the software life cycle phases
Develop software engineering skills working on a team project
Identify processes related to phases of the software lifecycle
Explain the differences between software engineering processes
Discuss research questions and studies related to software engineering
Communicate (via demo and writing) details about a developed software application

‹#›

Announcements

PM1.3
Demo slides due next Thursday (3/5) before class (12:30pm 🚨)
Report, project repo, and retrospective (individual) due next Friday (3/6) before midnight
Final Demo timing changed to 8 minutes 🚨
Next Week
Tuesday (3/3): Project Workday
Thursday (3/5): Project 1 Demos
No office hours this afternoon

‹#›

Discussion Presentations

Each student will lead a discussion on a selected research paper.
15 minutes, including presentation and class discussion components
Class will be expected to provide a reflection based on the research topic (and participate in the discussion).
If you want to pick a different paper/select one not on the list, please let the instructor know.

‹#›

Rubric



‹#›

Discussion Presentation Tips

Read the paper thoroughly, but don’t try to understand all of the details
Practice your talk ahead of time (Stay on time!)
Always start with the problem
Be creative in your discussion or activity
Grade is based on the presentation and class discussion activity
Learning Outcome:
Discuss research questions and studies related to software engineering

‹#›

Example

Program Comprehension and Code Complexity Metrics: An fMRI Study
Norman Peitek, Sven Apel, Chris Parnin, André Brechmann, Janet Siegmund
https://doi.org/10.1109/ICSE43902.2021.00056
International Conference on Software Engineering (ICSE), 2021
Presented by: Chris Brown

‹#›

Prelude

“Before going further—putting aside concerns of performance or coding style—we would like you to spend a few moments and calculate the result of compute(8, 12, 4). Based on this experience, please rate the complexity (i.e., how difficult it is to understand the parts of the code and their dependencies) of this code snippet on a 5-point scale, from Very Simple to Very Complex.”

‹#›

Example provided in the paper:

Motivation

Code quality is one of the most important factors in software development. Software engineering research has developed several complexity metrics calculated based on various structural properties of code.
From 2010-2015, 226 studies proposed or analyzed 300 code metrics
Static analysis tools calculate these metrics across programming languages

‹#›

Problem

Metric values differ considerably!

‹#›

Halstead’s complexity vocabulary size = 21
McCabe’s Cyclomatic Complexity = 4
Beyer’s DepDegree (low-level data flow) = 31
Lines of code = 7
… 

2. There is limited work exploring how these metrics impact code comprehension.

Goal: explore the relation of code complexity metrics to behavioral and cognitive correlates of program comprehension.

Background

Functional Magnetic Resonance Imaging (fMRI)

‹#›

Prior neuroscience studies investigate cognitive load and from linguistic studies on sentence complexity (more complex sentences = more cognitive load).
Does this also apply to code?

Methodology

Overview
Systematic experiment with 19 programmers analyzing 50 Java code snippets in an fMRI scanner followed by interviews.

Code Metrics 📊
Code Size (LOC)
Vocabulary (Halstead)
Control Flow (McCabe)
Data Flow (DepDegree)

Measures 🔎
Behavioral Data
Time
Correctness
Subjective Complexity
fMRI Data
Brain Activation
Brain Deactivation
Blood oxygen levels

RQs ❓
RQ1: Do different (classes of) code complexity metrics correlate with programmers’ behavior during program comprehension?
RQ2: Do different (classes of) code complexity metrics correlate with programmers’ cognitive load in terms of brain (de)activation during program comprehension?
RQ3: Do different (classes of) code complexity metrics correlate with programmers’ subjective perception of code complexity?

Results: RQ1 (Behavior)



‹#›

Participants completed all tasks, averaging 32 seconds and 72% correctness
McCabe’s complexity: no correlation with time or correctness
LOC, Halstead, and DepDegree: small correlation with response time and medium correlation with correctness

Results: RQ2



‹#›



McCabe’s complexity: no correlation with time or correctness
LOC, Halstead, and DepDegree: small to medium correlations for (de)activation



Results: RQ3 (Subjective Complexity)



‹#›



McCabe’s complexity: no correlation with subjective complexity
LOC, Halstead, and DepDegree: small correlations for subjective complexity
Subjective complexity had medium correlation with time and strong correlation with whether or not participants could correctly complete the task!



Takeaways

Advantages
Novel study design (fMRI)
Detailed implications for programming and code metrics in practice
Disadvantages
Student participants
Simple code tasks
Complex metrics and setting
Limited number of code metrics
Additional follow-up analyses on 37 other metrics

‹#›

Takeaways (cont.)

🤯 Limited cognitive impact of cyclomatic complexity
Data flow vs control flow
🤔Code size (LOC, vocabulary) is an indicator of cognitive load
🧠 LOC increases demand in one area
🧠🧠🧠 Halstead/DepDegree across multiple areas 

‹#›

Relevance

Relevance to code analysis: Code metrics are common for assessing the quality of code.
Relevance to class: The experiment incorporates several code quality metrics discussed in class. The quality of code also directly affects development and maintenance efforts.

‹#›

Questions?

‹#›

Program Comprehension and Code Complexity Metrics: An fMRI Study
Norman Peitek, Sven Apel, Chris Parnin, André Brechmann, Janet Siegmund
https://doi.org/10.1109/ICSE43902.2021.00056
International Conference on Software Engineering (ICSE), 2021
Presented by: Chris Brown

Discussion

What do you find makes code more or less difficult to comprehend?
How might these findings impact development activities in practice?
How can programming and software engineering education be improved to help students write less complex/more comprehensible code?

‹#›

Code Analysis Workshop

Find your randomly assigned activity partner.
Select one person to be the interviewer and the other to be the candidate.
The interviewer will select a problem from the Blind 75 Leetcode Questions list.
The candidate will code a solution to the problem.
Aim to come up with the most efficient solution
Explain your problem-solving approach (think-aloud)
You will not be graded on your code
The interviewer will provide feedback on the code quality (see Lecture slides) and overall interview performance.
Complete the provided survey for your role (see Canvas).
Switch roles and repeat.
There is nothing to submit on Canvas
Each student is expected to complete both surveys for attendance.
If you run out of time to complete both roles, indicate in the other survey
\* Preferred not to use AI tools, but up to each group to decide. If you do, you are expected to report which tools were used, how, and assess the quality of the generated code.

