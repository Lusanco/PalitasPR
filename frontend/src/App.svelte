<script>
  // Svelte Routing Library
  import { Router, Route } from "svelte-routing";

  // PalitasPR Layouts
  import Header from "./layouts/Header.svelte";
  import Main from "./layouts/Main.svelte";
  import Footer from "./layouts/Footer.svelte";

  // PalitasPR Routes
  import Index from "./routes/Index.svelte";
  import LoginToContinue from "./routes/LoginToContinue.svelte";
  import Login from "./routes/Login.svelte";
  import Signup from "./routes/Signup.svelte";
  import SignupSuccess from "./routes/SignupSuccess.svelte";
  import Dashboard from "./routes/Dashboard.svelte";
  import CreateService from "./routes/CreateService.svelte";
  import CreateServiceSuccess from "./routes/CreateServiceSuccess.svelte";
  import CreateRequest from "./routes/CreateRequest.svelte";
  import CreateRequestSuccess from "./routes/CreateRequestSuccess.svelte";
  import ManageServices from "./routes/ManageServices.svelte";
  import ManageRequests from "./routes/ManageRequests.svelte";
  import Profile from "./routes/Profile.svelte";
  import About from "./routes/About.svelte";
  import Contact from "./routes/Contact.svelte";
  import Faq from "./routes/FAQ.svelte";
  import Inbox from "./routes/Inbox.svelte";
  import ServiceDetails from "./routes/ServiceDetails.svelte";
  import RequestDetails from "./routes/RequestDetails.svelte";
  import ServiceOffers from "./routes/ServiceOffers.svelte";
  import NotFound from "./routes/NotFound.svelte";
  import TermsOfUse from "./routes/TermsOfUse.svelte";
  import Privacy from "./routes/Privacy.svelte";
  import Test from "./routes/TEST.svelte";
  import InitialContactSuccess from "./routes/InitialContactSuccess.svelte";

  // Agreement Routes
  import Agreement from "./routes/Agreement.svelte";
  import AgreementReview from "./routes/AgreementReview.svelte";
</script>

<div class="flex flex-col min-h-screen">
  <Header />
  <Main>
    <Router>
      <Route path="/" component={Index} />
      <Route path="/login-to-continue" component={LoginToContinue} />
      <Route path="/login" component={Login} />
      <Route path="/signup" component={Signup} />
      <Route path="/signup-success" component={SignupSuccess} />
      <Route path="/dashboard" component={Dashboard} />
      <Route path="/create-service" component={CreateService} />
      <Route path="/create-service-success" component={CreateServiceSuccess} />
      <Route path="/service-details/:id" component={ServiceDetails} />
      <Route path="/create-request" component={CreateRequest} />
      <Route path="/create-request-success" component={CreateRequestSuccess} />
      <Route path="/request-details/:id" component={RequestDetails} />
      <Route path="/manage-services" component={ManageServices} />
      <Route path="/manage-requests" component={ManageRequests} />
      <Route path="/profile" component={Profile} />
      <Route path="/about" component={About} />
      <Route path="/contact" component={Contact} />
      <Route path="/faq" component={Faq} />
      <Route path="/404" component={NotFound} />
      <Route path="/terms-of-use" component={TermsOfUse} />
      <Route path="/privacy" component={Privacy} />
      <Route
        path="/initial-contact-success"
        component={InitialContactSuccess}
      />

      <!--* Agreement routes -->
      <Route path="/agreement" component={Agreement} />
      <Route path="/agreement-review" component={AgreementReview} />

      <!--! 404 / Not found -->
      <Route path="*" component={NotFound} />

      <!-- Test Route -->
      <Route path="/test" component={Test} />
      <Route path="/agreement" component={Agreement} />
    </Router>
  </Main>
  <Footer />
</div>
