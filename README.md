<p align="center">
    <img src="https://d22wxe17x1tv7t.cloudfront.net/portalinterno.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">PORTAL INTERNO MSS</h1></p>
<p align="center">
	<em>Empower Your Projects with port_mss_action: Streamline, Secure, and Scale!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Maua-Dev/port_mss_action?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Maua-Dev/port_mss_action?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Maua-Dev/port_mss_action?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Maua-Dev/port_mss_action?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#overview)
- [ Features](#features)
- [ Project Structure](#project-structure)
  - [ Project Index](#project-index)
- [ Getting Started](#getting-started)
  - [ Prerequisites](#prerequisites)
  - [ Installation](#installation)
  - [ Usage](#usage)
  - [ Testing](#testing)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)
- [ Contributors](#contributors)
- [ Especial Thanks](#especial-thanks)

---

##  Overview

The Portal Interno MSS project streamlines Infrastructure as Code (IaC) development by automating AWS CDK deployment, managing dependencies, and simplifying testing workflows. Key features include dynamic environment-based deployment, seamless integration with AWS services, and efficient testing setups. Ideal for IaC developers and teams seeking streamlined deployment and testing processes.

---

##  Features
### Clean Architecture  🧼🏰

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li></ul> |
| 📄 | **Documentation** | <ul><li>Primary Language: Python</li><li>Language Counts: txt - 3, py - 116, bat - 1, json - 1, yml - 5</li><li>Package Managers: pip - requirements-dev.txt, iac/requirements.txt, iac/requirements-dev.txt</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Dependencies: github_actions, docker, pip, repo_owner.yml, create_pr.yml, docker-compose.yml, cdk.json, source.bat, requirements-dev.txt, python, ci.yml, cd.yml, requirements.txt, pytest-cov, boto3, python-dotenv, pytest</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li></ul> |
| 🧪 | **Testing**       | <ul><li>Test Commands: Using `pip` - pytest</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li></ul> |
| 🛡️ | **Security**      | <ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Fact 1</li><li>Fact 2</li><li>Fact 3</li></ul> |

---

##  Project Structure

```sh
└── port_mss_action/
    ├── .github
    │   └── workflows
    ├── README.md
    ├── iac
    │   ├── .gitignore
    │   ├── README.md
    │   ├── __init__.py
    │   ├── adjust_layer_directory.py
    │   ├── app.py
    │   ├── cdk.json
    │   ├── iac
    │   ├── local
    │   ├── requirements-dev.txt
    │   ├── requirements.txt
    │   └── source.bat
    ├── requirements-dev.txt
    ├── src
    │   ├── __init__.py
    │   ├── modules
    │   └── shared
    └── tests
        ├── __init__.py
        ├── modules
        └── shared
```


###  Project Index
<details open>
	<summary><b><code>PORT_MSS_ACTION/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/requirements-dev.txt'>requirements-dev.txt</a></b></td>
				<td>- Facilitates testing and development by specifying required dependencies<br>- Ensures seamless integration of pytest, pytest-cov, boto3, and python-dotenv for efficient testing and development workflows within the project architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- iac Submodule -->
		<summary><b>iac</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/app.py'>app.py</a></b></td>
				<td>- Orchestrates AWS CDK deployment based on environment variables, adjusting layer directories for Lambda functions<br>- Determines deployment stage based on GitHub branch name and sets relevant tags<br>- Creates an AWS CloudFormation stack with specified configurations and tags.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/requirements.txt'>requirements.txt</a></b></td>
				<td>Define dependencies for AWS CDK and Constructs library in the requirements file to manage infrastructure as code for the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/source.bat'>source.bat</a></b></td>
				<td>- Enables activation of a Python virtualenv on Windows by running a batch script<br>- Simplifies the process and eliminates the need for separate documentation on Windows-specific virtualenv activation commands.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/cdk.json'>cdk.json</a></b></td>
				<td>Enables configuration settings for AWS CDK, ensuring secure and efficient deployment across AWS and AWS China regions.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/requirements-dev.txt'>requirements-dev.txt</a></b></td>
				<td>Define testing dependencies for the infrastructure as code project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/adjust_layer_directory.py'>adjust_layer_directory.py</a></b></td>
				<td>- The code file `adjust_layer_directory.py` facilitates adjusting the directory structure for Infrastructure as Code (IaC) projects<br>- It handles copying shared directories to a specified destination, ensuring the correct structure for Lambda layers<br>- This functionality streamlines the organization and deployment of resources within the project architecture.</td>
			</tr>
			</table>
			<details>
				<summary><b>local</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/local/docker-compose.yml'>docker-compose.yml</a></b></td>
						<td>Facilitates local DynamoDB setup for development environment using Docker Compose.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>iac</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/iac/bucket_stack.py'>bucket_stack.py</a></b></td>
						<td>- Defines AWS S3 buckets and CloudFront distributions for member and project photos based on the environment<br>- Manages access policies and caching strategies for secure and optimized content delivery.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/iac/dynamo_stack.py'>dynamo_stack.py</a></b></td>
						<td>- Creates DynamoDB tables with specified attributes, indexes, and removal policies based on the environment<br>- Exports removal policies for actions and members with dynamic names.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/iac/lambda_stack.py'>lambda_stack.py</a></b></td>
						<td>- Generates Lambda functions for API Gateway integration, handling various CRUD operations for projects, members, and actions<br>- Manages permissions for DynamoDB, SES, and S3 based on function requirements within the project's serverless architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/iac/iac/iac_stack.py'>iac_stack.py</a></b></td>
						<td>- Defines infrastructure for a REST API with AWS services like Cognito, DynamoDB, S3, and Lambda functions<br>- Manages environment variables, CORS settings, and permissions for various functions<br>- Integrates user authentication and authorization using Cognito User Pools.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<details>
				<summary><b>modules</b></summary>
				<blockquote>
					<details>
						<summary><b>delete_action</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_action/app/delete_action_controller.py'>delete_action_controller.py</a></b></td>
										<td>- Handles the deletion of an action by validating parameters, processing the request, and returning the appropriate response based on the outcome<br>- The controller interacts with the use case to delete the action, constructs a view model, and responds with success or error messages as needed.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_action/app/delete_action_presenter.py'>delete_action_presenter.py</a></b></td>
										<td>- Implements a Lambda handler for deleting actions, integrating with controllers and use cases<br>- Retrieves repositories for actions and members from the environment<br>- Parses incoming Lambda request data and processes it through the delete action controller, returning a formatted Lambda response.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_action/app/delete_action_viewmodel.py'>delete_action_viewmodel.py</a></b></td>
										<td>Defines view models for actions and deletion actions, facilitating data transformation for the frontend.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_action/app/delete_action_usecase.py'>delete_action_usecase.py</a></b></td>
										<td>- Implements the Delete Action Usecase, handling the deletion of an action based on user permissions and ownership<br>- Validates user registration, active status, and authorization to delete the action<br>- Ensures only the action owner or an admin can perform the deletion operation.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>create_member</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_member/app/create_member_presenter.py'>create_member_presenter.py</a></b></td>
										<td>- Generates Lambda HTTP responses for creating a new member in the system<br>- Orchestrates the flow between the HTTP request, member creation use case, and controller<br>- Handles the event data and context to process the request and return the appropriate response.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_member/app/create_member_controller.py'>create_member_controller.py</a></b></td>
										<td>- Handles the creation of a new member by validating and processing incoming data<br>- If all required parameters are present and valid, it creates a new member entity, generates a view model, and returns a successful response<br>- Handles various error scenarios gracefully, providing appropriate error messages for missing parameters, duplicate items, and other issues.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_member/app/create_member_usecase.py'>create_member_usecase.py</a></b></td>
										<td>- Implements a use case to create a new member in the system, ensuring uniqueness of user ID<br>- Converts member details to title case and timestamps the hiring date.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_member/app/create_member_viewmodel.py'>create_member_viewmodel.py</a></b></td>
										<td>- Transforms member data into a structured dictionary for creating a new member<br>- The code encapsulates the member details and generates a formatted output for the creation process, ensuring consistency and ease of use within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>delete_project</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_project/app/delete_project_viewmodel.py'>delete_project_viewmodel.py</a></b></td>
										<td>- The `delete_project_viewmodel.py` file defines classes to represent and serialize project data for deletion<br>- It encapsulates project details and formats them into a dictionary for deletion confirmation messages<br>- This file plays a crucial role in managing project data during deletion operations within the codebase architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_project/app/delete_project_controller.py'>delete_project_controller.py</a></b></td>
										<td>- Handles the deletion of a project by validating parameters, executing the deletion process, and returning the appropriate response based on the outcome<br>- The controller interacts with the use case to delete the project, constructs a view model, and responds with success or error messages as needed.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_project/app/delete_project_usecase.py'>delete_project_usecase.py</a></b></td>
										<td>- Implements a use case to delete a project, ensuring the user has the necessary permissions and the project exists<br>- It interacts with repositories to handle the deletion process securely within the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_project/app/delete_project_presenter.py'>delete_project_presenter.py</a></b></td>
										<td>- Handles the deletion of projects by orchestrating the communication between the controller and use case<br>- Retrieves necessary data from the request, processes the deletion, and constructs the appropriate response for the Lambda function.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>update_action</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action/app/update_action_presenter.py'>update_action_presenter.py</a></b></td>
										<td>- Handles HTTP requests to update actions by interfacing with repositories and executing the necessary business logic through a controller<br>- The code orchestrates the flow by processing incoming data, invoking the appropriate use case, and generating a response for the client.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action/app/update_action_viewmodel.py'>update_action_viewmodel.py</a></b></td>
										<td>- UpdateActionViewModel encapsulates the logic to transform an Action object into a dictionary representation for updating actions<br>- It serves as a bridge between the Action entity and the presentation layer, ensuring a clean separation of concerns within the codebase architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action/app/update_action_usecase.py'>update_action_usecase.py</a></b></td>
										<td>- Implements the Update Action Usecase, handling updates to action details based on specified parameters<br>- Validates user permissions and ensures data integrity by updating associated members and start date accordingly.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action/app/update_action_controller.py'>update_action_controller.py</a></b></td>
										<td>- Handles updating action details based on user input, validating and processing data to create a new action entity<br>- Utilizes a structured approach to ensure data integrity and consistency, returning a view model with the updated action information<br>- Handles various error scenarios gracefully, providing appropriate responses for different types of issues encountered during the update process.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>get_history</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history/app/get_history_presenter.py'>get_history_presenter.py</a></b></td>
										<td>- Handles the retrieval of historical data by orchestrating interactions between the controller, use case, and repositories<br>- Parses incoming Lambda requests, enriches them with user information, and generates appropriate HTTP responses for the API endpoint.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history/app/get_history_viewmodel.py'>get_history_viewmodel.py</a></b></td>
										<td>- Generates a view model for historical actions, encapsulating user, time, and project details<br>- Converts actions to dictionaries for easy serialization, including stack and action type tags<br>- Handles pagination with a last evaluated key for efficient retrieval.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history/app/get_history_controller.py'>get_history_controller.py</a></b></td>
										<td>- Handles retrieving user history based on specified parameters, validating input data, and returning the appropriate response<br>- Parses and processes user requests, ensuring data integrity and error handling<br>- The controller orchestrates the use case to fetch actions and generates a view model for the response, handling various exceptions for different scenarios.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history/app/get_history_usecase.py'>get_history_usecase.py</a></b></td>
										<td>- Implements a use case to retrieve user actions history, handling pagination and access control based on user roles<br>- Validates user permissions and fetches relevant actions from repositories, ensuring data integrity and security within the codebase architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>create_action</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_action/app/create_action_viewmodel.py'>create_action_viewmodel.py</a></b></td>
										<td>- The code in create_action_viewmodel.py defines classes to represent and transform action data for creating new actions within the project architecture<br>- It encapsulates the necessary attributes and methods to handle the conversion of action objects into dictionary formats for further processing and messaging purposes.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_action/app/create_action_controller.py'>create_action_controller.py</a></b></td>
										<td>- Handles the creation of actions by validating and processing incoming data, then invoking the appropriate use case to create the action<br>- Returns a view model representing the created action in the response<br>- Handles various error scenarios and maps them to the corresponding HTTP status codes for proper error handling.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_action/app/create_action_presenter.py'>create_action_presenter.py</a></b></td>
										<td>- Facilitates the creation of actions by handling HTTP requests and responses through a structured flow of controller and use case interactions<br>- Integrates with external interfaces and repositories to manage action and member data effectively within the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_action/app/create_action_usecase.py'>create_action_usecase.py</a></b></td>
										<td>- Implements a use case to create an action, ensuring user permissions and data integrity<br>- Validates user registration, permission status, and creates associated actions<br>- Manages action creation and association with members, enforcing project rules and maintaining data consistency.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>get_all_projects</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_projects/app/get_all_projects_presenter.py'>get_all_projects_presenter.py</a></b></td>
										<td>- Handles the retrieval of all projects by orchestrating the communication between the controller, use case, and repositories<br>- Parses incoming Lambda requests, processes the data, and constructs the appropriate HTTP response for the client.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_projects/app/get_all_projects_controller.py'>get_all_projects_controller.py</a></b></td>
										<td>- Handles requests to retrieve projects based on specified dates and user, ensuring data integrity and user permissions<br>- Parses request data, validates types, and triggers the use case to fetch projects<br>- Converts project data into a view model for response<br>- Handles various error scenarios gracefully, returning appropriate HTTP responses.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_projects/app/get_all_projects_viewmodel.py'>get_all_projects_viewmodel.py</a></b></td>
										<td>- Transforms project data into a structured format for display<br>- The code organizes project details into a view model hierarchy, facilitating easy retrieval and presentation of multiple projects.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_projects/app/get_all_projects_usecase.py'>get_all_projects_usecase.py</a></b></td>
										<td>- Retrieve and enrich project data by fetching all projects within a specified timeframe<br>- Validate user permissions and filter projects based on user roles<br>- Calculate hours worked on each project and return the updated project list.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>update_member</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_member/app/update_member_viewmodel.py'>update_member_viewmodel.py</a></b></td>
										<td>Transforms member data into a view-friendly format for updating, encapsulating necessary fields and metadata.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_member/app/update_member_controller.py'>update_member_controller.py</a></b></td>
										<td>- Handles updating member information based on incoming requests, ensuring data integrity and type validation<br>- Utilizes a structured approach to validate and process various fields such as name, email, role, stack, year, and more<br>- Returns appropriate responses for different error scenarios, maintaining robustness and reliability in the system.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_member/app/update_member_presenter.py'>update_member_presenter.py</a></b></td>
										<td>- Handles updating member information by orchestrating the communication between the controller, use case, and repository<br>- Retrieves the requester's user information from the event context and returns the response in a standardized format.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_member/app/update_member_usecase.py'>update_member_usecase.py</a></b></td>
										<td>- Manages updating member details, ensuring data integrity and authorization<br>- Validates and processes changes based on user roles and permissions<br>- Handles exceptions and triggers email notifications for specific scenarios<br>- Maintains consistency and security in member data modifications.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>delete_member</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_member/app/delete_member_presenter.py'>delete_member_presenter.py</a></b></td>
										<td>- Handles the deletion of a member by orchestrating the communication between the controller, use case, and repository<br>- Parses incoming Lambda requests, processes the deletion operation, and constructs the appropriate Lambda response.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_member/app/delete_member_viewmodel.py'>delete_member_viewmodel.py</a></b></td>
										<td>- Transforms member data into a dictionary for deletion confirmation<br>- The code encapsulates member details and generates a structured output with a deletion message.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_member/app/delete_member_usecase.py'>delete_member_usecase.py</a></b></td>
										<td>- Implements the deletion of a member from the system based on specified conditions, ensuring that only authorized users can perform this action<br>- Handles scenarios where the user initiating the deletion is an admin or a regular user, safeguarding against unauthorized access.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/delete_member/app/delete_member_controller.py'>delete_member_controller.py</a></b></td>
										<td>- Handles the deletion of a member in the system by validating the request parameters, executing the deletion process, and returning the appropriate response based on the outcome<br>- The controller interacts with the use case and view model to manage the deletion operation and provide feedback to the user.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>update_action_validation</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action_validation/app/update_action_validation_viewmodel.py'>update_action_validation_viewmodel.py</a></b></td>
										<td>- Facilitates updating action validation status with a structured view model<br>- The code defines two classes to represent action validation data and its update, ensuring a clear separation of concerns within the codebase architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action_validation/app/update_action_validation_presenter.py'>update_action_validation_presenter.py</a></b></td>
										<td>- Handles HTTP requests, enriches them with user data, and delegates to a controller for processing<br>- Utilizes repositories to validate and update actions, ensuring proper authorization and data integrity within the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action_validation/app/update_action_validation_controller.py'>update_action_validation_controller.py</a></b></td>
										<td>- Handles updating action validation status based on user input, ensuring required parameters are present<br>- Converts data to appropriate formats, handles errors, and returns responses with corresponding HTTP status codes.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_action_validation/app/update_action_validation_usecase.py'>update_action_validation_usecase.py</a></b></td>
										<td>- Validates and updates action items based on user permissions and validity status<br>- Checks user roles and activity status before allowing updates<br>- Sends email notifications for invalid actions to associated members.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>create_project</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_project/app/create_project_controller.py'>create_project_controller.py</a></b></td>
										<td>- Handles project creation requests by validating and processing incoming data, then invoking the appropriate use case to create a new project<br>- If any required parameters are missing or errors occur during processing, it returns the corresponding HTTP error response.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_project/app/create_project_presenter.py'>create_project_presenter.py</a></b></td>
										<td>- Facilitates project creation by orchestrating interactions between the controller, use case, and repositories<br>- Handles Lambda requests, enriches data, and generates appropriate HTTP responses.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_project/app/create_project_usecase.py'>create_project_usecase.py</a></b></td>
										<td>Generates unique project codes and creates new projects, ensuring user roles, permissions, and project uniqueness are validated before persisting data.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/create_project/app/create_project_viewmodel.py'>create_project_viewmodel.py</a></b></td>
										<td>Transforms a Project into a formatted dictionary for display, encapsulating project details and creation message.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>batch_get_member</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/batch_get_member/app/batch_get_member_viewmodel.py'>batch_get_member_viewmodel.py</a></b></td>
										<td>Transforms member data into a structured format for retrieval, enabling seamless integration with the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/batch_get_member/app/batch_get_member_usecase.py'>batch_get_member_usecase.py</a></b></td>
										<td>- Implements a use case to retrieve multiple members by user IDs, ensuring they are active and registered<br>- The code interacts with a member repository to fetch and validate member data, handling errors for unregistered users or inactive members.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/batch_get_member/app/batch_get_member_controller.py'>batch_get_member_controller.py</a></b></td>
										<td>- Handles batch retrieval of member data, validating user input and returning appropriate responses based on the outcome<br>- Validates user IDs, processes the request, and constructs a view model for successful responses<br>- Handles various error scenarios like missing parameters, wrong types, and unregistered users, ensuring proper HTTP status codes are returned.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/batch_get_member/app/batch_get_member_presenter.py'>batch_get_member_presenter.py</a></b></td>
										<td>- Handles HTTP requests to retrieve member data by orchestrating the use case and controller components<br>- Parses incoming data, processes it through the controller, and constructs an HTTP response for the client.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>get_history_project</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history_project/app/get_history_project_controller.py'>get_history_project_controller.py</a></b></td>
										<td>- Handles retrieving project history based on specified parameters, validating input data, and returning the results in a structured format<br>- The controller ensures proper user authentication, parameter validation, and error handling, providing a seamless interaction between the user interface and the project history retrieval logic.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history_project/app/get_history_project_viewmodel.py'>get_history_project_viewmodel.py</a></b></td>
										<td>- Define a view model that transforms actions into a structured dictionary for retrieving project history<br>- The model encapsulates action details and handles conversion to a dictionary format, including associated members and tags.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history_project/app/get_history_project_presenter.py'>get_history_project_presenter.py</a></b></td>
										<td>- Handles the HTTP request for retrieving project history by orchestrating the interaction between the controller, use case, and repositories<br>- Parses the incoming request, processes it through the use case, and constructs the appropriate HTTP response for the client.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_history_project/app/get_history_project_usecase.py'>get_history_project_usecase.py</a></b></td>
										<td>- Implements a use case to retrieve project history, ensuring user permissions and pagination<br>- Validates user access, retrieves actions based on role, and handles pagination for historical data retrieval.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>get_member</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_member/app/get_member_controller.py'>get_member_controller.py</a></b></td>
										<td>- Handles incoming requests, validates parameters, and retrieves member data using the GetMemberUsecase<br>- Converts data into a view model and returns a response based on the outcome, such as OK, BadRequest, Forbidden, or InternalServerError, ensuring proper error handling and response generation in the application.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_member/app/get_member_viewmodel.py'>get_member_viewmodel.py</a></b></td>
										<td>Transforms member data into a structured dictionary for retrieval, maintaining key attributes and values.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_member/app/get_member_usecase.py'>get_member_usecase.py</a></b></td>
										<td>- Retrieve member data, calculate hours worked, and assign projects based on user activity within specified date range<br>- Validates user ID, checks registration status, and ensures user is active before returning member details.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_member/app/get_member_presenter.py'>get_member_presenter.py</a></b></td>
										<td>- Facilitates retrieving member data by orchestrating interactions between the member repository, action repository, and the use case<br>- The presenter handles incoming HTTP requests, enriches them with user context, and delegates processing to the controller for generating an appropriate HTTP response.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>get_project</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_project/app/get_project_presenter.py'>get_project_presenter.py</a></b></td>
										<td>- Handles the retrieval of project data by orchestrating interactions between the project controller, use case, and repositories<br>- Parses incoming HTTP requests, extracts user information, and generates appropriate HTTP responses for the project retrieval operation.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_project/app/get_project_usecase.py'>get_project_usecase.py</a></b></td>
										<td>- Retrieves project details based on a provided code and user ID, ensuring the user is registered and active<br>- Validates input parameters and handles potential errors, returning the project information if found.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_project/app/get_project_viewmodel.py'>get_project_viewmodel.py</a></b></td>
										<td>Transforms project data into a structured view for retrieval, encapsulating key project details.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_project/app/get_project_controller.py'>get_project_controller.py</a></b></td>
										<td>- Handles incoming requests to retrieve project details, ensuring required parameters are present and valid<br>- Utilizes a use case to fetch project data and constructs a view model for response<br>- Handles various error scenarios and returns appropriate HTTP responses based on the outcome.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>get_all_members</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members/app/get_all_members_usecase.py'>get_all_members_usecase.py</a></b></td>
										<td>- Retrieves and processes member data based on specified criteria, including active status and admin role validation<br>- Calculates hours worked and assigns projects to members<br>- Ensures user permissions are met before returning the member data.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members/app/get_all_members_viewmodel.py'>get_all_members_viewmodel.py</a></b></td>
										<td>Converts and structures member data for retrieval, ensuring consistency and ease of use across the codebase architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members/app/get_all_members_controller.py'>get_all_members_controller.py</a></b></td>
										<td>- Handles requests to retrieve all members, validating parameters and handling errors appropriately<br>- Utilizes a use case to fetch members based on the requester's user ID, then formats the data using a view model before returning a response with the member information.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members/app/get_all_members_presenter.py'>get_all_members_presenter.py</a></b></td>
										<td>- Handles HTTP requests to retrieve all members by utilizing a controller that interacts with a use case<br>- The use case accesses member and action repositories to fetch the required data<br>- The presenter formats the response for the Lambda function, ensuring seamless communication between the client and the backend system.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>update_project</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_project/app/update_project_controller.py'>update_project_controller.py</a></b></td>
										<td>- Handles updating project details based on user input, validating and processing data to ensure accuracy<br>- Utilizes a structured approach to manage project information, interacting with external interfaces for seamless integration<br>- Returns appropriate responses for successful updates or error scenarios, maintaining data integrity throughout the process.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_project/app/update_project_presenter.py'>update_project_presenter.py</a></b></td>
										<td>- Handles updating project data by orchestrating interactions between the project repository, use case, and controller<br>- Parses incoming HTTP requests, extracts user information, and generates appropriate HTTP responses.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_project/app/update_project_viewmodel.py'>update_project_viewmodel.py</a></b></td>
										<td>- UpdateProjectViewmodel class transforms and structures project data for updates<br>- It encapsulates the logic to convert project details into a dictionary format, including a message indicating successful project updates.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/update_project/app/update_project_usecase.py'>update_project_usecase.py</a></b></td>
										<td>- UpdateProjectUsecase class handles updating project details based on user input<br>- It validates user permissions, project existence, and member associations before making updates through repositories<br>- This code ensures data integrity and security within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>get_all_members_admin</b></summary>
						<blockquote>
							<details>
								<summary><b>app</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members_admin/app/get_all_members_admin_presenter.py'>get_all_members_admin_presenter.py</a></b></td>
										<td>- Handles the Lambda function for retrieving all members in the admin panel by orchestrating the necessary components like controllers, use cases, and repositories<br>- The code integrates with external interfaces for HTTP requests and responses, ensuring seamless communication within the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members_admin/app/get_all_members_admin_controller.py'>get_all_members_admin_controller.py</a></b></td>
										<td>Handles requests to retrieve all members for admin view, validating parameters and returning appropriate responses based on the outcome.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members_admin/app/get_all_members_admin_usecase.py'>get_all_members_admin_usecase.py</a></b></td>
										<td>- Generates a list of active members, their hours worked, and associated projects within a specified date range<br>- Validates user permissions and handles edge cases like no active members or empty results<br>- Integrates with repositories to fetch member and action data for comprehensive reporting.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/modules/get_all_members_admin/app/get_all_members_admin_viewmodel.py'>get_all_members_admin_viewmodel.py</a></b></td>
										<td>- Transforms member data into a structured format for admin display<br>- The code organizes member details and formats them into dictionaries for easy retrieval and presentation.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>shared</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/environments.py'>environments.py</a></b></td>
						<td>- Defines environment variables and repositories based on the application stage<br>- Determines repository implementations for actions and members<br>- Handles loading environment variables and configuring local settings<br>- Provides methods to retrieve environment settings and repositories.</td>
					</tr>
					</table>
					<details>
						<summary><b>domain</b></summary>
						<blockquote>
							<details>
								<summary><b>entities</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/entities/member.py'>member.py</a></b></td>
										<td>Defines a Member entity with essential attributes and validation methods to ensure data integrity and consistency within the project's domain model.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/entities/action.py'>action.py</a></b></td>
										<td>- Defines a structured entity for actions within the project, enforcing data integrity and consistency<br>- Validates and stores essential details such as user ID, dates, duration, and project information<br>- Implements methods to ensure the correctness of action attributes like titles, descriptions, and associated members.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/entities/associated_action.py'>associated_action.py</a></b></td>
										<td>- Defines an entity for an associated action with validation checks for action ID, start date, and user ID<br>- The class ensures data integrity and consistency for associated actions within the project's domain entities.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/entities/project.py'>project.py</a></b></td>
										<td>- Defines a Project entity with attributes like code, name, and description<br>- Validates user IDs and project code length<br>- Allows changing Product Owner and Scrum Master user IDs<br>- Handles photo validation and provides methods for comparison and representation.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>repositories</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/repositories/member_repository_interface.py'>member_repository_interface.py</a></b></td>
										<td>- Defines an interface for member repository operations, including creating, deleting, updating, and retrieving members<br>- Also supports batch operations and sending active member emails.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/repositories/action_repository_interface.py'>action_repository_interface.py</a></b></td>
										<td>- Defines an interface for interacting with actions, projects, and associated actions<br>- It outlines methods for creating, updating, and deleting actions and projects, as well as retrieving associated actions by user ID or project code<br>- Additionally, it includes functionality for managing action durations and sending notifications.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>enums</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/enums/course_enum.py'>course_enum.py</a></b></td>
										<td>Defines course enums for various engineering disciplines in the project's shared domain.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/enums/stack_enum.py'>stack_enum.py</a></b></td>
										<td>Defines stack categories for different project domains.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/enums/role_enum.py'>role_enum.py</a></b></td>
										<td>Defines role enums for various team positions in the project's shared domain.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/enums/action_type_enum.py'>action_type_enum.py</a></b></td>
										<td>Defines action types for various activities within the project, such as coding, meetings, code reviews, learning, presentations, design, architecture, and work.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/domain/enums/active_enum.py'>active_enum.py</a></b></td>
										<td>Defines active status states for the domain, such as ACTIVE, FREEZE, DISCONNECTED, and ON_HOLD.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>infra</b></summary>
						<blockquote>
							<details>
								<summary><b>external</b></summary>
								<blockquote>
									<details>
										<summary><b>dynamo</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/external/dynamo/dynamo_table.py'>dynamo_table.py</a></b></td>
												<td>- Facilitates interaction with DynamoDB tables by managing the connection and providing access to the specified table<br>- This class abstracts the setup and teardown logic required to work with DynamoDB, enhancing the codebase's modularity and maintainability.</td>
											</tr>
											</table>
											<details>
												<summary><b>datasources</b></summary>
												<blockquote>
													<table>
													<tr>
														<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/external/dynamo/datasources/dynamo_datasource.py'>dynamo_datasource.py</a></b></td>
														<td>- The `dynamo_datasource.py` file in the project's architecture serves as a crucial component for interacting with DynamoDB tables<br>- It encapsulates functionality for managing data sources, including defining the partition and sort keys<br>- By leveraging the boto3 library, this code file enables seamless communication with DynamoDB tables, ensuring efficient data retrieval and manipulation within the system.</td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/external/dynamo/datasources/mock_db.py'>mock_db.py</a></b></td>
														<td>Manages a list of classes for the DynamoDB mock database in the shared infrastructure.</td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/external/dynamo/datasources/manual_upload_database.py'>manual_upload_database.py</a></b></td>
														<td>- Improve data integrity by identifying and handling duplicates in the DynamoDB table<br>- The code initializes a DynamoDB datasource, retrieves data, and performs a batch write operation<br>- Additionally, it includes a function to identify duplicate records based on specified keys.</td>
													</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>repositories</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/repositories/load_action_mock_to_dynamo.py'>load_action_mock_to_dynamo.py</a></b></td>
										<td>- Initialize and load mock data into DynamoDB for the project's action and project entities<br>- The code sets up a DynamoDB table, then populates it with mock data for actions, projects, and associated actions<br>- This process ensures a local DynamoDB instance is ready for testing or a real DynamoDB instance for production use.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/repositories/member_repository_mock.py'>member_repository_mock.py</a></b></td>
										<td>- Manages a mock repository for members, allowing creation, deletion, retrieval, and updating of member information<br>- Implements methods to handle member data and send active member emails.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/repositories/load_member_mock_to_dynamo.py'>load_member_mock_to_dynamo.py</a></b></td>
										<td>- Initialize and load mock data into a DynamoDB table for the project's member repository<br>- The code sets up the DynamoDB table and populates it with mock member data using a DynamoDB client and repository classes<br>- This process ensures the availability of test data for the member repository in a local or real DynamoDB environment.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/repositories/action_repository_dynamo.py'>action_repository_dynamo.py</a></b></td>
										<td>- The code file `action_repository_dynamo.py` in the `src/shared/infra/repositories` directory serves as an implementation of the Action Repository Interface within the project architecture<br>- It facilitates the interaction with a DynamoDB datasource to handle actions, associated actions, members, and projects<br>- This file encapsulates the logic for storing and retrieving data related to actions, ensuring seamless communication with the underlying data storage while maintaining consistency with the project's domain entities.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/repositories/member_repository_dynamo.py'>member_repository_dynamo.py</a></b></td>
										<td>- Manages member data in DynamoDB, including creation, retrieval, update, and deletion operations<br>- Handles member photo uploads to S3 with presigned URLs<br>- Sends email notifications for member activation<br>- Implements methods for batch retrieval and updating member details.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/repositories/action_repository_mock.py'>action_repository_mock.py</a></b></td>
										<td>- The code file `action_repository_mock.py` serves as a mock implementation of an action repository interface within the project's architecture<br>- It defines data structures for projects, actions, and associated actions, mimicking the behavior of a real repository<br>- This file plays a crucial role in providing a simulated environment for testing and development purposes, enabling seamless integration of actions within the project's ecosystem.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>dto</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/dto/associated_action_dynamo_dto.py'>associated_action_dynamo_dto.py</a></b></td>
										<td>Converts data between AssociatedAction and DynamoDB formats, facilitating seamless interaction with the database layer.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/dto/member_dynamo_dto.py'>member_dynamo_dto.py</a></b></td>
										<td>- Defines a data transfer object (DTO) for a member entity, facilitating conversion to and from a DynamoDB-compatible format<br>- Enables seamless interaction between the application's domain entities and the underlying data storage layer.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/dto/project_dynamo_dto.py'>project_dynamo_dto.py</a></b></td>
										<td>Converts project data between DynamoDB format and entity objects, facilitating seamless integration within the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/dto/user_api_gateway_dto.py'>user_api_gateway_dto.py</a></b></td>
										<td>Converts user data from the API Gateway to a standardized DTO object for seamless integration within the project's infrastructure.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/infra/dto/action_dynamo_dto.py'>action_dynamo_dto.py</a></b></td>
										<td>- Defines a data transfer object (DTO) for actions in the project, facilitating conversion between different data representations<br>- The DTO encapsulates essential action details and provides methods for conversion to and from DynamoDB-compatible formats<br>- This abstraction streamlines data handling and ensures consistency across the system.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>helpers</b></summary>
						<blockquote>
							<details>
								<summary><b>enum</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/enum/http_status_code_enum.py'>http_status_code_enum.py</a></b></td>
										<td>Defines HTTP status codes as an Enum for easy reference and consistency across the codebase.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>errors</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/errors/controller_errors.py'>controller_errors.py</a></b></td>
										<td>Define custom error classes for handling missing parameters, wrong type parameters, and wrong file types in the controller_errors module, enhancing error management in the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/errors/base_error.py'>base_error.py</a></b></td>
										<td>Defines a base error class to handle custom error messages across the codebase architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/errors/domain_errors.py'>domain_errors.py</a></b></td>
										<td>Define custom domain errors for better error handling in the project's shared helpers.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/errors/usecase_errors.py'>usecase_errors.py</a></b></td>
										<td>- Define custom error classes for specific scenarios like no items found, duplicated items, forbidden actions, user permissions, and invalid pagination amounts<br>- These classes enhance error handling and provide clear feedback within the codebase architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>external_interfaces</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/external_interfaces/external_interface.py'>external_interface.py</a></b></td>
										<td>- Defines abstract classes for request and response interfaces to standardize external interactions within the project architecture<br>- This code file establishes a clear structure for handling data and status codes in external interfaces, promoting consistency and ease of integration across various components.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/external_interfaces/http_lambda_requests.py'>http_lambda_requests.py</a></b></td>
										<td>- The code file in src/shared/helpers/external_interfaces/http_lambda_requests.py defines classes for handling HTTP requests and responses in a Lambda environment<br>- It encapsulates logic for constructing and formatting HTTP responses, including setting default headers and handling request data<br>- The classes provide a structured approach for managing communication with external interfaces in AWS Lambda functions.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/external_interfaces/http_models.py'>http_models.py</a></b></td>
										<td>- Defines HTTP request and response models with data, headers, and status code attributes<br>- Handles overlapping keys between body, query parameters, and headers<br>- Provides a structured representation of incoming and outgoing HTTP messages.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/external_interfaces/http_codes.py'>http_codes.py</a></b></td>
										<td>- Define standard HTTP response classes for different status codes in the project's shared helpers<br>- These classes encapsulate response logic for OK, Created, No Content, Bad Request, Internal Server Error, Not Found, Conflict, Redirect, and Forbidden responses, enhancing code readability and maintainability.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>utils</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/utils/compose_invalid_action_email.py'>compose_invalid_action_email.py</a></b></td>
										<td>Generates an invalid action email message by composing a customized HTML template with member and action details.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/src/shared/helpers/utils/compose_member_active_email.py'>compose_member_active_email.py</a></b></td>
										<td>- Generates an HTML email message to notify a member of their system activation status<br>- Incorporates member's name dynamically into the message template.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/.github/workflows/REPO_OWNER.yml'>REPO_OWNER.yml</a></b></td>
						<td>- Implements a workflow that checks and approves the owner of a repository on pull request reviews for specified branches<br>- It leverages a reusable CI workflow file from the `maua-dev/ci_workflows_reusable` repository to streamline the process.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/.github/workflows/CI.yml'>CI.yml</a></b></td>
						<td>- Automate CI/CD pipeline for testing and code coverage<br>- Run tests, generate coverage reports, and upload to Codecov using GitHub Actions<br>- Ensure Python 3.9 setup and dependencies installation before executing tests<br>- This workflow triggers on push, pull requests, and manual dispatch.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/.github/workflows/CREATE_PR.yml'>CREATE_PR.yml</a></b></td>
						<td>- Automates the creation of pull requests on specific branches by leveraging a reusable workflow file<br>- This setup streamlines the process of initiating code reviews and collaboration within the project, enhancing overall development efficiency and code quality.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Maua-Dev/port_mss_action/blob/master/.github/workflows/CD.yml'>CD.yml</a></b></td>
						<td>Automates AWS CDK deployment based on branch pushes and workflow triggers, setting up AWS credentials and deploying infrastructure with specified configurations.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with port_mss_action, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Install port_mss_action using one of the following methods:

**Build from source:**

1. Clone the port_mss_action repository:
```sh
❯ git clone https://github.com/Maua-Dev/port_mss_action
```

2. Navigate to the project directory:
```sh
❯ cd port_mss_action
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements-dev.txt, iac/requirements.txt, iac/requirements-dev.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t Maua-Dev/port_mss_action .
```




###  Usage
Run port_mss_action using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```



##  Contributing

- **💬 [Join the Discussions](https://github.com/Maua-Dev/port_mss_action/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Maua-Dev/port_mss_action/issues)**: Submit bugs found or log feature requests for the `port_mss_action` project.
- **💡 [Submit Pull Requests](https://github.com/Maua-Dev/port_mss_action/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Maua-Dev/port_mss_action
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/Maua-Dev/port_mss_action/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Maua-Dev/port_mss_action">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT License](./License).

---

## Contributors

- Bruno Vilardi - [Brvilardi](https://github.com/Brvilardi) 👷‍♂️
- Hector Guerrini - [hectorguerrini](https://github.com/hectorguerrini) 🧙‍♂️
- João Branco - [JoaoVitorBranco](https://github.com/JoaoVitorBranco) 😎
- Vitor Soller - [VgsStudio](https://github.com/VgsStudio) 🐱‍💻
- Luigi Trevisan - [LuigiTrevisan](https://github.com/LuigiTrevisan) 📺
- Mateus Capaldo - [MatCMartins](https://github.com/MatCMartins) 🔥
- Rafael Rubio - [Rubiozito](https://github.com/Rubiozito) 🐦
- Gabriel Bianconi - [GabrielBianconiconi](https://github.com/GabrielBianconiconi) 🚨
- João Pedro Soares - [joae1234](https://github.com/joae1234) 🖌️
- Rodrigo Morales - [RodrigoM2004](https://github.com/RodrigoM2004) 🛞
- Lucas Crapino - [LucasCrapino](https://github.com/LucasCrapino) 🐼
- Rafael Ruthes - [rruthes](https://github.com/rruthes) 🐨
- Thomas Boehm - [ThomassBoehm](https://github.com/ThomassBoehm) 🏈
- Leonardo Moreno - [pleomoreno](https://github.com/pleomoreno) ⚽
- Guilherme Guerreiro - [GuiGuerreiroo](https://github.com/GuiGuerreiroo) ⚒️

## Especial Thanks

- [Dev. Community Mauá](https://www.instagram.com/devcommunitymaua/)
- [Clean Architecture: A Craftsman's Guide to Software Structure and Design](https://www.amazon.com.br/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)
- [Institute Mauá of Technology](https://www.maua.br/)

---