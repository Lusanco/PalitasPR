
<p align="center">
  <img src="https://github.com/Lusanco/PalitasPR/blob/development/pre-main/frontend/public/logoLight.svg" />
</p>

<hr>

<h3>Table of contents</h3>

- [Description](#description)
- [Usage](#usage)
- [Frontend](#frontend)
- [Backend](#backend)
- [Cloud](#cloud)
- [Deployment](#deployment)
- [Credits](#credits)


<h1>Description</h1>

  PalitasPR is a service requests - promotions platform born from the need of a fast and reliable service requests - promotions system. We all know that finding jobs/services online as a contractor or as a person who needs to contract a servicer it's almos impossible. Between almost-dead platforms and the load of congestion that we can find in social media, everyday, searching or promoting a service gets more difficult. Our team worked with multiple technologies to bring you the best user experience. 
  
  Our frontend, made with the Javascript framework [Svelte](https://svelte.dev/), our CSS framework [TailwindCSS](https://tailwindcss.com/), the UI library [DaisyUI](https://daisyui.com/). Our backend, made with [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/3.0.x/). Our database, made in [PostgreSQL](https://www.postgresql.org/) and loaded into our cloud service. Our Cloud based in [AWS](https://aws.amazon.com/). All of this tools and technologies together, make our app as efficient and as reliable as it is.

<h1>Usage</h1>

<h2>Frontend</h2>

<h3> Running the Project </h3>

```bash
npm run dev
```

- Svelte is a modern JavaScript framework that enables building fast and reactive user interfaces with less code.

<h4> Svelte installation </h4>

```bash
npm create vite@latest <project-name>
```

- TailwindCSS is a utility-first CSS framework that provides low-level utility classes to build custom designs without leaving your HTML.

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

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

- DaisyUI is a plugin for TailwindCSS that provides a set of beautifully designed, fully customizable UI components.

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

<h3> Project Structure </h3>

```
Root Directory

index.html: Main HTML file.
package.json: Project metadata and dependencies.
tailwind.config.js: Configuration for TailwindCSS.

Public Directory

images/members: Contains member images.
Alfre.jpg
Antonio.jpg
Jonathan.jpg
Livan.jpg
Louis.jpg
logoDark.svg, logoLight.svg: Project logos.
manifest.json: Web app manifest.

Main Files
app.css: Global styles.
App.svelte: Main Svelte component. Acts as the root component, orchestrating the structure and behavior of the app.
```


<h3> Components </h3>


```
Reusable UI components:

Button.svelte: Custom button component.
Card.svelte: A card component used for displaying information in a card layout.
List.svelte: A list component for displaying lists of items.
Loading.svelte: A loading spinner component to indicate loading states.
Member.svelte: Displays member information.
Menu.svelte: Navigation menu component.
OfferCard.svelte: Displays offer details.
OriginalButton.svelte: Another button variant with different styles.
QR.svelte: QR code generator component.
ReviewCard.svelte: Displays review details.
Slogan.svelte: Component to display the application's slogan.
Team.svelte: Displays team members' information.
```

<h3> Layouts </h3>

```
Layout components:

Footer.svelte: The footer section of the layout.
Header.svelte: The header section of the layout.
Main.svelte: The main content area of the layout.
```

Routes

```
Page components for different routes:

About.svelte: About page.
Agreement.svelte: Agreement details page.
AgreementReview.svelte: Review agreement details.
Contact.svelte: Contact page.
CreateRequest.svelte: Form to create a new request.
CreateRequestSuccess.svelte: Success message after creating a request.
CreateReview.svelte: Form to create a new review.
CreateReviewSuccess.svelte: Success message after creating a review.
CreateService.svelte: Form to create a new service.
CreateServiceSuccess.svelte: Success message after creating a service.
Dashboard.svelte: User dashboard with various functionalities.
EmailSuccess.svelte: Email success notification page.
FAQ.svelte: Frequently Asked Questions page.
Inbox.svelte: User inbox for messages.
Index.svelte: Landing page.
InitialContactSuccess.svelte: Initial contact success message.
Login.svelte: Login page.
LoginToContinue.svelte: Prompt to login to continue.
ManageRequests.svelte: Page to manage user requests.
ManageServices.svelte: Page to manage user services.
NotFound.svelte: 404 Not Found page.
Privacy.svelte: Privacy policy page.
Profile.svelte: User profile page.
RequestDetails.svelte: Detailed view of a request.
RequestOffers.svelte: View offers for a request.
Review.svelte: Detailed view of a review.
ServiceDetails.svelte: Detailed view of a service.
ServiceOffers.svelte: View offers for a service.
Signup.svelte: Signup page.
SignupSuccess.svelte: Signup success message.
Tasks.svelte: User tasks management page.
TermsOfUse.svelte: Terms of use page.
Scripts
currentPage.js: Handles current page state.
servicesID.js: Manages service IDs.
stores.js: Contains Svelte stores.
teamMembers.js: Manages team members data.
townsID.js: Manages towns IDs.
utils.js: General utility functions.
```

<h2>Backend</h2>

- <h3> Main App </h3>
  EXAMPLE FIX The **Main App** serves as the backbone of our project, seamlessly integrating with the frontend through the `static` folder, which hosts the built assets generated by Svelte. These assets include optimized JavaScript and CSS files that enhance the user experience. Within the app, we've implemented robust routes that the frontend utilizes to fetch data from various APIs. This architecture ensures efficient communication between the user interface and backend, facilitating dynamic content delivery and smooth interaction throughout the platform. EXAMPLE FIX

- <h3> SQLAlchemy and Postgres </h3>
  Our application relies on SQLAlchemy, an ORM (Object-Relational Mapping) tool, to interact with our PostgreSQL database efficiently. SQLAlchemy simplifies database operations by mapping Python objects to database tables and handling queries through Python methods.

  While SQLAlchemy encourages using relationships defined in models for data retrieval, we occasionally opt for custom SQL queries executed directly from the database session. This approach allows us to optimize performance for specific queries that may be more efficient when tailored directly to our database schema and requirements. In some cases, bypassing ORM relationships has proven faster and more effective, especially for complex data retrieval operations.

  This hybrid approach ensures flexibility in managing our database interactions, balancing the convenience of ORM with the performance benefits of custom SQL queries where necessary.

- <h3> S3 Bucket With the App </h3>
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

  <h1>Cloud</h1>

- <h3>Deployment</h3>

  <h4> How is it Deployed?</h4>
  Our deployment strategy revolves around leveraging AWS services for robust and scalable hosting. We've secured our domain, palitaspr.com, using Amazon Route 53 and obtained an SSL/TLS certificate from AWS Certificate Manager (ACM). This certificate ensures secure communication over HTTPS.

  The core of our infrastructure is managed by an Elastic Load Balancer (ELB), which distributes incoming traffic across multiple EC2 instances, but in the case of this demo project only to one. These instances are configured with a Linux server environment running Gunicorn and Nginx. Gunicorn serves as the WSGI server, handling Python web application requests(the main `app.py`, while Nginx acts as a reverse proxy server, enhancing performance by caching and serving static content.

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
