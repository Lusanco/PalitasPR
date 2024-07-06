
<p align="center">
  <img src="https://github.com/Lusanco/PalitasPR/blob/development/pre-main/frontend/public/logoLight.svg" />
</p>

<hr>

<h3>Table of contents</h3>

- [Description](#description)
- [Usage](#usage)
- [Resources](#resources)
- [Frontend](#frontend)
- [Backend](#backend)
- [Cloud](#cloud)
- [Deployment](#deployment)
- [Credits](#credits)


<h1>Description</h1>

<p>
  PalitasPR is a service requests/promotions platform.
</p>

<h1>Usage</h1>

<h1>Frontend</h1>

<h1>Backend</h1>

| Folders & Files                                         | Content                                                                           |
| -------------------------------------------------- | --------------------------------------------------------------------------------- | 
| [_api_blueprints_](backend/api_blueprints)                         | Routes and blueprints for main flask app.py                                         |     
| [_api_documentation_](backend/api_documentation) | Routes documentation |
| [_db_](backend/db)        | Db operation files based on class model and regular C.R.U.D for database                                    |
| [_email_template_](backend/email_template)            | Template for email visual structure sent on confimation email                               |
| [_static_](models/user.py)                        | Files to serve from the frontend build via flask                                             |
| [_app.py_](backend/app.py)                        | Main Flask Aplication                                          |
| [_aws_bucket.py_](backend/aws_bucket.py)                      | S3 bucket related functions                                           |
| [_base_model.py_](backend/base_model.py)                    | Base model for all models                                          |
| [_models.py_](backend/models.py)                      | All models represeting tables on database                                           |
| [_console.py_](backend/console.py)                  | Testing console for the app                                             |
| [_emails.py_](backend/emails.py)                                  | Functions related to emails                                        |

### Main App
The **Main App** is the core of our platform, utilizing the Flask framework for a seamless connection between the frontend and backend. It features a modular blueprint structure for organized routing and API management. With SQLAlchemy and PostgreSQL, we handle data efficiently, supporting C.R.U.D. operations and custom queries. The application serves static files, including Svelte-generated JavaScript and CSS, ensuring a dynamic user interface. AWS S3 integration allows secure image uploads and retrievals. Key components include app.py for app initialization, base_model.py and models.py for database schema, console.py for command-line database operations, and emails.py for managing email communications. This setup ensures a robust and scalable backend infrastructure.

### SQLAlchemy and Postgres
Our application relies on SQLAlchemy, an ORM (Object-Relational Mapping) tool, to interact with our PostgreSQL database efficiently. SQLAlchemy simplifies database operations by mapping Python objects to database tables and handling queries through Python methods.

While SQLAlchemy encourages using relationships defined in models for data retrieval, we occasionally opt for custom SQL queries executed directly from the database session. This approach allows us to optimize performance for specific queries that may be more efficient when tailored directly to our database schema and requirements.

Database Operations are managed through the **db** folder, organized based on class models and standard CRUD operations. We use SQLAlchemy as our ORM tool to map Python objects to PostgreSQL tables. While ORM relationships are used for typical data retrieval, custom SQL queries are employed for performance optimization in specific scenarios.

**DB Operations Classes**
The following classes manage various aspects of database interactions:

- **DBOperations**: General database operations.
- **Db_promotion**: Operations related to promotions.
- **Db_use**r: User-related operations, including login and signup.
- **Db_core**: Core operations like search and filtering.
- **Db_task**: Task management operations.
- **Db_review**: Review management operations.
- **Db_promo_towns**: Promotion town mappings.
- **Db_request_towns**: Request town mappings.
- **Db_initial_contact**: Initial contact operations.
- **Db_request**: Request management operations.

These classes encapsulate the logic for interacting with the database, ensuring a clean separation of concerns and making the codebase easier to maintain and extend.

This hybrid approach ensures flexibility in managing our database interactions, balancing the convenience of ORM with the performance benefits of custom SQL queries where necessary.

### S3 Bucket With the App
Our application integrates with AWS S3 for managing pictures. When uploading or retrieving pictures, we use Boto3, the AWS SDK for Python, to interact with our bucket. For uploads, the app sends requests to S3, storing pictures securely in the cloud. When retrieving pictures, we generate presigned URLs using Boto3, granting temporary access to specific objects in our S3 bucket. These presigned URLs are then provided to the frontend, enabling clients to fetch and display pictures dynamically.

<h1>Cloud</h1>

| AWS Instance                                         | Usage                                                                        |
| -------------------------------------------------- | --------------------------------------------------------------------------------- | 
| _RDS_                      | Hosting Postgres Database                         |
| _EC2_ | Virtual machine using linux with gunicorn and nginx to run server |
| _ELB_ | Load balancer to redirect traffic from http and https into EC2 intance |
| _S3_ | Bucket for handling pictures of the app and its users|
| _Route-53_ | Used to obtain domain 'palitaspr.com'|
| _ACM_ | Certification(SSL) from ACM to use https safely in our load balancer'|


<h1>Deployment</h1>

### How is it Deployed
Our deployment strategy revolves around AWS services. We've secured our domain, palitaspr.com, using Amazon Route 53 and obtained an SSL/TLS certificate from AWS Certificate Manager (ACM). This certificate ensures secure communication over HTTPS.

The core of our infrastructure is managed by an Elastic Load Balancer (ELB), which distributes incoming traffic across multiple EC2 instances, but in the case for this demo project only to one. These instances are configured with a Linux server environment running Gunicorn and Nginx. Gunicorn serves as the WSGI server, handling Python web application requests(the main `app.py`, while Nginx acts as a reverse proxy server, enhancing performance by caching and serving static content.

Our ELB is configured to target a group of EC2 instances, where listeners on ports 80 (HTTP) and 443 (HTTPS) are redirected to our palitaspr.com EC2 instance.

<h1>Resources</h1>

<h1>Credits</h1>

<!-- [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)]
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)]
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)] -->

<div align="center">

| Members          | Roles | Links                               |                             
|------------------|-------|-------------------------------------|
| Antonio de Jesus | Database Manager | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/antonio-de-jesus-santiago-851890296/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/antoniofdjs) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:antoniofdjs@gmail.com) |  
| Jonathan Perez   | Frontend-Mobile Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prodjohnper) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/prodjohnper) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:prodjohnper@gmail.com) 
| Livan Hernandez  | Frontend Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/livan-hernandez-baba4a190/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/livanhernandez) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:livanhernandez9@gmail.com) 
| Louis Toro       | Backend Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/louis-s-toro-rosario-32b8088a/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ltoro9) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:louistororosario@gmail.com) 
| Luis Santiago    | Lead Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lusanco/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lusanco) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lasc1026@gmail.com) 

</div>
