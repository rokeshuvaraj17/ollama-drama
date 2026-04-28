[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
3/17/2026

‹#›

Announcements

‹#›

HW3 due Friday (3/27) before midnight
PM2.0 due next class (3/20) before midnight
Project 2 Introduction (today and Thursday)
Project Workday on Thursday
Ut Prosim Activities
Updated grades to reflect current submissions
To receive full credit, five activities must be reported in the course form
Maintenance discussions next Thursday (3/26)
Wright, Calvo, Tolley, Broerman, Chhetri

Maintenance

What is maintenance?
Types of Maintenance
Maintenance Activities

After you complete implementation, what’s next?
When software is completed, it must be:
tested to ensure it meets requirements;
deployed or delivered to the customer; and
maintained such that user problems are addressed after operationalization.
Software requires continual maintenance and testing to ensure the program operates correctly, and frequent deployments to make updates available to users.
Software Artifacts: All!

Warm-Up

Do you have experience maintaining code long-term (i.e., more than one semester or summer)?

Software Maintenance

The process of changing, modifying, and updating software to keep up with customer needs.
i.e. debugging, improving performance, new features, etc.
Maintainability: The ease with which existing software can be corrected, adapted, or enhanced after delivery. [Pressman]
The goal of software maintenance is to keep the software system working correctly, efficiently, and securely, and to ensure that it continues to meet the needs of the users.
The majority of software engineering is maintenance!

“Software engineering is creating things someone else is willing [and able] to maintain.” [Menzies]

Software Maintenance (cont.)

Problem: Time/Effort

“Understanding code is by far the activity at which professional developers spend most of their time.” – Peter Hallam, Microsoft [2006]

[Godfrey]

[Zelkowitz]

Problem: Costs

‹#›

Maintenance in Practice
IBM: 50-75% of costs
Standish: 3-4x original cost
Gartner: 55-80% of budget
[Jurkėnas]

Case Studies: Linux



[Ogheneovo]

Case Studies: Microsoft



[Ogheneovo]

Types of Software Maintenance

Corrective
Preventative
Perfective
Adaptive

[Thales]

Corrective Software Maintenance

Fixing something that goes wrong in a piece of software.
Ex.) Finding faults and errors
\* This is the most common form of software maintenance!

Preventative Software Maintenance

Predicting changes to keep software working for as long as possible.
Ex.) Upgrades, bug prevention, security updates, latent faults

Perfective Software Maintenance

Improving software to adjust to user needs and stay relevant on the market.
Ex.) Adding new features, removing less effective features

Adaptive Software Maintenance

Changing non-functional aspects of the system related to your software.
Ex.) Compatibility on new operating systems, cloud storage, hardware, policies and rules for usage

Common Maintenance Activities

Refactoring
Debugging
Code Reviews

Refactoring

The process of modifying code for improvement without changing the underlying functionality and behavior of the program.
Refactoring is not just modifying code
There are many different types of refactoring

72 refactorings introduced ed by Fowler et al.

Most Common Refactoring

[Silva]

77%!

Refactoring Example

class Gorilla {
int paws() {
return 4;
}
}

class Gorilla{
int paws(){
int pawCount = 4;
return pawCount;
}
}

INTRODUCE EXPLAINING VARIABLE

class Gorilla implements Primate {
int paws() {
int pawCount = 4;
return pawCount;
}
}
…
interface Primate {
abstract int paws();
}

EXTRACT INTERFACE

class Gorilla implements Primate{
int feet() {
int pawCount = 4;
return pawCount;
}
}
…
interface Primate {
abstract int feet();
}

RENAME METHOD

Why Refactor?

The idea behind refactoring is to acknowledge that it will be difficult to get a design right the first time!
As a program’s requirements change, the design may also need to change.
Refactoring provides techniques for evolving the design in small incremental steps.
Benefits
Often code size is reduced after refactoring
Confusing structures are transformed into simpler structures
Which are easier to maintain and understand

Floss vs. Root Canal Refactoring 

Describes when refactoring is done and why.
The distinction will help you: 🦷
Identify the tools that will be most useful to you
Figure out whether your refactoring is “best practice”
[Parnin][Murphy-Hill]

Root Canal Refactoring

Large changes to software code.
Painful, expensive, the result of long periods of neglect
When: Refactoring for protracted periods; time specifically set aside
Why: Typically after code has gotten difficult to maintain
Not considered best practice ✘

Floss Refactoring

Smaller and more frequent code changes
Easier to do, regular, something software engineers know they should do
When: Continuously
As often as “every few minutes”
Why: It helps achieve an immediate goal (to “clean up” or “improve” is not a goal)
Considered best practice ✅

Debugging

The process of finding and fixing errors in code.
This is widely regarded as the most expensive and time-consuming part of SE! [Alaboudi]



Debugging (cont.)

Debugging activities

Code Reviews

The process of manually inspecting source code changes.
Human code analysis (also known as peer code reviews)
Usually performed by a developer other than the author
Goal: Inspect code before integration to improve software quality.

Why Code Reviews?



[Bacchelli]

Code Reviews in Industry

Code reviews are a very common industry practice.
Made easier by advanced tools that:
integrate with configuration management systems
highlight changes (i.e., diff function)
allow traversing back into history

Project 2

\*

“Software engineering is creating things someone else is willing [and able] to maintain.” [Menzies]

Modern software engineering is largely about maintaining and evolving existing software systems. While Project 1 focused on forming requirements and designing a software product, Project 2 will focus on maintaining and extending an existing application.

Project 2 Guidelines

For Project 2, you have ~eight weeks to maintain and extend an application developed during Project 1. For this assignment, students:
Must understand and analyze an existing codebase;
Must track work in progress and planned tasks in a GitHub project and/or GitHub issues;
Must implement at least two enhancements to the codebase—one from the original team and one proposed by the Project 2 team;
Must complete assigned maintenance and testing activities;
Must complete a demo presentation of the updated system;
Must work in an assigned group;
May use Generative AI tools to support implementation and maintenance (adhering to the class and team-specific AI policies).

Project 2 Milestones

There will be Four major milestones for Project 2:

‹#›

PM2.0: Project Introduction (due 3/20)
PM2.1: Development Sprint I (due 4/3)
PM2.2: Development Sprint II (due 4/17)
PM2.3: Development Sprint III (due 5/1)
PM2.4: Final Presentation (due 5/9\*)
\* presentation slides due before class (1:05pm) on deadline date!

Class Activity

Work together with your Project 2 group to complete a comprehensive code review of your project codebase.
Sample rubric

‹#›

Project groups and repos should be available on Canvas.
This is required for the PM2.0 submission.
Submit on Canvas (only one person needs to submit)

References

Abdulaziz Alaboudi et al. “An exploratory study of debugging episodes”. 2017
RS Pressman. “Software engineering: a practitioner's approach”.
Martin Fowler, Kent Beck, John Brant, William Opdyke, and Donald Roberts, “Refactoring: Improving the Design of Existing Code”, 1999.
Tim Menzies. “Class takes software ideas from development to pitch”. CSC News, 2023. NC State.
Michael W. Godfrey and Qiang Tu. “Evolution in Open Source Software: A Case Study”. International Conference on Software Maintenance. IEEE, 2000.
Danilo Silva et al. “Why We Refactor? Confessions of GitHub Contributors”. 2016
Ruchika Malhotra and Anuradha Chug, “Software Maintainability: Systematic Literature Review and Current Trends”, 2016.
Marvin V. Zelkowitz, Alan C. Shaw, and John D. Gannon. “Principles of Software Engineering and Design”. Prentice-Hall, 1979.
Edward E. Ogheneovo. “On the Relationship between Software Complexity and Maintenance Costs”. Journal of Computer and Communications, 2014.
The Thales Group. “The 4 Types of Software Maintenance”.
Rokas Jurkėnas. “The true cost equation: Software development and maintenance costs explained”. Idea Link, 2026. https://idealink.tech/blog/software-development-maintenance-true-cost-equation
Emerson Murphy-Hill. “How we Refactor, and How We Know It”. 2012
Chris Parnin
Code Reviews lecture, University of Washington.

