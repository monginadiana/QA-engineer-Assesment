# Section 1 : General Knowledge

# Explain the difference between black-box, white-box, and gray-box testing. Provide a scenario where each type would be most applicable. 

**Black-box** is a testing approach where testing is done with no knowledge of the application's internal structure under test. It mainly focuses on valid and invalid inputs and outputs while observing the outcomes. The testing is also called behavioral testing usually done from the end-user perspective. 

**Scenario**:-  Testing a login form by providing both valid and invalid credentials to check on the authentication behavior

**White-box** on the other hand involves testing the workings and structure of a software application. The tester has access to the design document and source code and uses the knowledge to check on the correctness of the application on the code level.

**Scenario**: - Assuming you are working with savings accounts, you can test the loop logic that calculates the interest on the savings accounts to ensure it iterates the correct number of times.

Lastly, we have **Gray-box** testing that combines both black-box and white-box testing to find defects in an application. In this case, the tester has limited knowledge of how the components being tested work. It ensures that the testing done reflects the users' and potential attackers' experience.

**Scenario**:-Test a file upload feature where you know the maximum size limit, but you try and upload a file whose size exceeds the required size limit to see the outcome.



