# PalitasPR

<div align="center">
  <img src="https://github.com/Lusanco/PalitasPR/blob/development/pre-main/frontend/public/logoLight.svg" alt="PalitasPR logo"/>
</div>

<!-- Table of contents -->
### Table of contents

- [Description](#description)
- [Usage](#usage)
- [Frontend](#frontend)
- [Backend](#backend)
- [Cloud](#cloud)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Learn more about the project](#learn-more-about-the-project)
- [Credits](#credits)

<!-- Description -->
<h1>Description</h1>

PalitasPR is a platform designed to simplify the connection between service providers and requesters in Puerto Rico. Finding and promoting services online can be challenging due to outdated platforms and the overwhelming noise on social media. Our platform streamlines this process by offering a fast, reliable, and user-friendly solution.

## Project Overview
  
- Frontend: Built with Svelte for a reactive, efficient user interface, styled using Tailwind CSS and DaisyUI, with Vite as the build tool.
- Backend: Powered by Python Flask, handling requests and server-side logic.
- Database: Structured with PostgreSQL for robust and scalable data management.
- Cloud Services: Originally deployed using AWS (RDS, S3, EC2) for hosting and scalability.

### Note

This project is no longer hosted but remains accessible on GitHub for review and reference.

<!-- Usage --> 
<h1>Usage</h1>


<!-- Frontend --> 
<h3>Frontend</h3>

<h4> Svelte installation using Vite </h4>

```bash
npm create vite@latest <project-name>
```

##

<h4> TailwindCSS Installation </h4>

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

<h4> TailwindCSS Config </h4>

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

<h5>Global CSS Tailwind imports</h5>

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

##

<h4> DaisyUI Installation </h4>

```bash
npm i -D daisyui@latest
```

<h4> DaisyUI Config </h4>

```js
module.exports = {
  //...
  plugins: [
    require('daisyui'),
  ],
}

```

##

<h4> Running the project </h4>

```bash
npm run dev # runs the project in development mode
```

<!-- Backend -->
<h2>Backend</h2>

<h3> Main App </h3>
The <b>Main App</b> is the core of our platform, utilizing the Flask framework for a seamless connection between the frontend and backend. It features a modular blueprint structure for organized routing and API management. With SQLAlchemy and PostgreSQL, we handle data efficiently, supporting C.R.U.D. operations and custom queries. The application serves static files, including Svelte-generated JavaScript and CSS, ensuring a dynamic user interface. AWS S3 integration allows secure image uploads and retrievals. Key components include app.py for app initialization, base_model.py and models.py for database schema, console.py for command-line database operations, and emails.py for managing email communications. This setup ensures a robust and scalable backend infrastructure.

<h3> SQLAlchemy and Postgres </h3>
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

<h3> S3 Bucket With the App </h3>
Our application seamlessly integrates with AWS S3 for managing pictures. When uploading or retrieving pictures, we leverage Boto3, the AWS SDK for Python, to interact with our S3 bucket. For uploads, the app sends requests to S3, storing pictures securely in the cloud. When retrieving pictures, we generate presigned URLs using Boto3, granting temporary access to specific objects in our S3 bucket. These presigned URLs are then provided to the frontend, enabling clients to fetch and display pictures dynamically. This approach ensures efficient storage, retrieval, and display of images while maintaining security and scalability.

<div align="center">

<h2> Backend Files Structure </h2>


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


  
</div>

<!-- Cloud -->
<h1>Cloud</h1>

<h3>Deployment</h3>

<h4> How is it Deployed?</h4>
Our deployment strategy revolves around leveraging AWS services for robust and scalable hosting. We've secured our domain, palitaspr.com, using Amazon Route 53 and obtained an SSL/TLS certificate from AWS Certificate Manager (ACM). This certificate ensures secure communication over HTTPS.

The core of our infrastructure is managed by an Elastic Load Balancer (ELB), which distributes incoming traffic across multiple EC2 instances, but in the case of this demo project only to one. These instances are configured with a Linux server environment running Gunicorn and Nginx. Gunicorn serves as the WSGI server, handling Python web application requests the main `app.py`, while Nginx acts as a reverse proxy server, enhancing performance by caching and serving static content.

Our ELB is configured to target a group of EC2 instances, where listeners on ports 80 (HTTP) and 443 (HTTPS) are redirected to our palitaspr.com EC2 instance.

<div align="center">

<h2> Cloud Files Structure</h2>

| AWS Instance                                         | Usage                                                                        |
| -------------------------------------------------- | --------------------------------------------------------------------------------- | 
| _RDS_                      | Hosting Postgres Database                         |
| _EC2_ | Virtual machine using linux with gunicorn and nginx to run server |
| _ELB_ | Load balancer to redirect traffic from http and https into EC2 intance |
| _S3_ | Bucket for handling pictures of the app and its users|
| _Route-53_ | Used to obtain domain 'palitaspr.com'|
| _ACM_ | Certification(SSL) from ACM to use https safely in our load balancer'|

</div>

<!-- Screenshots -->
# Screenshots

### Home page | Search
<div align="center">
  
  ![Search](https://palitaspr.netlify.app/images/searchIndex.png)
  
</div>

##

### Service details
<div align="center">
  
  ![Service details](https://palitaspr.netlify.app/images/serviceDetails.png)
  
</div>

##

### Profile page
<div align="center">
  
  ![Profile page](https://palitaspr.netlify.app/images/profile.png)
  
</div>

<!-- Learn more about the project -->
# Learn more about the project

<br />

<div align="center">

  ### Take a look at our [landing page](https://palitaspr.netlify.app/) and learn more about PalitasPR!

</div>

<br />

<!-- Credits -->
<h1>Credits</h1>

<div align="center">

| Members          | Roles | Links                               |
|------------------|-------|-------------------------------------|
| Antonio de Jesus | Database Manager | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/antonio-de-jesus-santiago-851890296/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/antoniofdjs) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:antoniofdjs@gmail.com) |  
| Jonathan Perez   | Frontend-Mobile Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prodjohnper) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/prodjohnper) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:prodjohnper@gmail.com) 
| Livan Hernandez  | Frontend Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/livan-hernandez-baba4a190/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/livanhernandez) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:livanhernandez9@gmail.com) 
| Louis Toro       | Backend Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/louis-s-toro-rosario-32b8088a/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ltoro9) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:louistororosario@gmail.com) 
| Luis Santiago    | Lead Developer | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lusanco/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lusanco) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lasc1026@gmail.com) 

</div>

##

<br />

<div align="end">

  [Back to top ↑](#palitaspr)
  
</div>
