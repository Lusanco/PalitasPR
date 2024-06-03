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
      <Route path="/create-request" component={CreateRequest} />
      <Route path="/create-request-success" component={CreateRequestSuccess} />
      <Route path="/manage-services" component={ManageServices} />
      <Route path="/manage-requests" component={ManageRequests} />
      <Route path="/profile" component={Profile} />
      <Route path="/about" component={About} />
      <Route path="/contact" component={Contact} />
      <Route path="/faq" component={Faq} />
    </Router>
  </Main>
  <Footer />
</div>
