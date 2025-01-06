# Section 1 : General Knowledge

# 1. Explain the difference between black-box, white-box, and gray-box testing. Provide a scenario where each type would be most applicable. 

**Black-box** is a testing approach where testing is done with no knowledge of the application's internal structure under test. It mainly focuses on valid and invalid inputs and outputs while observing the outcomes. The testing is also called behavioral testing usually done from the end-user perspective. 

**Scenario**:-  Testing a login form by providing both valid and invalid credentials to check on the authentication behavior

**White-box** on the other hand involves testing the workings and structure of a software application. The tester has access to the design document and source code and uses the knowledge to check on the correctness of the application on the code level.

**Scenario**: - Assuming you are working with savings accounts, you can test the loop logic that calculates the interest on the savings accounts to ensure it iterates the correct number of times.

Lastly, we have **Gray-box** testing that combines both black-box and white-box testing to find defects in an application. In this case, the tester has limited knowledge of how the components being tested work. It ensures that the testing done reflects the users' and potential attackers' experience.

**Scenario**:-Test a file upload feature where you know the maximum size limit, but you try and upload a file whose size exceeds the required size limit to see the outcome.

# 2. What are the key components of a Test Plan? Provide an example of each. 

A Test plan is a document that outlines the approach, resource, scope, and schedule for testing a software application. The test plan components include:- 

**Testing deliverables**:- A list of documents or reports that should be delivered after testing such as **test summary reports and test cases**.

**Test schedule**:- this outlines the timelines and milestones for the testing activities such as **testing should be done between 6th January 2025- 11th January 2025, and we should be able to cover the authentication flow**.

**Test objectives**:- define the goals and objectives of the testing, for example:-**Identifying defects by finding and documenting bugs, errors, and other issues in an application**.

# 3. Describe how you would approach testing a React Native application that supports both iOS and Android. 

To test React Native applications for both iOS and Android, we have two primary methods:- Manual testing and Automated testing.

Manual testing:- involves manually executing test cases to evaluate the application’s functionality and efficiency. I mainly simulate the user journey to check if the application works as expected or if there are bugs detected. Automated testing:- Involves writing test scripts and running them on different devices. 

Using a framework such as Appium that acts as a bridge between the test scripts and the mobile device.  Here are the steps:-

           Send test commands to the Appium server as JSON objects
           The server translates the commands to platform-specific- commands and executes them on the devices.
           Appium locates items using different mechanisms such as buttons on the devices
           Appium then performs actions on the specific locations e.g clicking on text
           The Appium server receives responses from the device interaction
           Test results are sent to client to be used to verify the expected behavior.






