# Cyberprofile
Survey Cyberprofile Management Web Application
This program is a web-based application developed using Flask and MySQL, designed to manage user roles and conduct surveys efficiently. It features a registration form and a login system with two-factor authentication to enhance security.


# Key Features:

# User Registration and Authentication:
  Users can register as company users, with fields such as company name, username, password, and email.
  The login system includes a two-factor authentication process, sending a verification code to the user's registered email address.

# User Roles:
  SuperAdmin: This role includes a control panel to manage all user types, modify user roles, suspend users, and manage groups. It also includes an activity log to track user actions such as login, logout, and modifications.
  Company User: These users can manage user groups, create and modify groups through Excel import or API connection, and send surveys via email to user groups. Each company user can have one or more user groups.
  General User: Created by company users, these users belong to specific groups and can access and respond to surveys. They can only change their password and answer surveys.

# Survey Management:
The SuperAdmin can create multiple surveys, each containing at least one question with multiple-choice answers.
Each question has a minimum of five response options, identified by numbers 1 through 5, allowing only one choice per question for the general user.
Surveys and responses are stored in the database for analysis and reporting.

# Reporting and Analytics:
Company users have a dashboard to view survey results graphically, displaying responses by quantity and percentage.
The dashboard also shows the completion status of users and the time taken to complete the survey.
Data can be exported to Excel, including user information and survey responses.

# Database Structure:
The MySQL database manages users, groups, surveys, questions, answers, and activity logs.
It supports the various functionalities of user management, survey distribution, and analytics.

# Responsive Design:
The application is designed to work seamlessly across different web browsers, ensuring a consistent user experience.
