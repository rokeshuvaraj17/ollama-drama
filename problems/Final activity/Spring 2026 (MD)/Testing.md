[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
3/24/2026

‹#›

Announcements

‹#›

HW3 due Friday (3/27) before midnight
PM2.1 due next Friday (4/3) before midnight
Development Sprint I
Instructor Travel: 4/13-4/17
No in-person class
Project Workday
Workshop
Maintenance discussions next Thursday (3/26)
Wright, Zhang, Tolley, Broerman, Chhetri

Presentation Rubric



‹#›

Project 2 Questions

‹#›

Will unit tests be required for maintenance and testing activities? [Yes]
What other tests besides unit tests will be required? [None required]
If we feel a feature is counterproductive or unintuitive can we remove it to improve the overall quality; Can we remove features that are already implemented if they contradict our vision for the app or do we need to work within the established code base? [Yes, would need to justify]
For the maintenance and testing portion of the assignment, should we be implementing our own tests or using the testing provided by the original codebase and ensuring it still works properly? [Implement your own tests for new features, can re-use (and add to) existing tests if modifying existing features]
Is creating a GitHub issue for each feature we add sufficient for this guideline: “Must track work in progress and planned tasks in a GitHub project and/or GitHub issues”? [Yes]
Does the enhancement have to be one of each (bug fix, feature) or can it be two of one? [Can be multiple of one]

Testing

Types of Testing
Test Cases
LLMs for Testing

Testing

Goal: Execute software with intent of finding errors
• While you can’t test until there is code to run, you can start planning testing when you’re analyzing the requirements
• Includes Unit (Ut) and System (St) tests to verify code and functionality
• Software Artifacts: test code, bug database, test database, test inputs and outputs, documentation

What is Testing?

Testing is the process of exercising a program with the specific intent of finding errors prior to delivery to the end user.
Discovery: Executing a program or system with the intent of finding errors. [Myers].
Verify: Any activity aimed at evaluating an attribute or capability of a program or system and determining that it meets its required results. [Hetzel]

Testing Process



Testing Software is Hard

Hardware: If you are testing a bridge’s ability to sustain weight and you test it with 1000 tons, you can infer that it will sustain 1000 tons
However, this kind of reasoning does not work for software systems
software systems are not linear nor continuous
testing all possible input/output combinations is too expensive
the number of test cases increases exponentially with the number of input/output variables

Testing Software is Hard (cont.)

Exhaustive testing
Random testing

int max(int x, int y) {
if (x > y)
return x;
else
return y;
}

Number of possible test cases (assuming 32 bit integers)
-232 \* 232 = 264

Coverage is problematic
i.e., If we pick test cases randomly it is unlikely that we will pick a case where x = y
Non-uniform distribution
When to stop?

Who should test software?



Ideally, both

Types of Testing

Black Box Testing: ignores the internals of the program and focuses on functionality.
White Box Testing: uses code to guide testing.





Black Box Testing

Focus on I/O behavior
If for any given input, we can predict the output, then the component passes the test.
Requires a test oracle
Reduce test cases by using equivalence classes and boundary value analysis
Define a partition of the input domain

Equivalence Classes

Minimize the number of test cases while choosing representatives from different equivalence classes.
Ex) Given a program that checks if a number is even or odd, example equivalence classes could include:
D1 = {x is even}, D2 = {x is odd}, D3 = {x 0}, D4={x > 0}
On one extreme, you can make each equivalence class one element which turns into exhaustive testing. On the other hand, choosing a whole input domain as an equivalence class will use only one test case!

Ex) Test set: {x=48, x=-23} covers all classes!

Boundary Value Analysis

Similar concept to equivalence classes.
Testing values around boundaries with conditional statements.

…
Scanner console = new Scanner(System.in);
System.out.print("Enter a month: ");
int num = console.nextInt();
if (num >= 1 && num <= 12) {
...

Ex) possible test set: {0, 1, 2, 11, 12, 13}

White Box Testing

Use code to motivate testing
Most popular: unit testing
Unit: individual functions or methods
Assert Statements: Used to programmatically verify the expected output matches the actual output
Assertion libraries differ based on testing framework, programming language, etc.

Assert Statements Example

public static String evenOdd(int num) {
if (num == 0 || num == 2 || num == 4 || num == 6 || num == 8) {
return "Even";
} else {
return "Odd";
}
}

1. assertEquals("The expected output is Even", "Even", evenOdd(6));
2. assertEquals("The expected output is Odd", "Odd", evenOdd(1));
3. assertEquals("The expected output is Even", "Even", evenOdd(10));
4. assertTrue("The expected output is Odd", "Odd".equals(evenOdd(99));
5. assertFalse("The expected output is Even", evenOdd(8).equals("Even"));

Given the code above, will the following (JUnit) test cases pass or fail?

// PASS
// PASS
// FAIL
// PASS
// FAIL

White Box Testing (cont.)

Measure for minimum number of unit tests…
Cyclomatic Complexity!
Reminder: Number of independent paths in a program
Cyclomatic Complexity = #decisions + 1

Cyclomatic Complexity Review

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

Testing Metrics

The best case would be to execute all paths through the code, but there are some problems with this:
the number of paths increases fast with the number of branches in the program
the number of executions of a loop may depend on the input variables and hence may not be possible to determine
most of the paths can be infeasible

Coverage Metrics

Statement coverage: all statements in the programs should be executed at least once
Branch coverage: all branches in the program should be executed at least once
Path coverage: all execution paths in the program should be executed at least once

Example

The following test set will give us statement and branch coverage:
T1={(x=12,y=5), (x= -1,y=35), (x=115,y=-13),(x=-91,y=-2)}
The following test set will give us statement and branch coverage with less test cases:
T2 = {(x=12,y=-5), (x= -1,y=35)}
What about path coverage?

areTheyPositive(int x, int y)
{
if (x >= 0)
print(“x is positive”);
else
print(“x is negative”);
if (y >= 0)
print(“y is positive”);
else
print(“y is negative”);
}

Example (cont.)

What about path coverage?

areTheyPositive(int x, int y)
{
if (x >= 0)
print(“x is positive”);
else
print(“x is negative”);
if (y >= 0)
print(“y is positive”);
else
print(“y is negative”);
}

T2 {(x = 12, y = -5), (x = -1, y = 35)} only executes paths: (B0,B1,B3,B5,B6) and (B0,B2,B3,B4,B6). T1 executes all paths, statements, and branches.

Path set:
[(B0,B1,B3,B4,B6); (B0,B1,B3,B5,B6); (B0,B2,B3,B4,B6); (B0,B2,B3,B4,B6)]

Example 2

T1 = {x=-1} will give statement coverage.
What about branch/path coverage?

absoluteValue(int x)
{
if (x < 0)
x = -x
return x;
}

T1 only executes one branch and path (B0, B1, B2). Path (B0, B2) is missing!
How about T2 = {(x=-1), (x=35)}?
This covers all paths, branches, and statements!
Moral: Minimizing test cases reduces time, but also potentially reduces coverage!

Writing Test Cases

Test case: Specific functionality or feature to test
Required test case information for all test cases:
Unique Identifier
Input
Expected Output
Actual Results

Black Box Test Cases



White Box Test Cases











Testing Strategies

Begin by “testing-in-the-small” and move toward “testing-in-the-large”:
Unit Testing
Integration Testing
Validation Testing
System Testing

Strategy 1: Unit Testing

What are you testing: Individual components on the smallest unit of software design (function, class, or subsystem)
Who?: Carried out by developers
Goal: Confirm that units are correctly coded and information flows in and out of modules properly.

Strategy 2: Integration Testing

What are you testing?: Groups of subsystems, and eventually the entire system
Who?: Carried out by developers (mostly, could also be testers)
Goal: To construct tests to uncover errors associated with interfacing between units

Strategy 3: Validation Testing

Also known as acceptance testing
What are you testing?: the system delivered by developers
Who?: Carried out by testers and/or clients (through typical product interactions on a trial basis)
Goal: Demonstrate that the system meets requirements and is ready to use

Strategy 4: System Testing

What are you testing?: The entire system
Who?: Developers and/or testers
Goal: Determine if the system meets the requirements (functional and nonfunctional)
How is this different from validation testing?
Not from the user’s perspective

Automated Testing

Testing: Software engineers have long desired methods to automate software testing.





LLMs can accelerate automated testing with more context understanding…

AI for Testing: Benefits

LLMs can generate syntactically valid tests, often improving code coverage.

[Wang]

AI for Testing: Case Study

Automated Unit Test Improvement using Large Language Models at Meta [Alshahwan]

“TestGenLLM verifies that its generated test classes successfully clear a set of filters that assure measurable improvement over the original test suite, thereby eliminating problems due to LLM hallucination…In an evaluation on Reels and Stories products for Instagram, 75% of TestGen-LLM’s test cases built correctly [and] 57% passed reliably…During Meta’s Instagram and Facebook test-a-thons, it improved 11.5% of all classes to which it was applied, with 73% of its recommendations being accepted for production deployment by Meta software engineers. 

AI for Testing: Challenges

However, LLM-generated tests can be:
Irrelevant
Testing useless or redundant test cases for the sake of improving code coverage
Difficult to benchmark
LLMs perform significantly worse on large codebases with real-world code, overfit to metrics
Unit-testing-centric
Inconsistent
flaky
Expensive
Prioritize Java/Python
…

Class Activity

Complete the following with your Project 2 group:
Identify three test cases for your Project 2 application.
Write a black box test plan describing three test cases to assess the system using the template in the slides:
Submit the test plan for attendance on Canvas [you may work together and submit once per group, but note who is in attendance].
Due: before the end of the day (submit whatever you complete)

‹#›

This column should be blank!

References

Nadia Alshahwan, et al. “Automated Unit Test Improvement using Large Language Models at Meta”. Arxiv https://arxiv.org/pdf/2402.09171
Tevfik Bultan. “272: Software Engineering; Lecture 10: Testing; Automated Testing”. 2008.
Wenhan Wang, et al. “TESTEVAL: Benchmarking Large Language Models for Test Case Generation”. Association for Computational Linguistics, NAACL 2025. https://aclanthology.org/2025.findings-naacl.197.pdf
RS Pressman. “Software engineering: a practitioner's approach”.
Ruchika Malhotra and Anuradha Chug, “Software Maintainability: Systematic Literature Review and Current Trends”, 2016.
Code Reviews lecture, University of Washington.

