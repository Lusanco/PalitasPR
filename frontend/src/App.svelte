<script>
  // Svelte Routing Library
  import { Router, Route } from "svelte-routing";

  // PalitasPR Layouts
  import Header from "./layouts/Header.svelte";
  import Main from "./layouts/Main.svelte";
  import Footer from "./layouts/Footer.svelte";

  // PalitasPR Routes
  import Index from "./routes/Index.svelte";
  import Login from "./routes/Login.svelte";
  import Signup from "./routes/Signup.svelte";
  import SignupSuccess from "./routes/SignupSuccess.svelte";
  import About from "./routes/About.svelte";
  import Contact from "./routes/Contact.svelte";
  import ConfirmLogin from "./routes/ConfirmLogin.svelte";

  // PalitasPR Components
  // import PromoteService from "./components/PromoteService.svelte";

  // PalitasPR Testing Imports
  import Dashboard from "./routes/Dashboard.svelte";
</script>

<div class="flex flex-col">
  <Header />
  <Main>
    <Router>
      <Route path="/" component={Index} />
      <Route path="/login" component={Login} />
      <Route path="/signup" component={Signup} />
      <Route path="/signup-success" component={SignupSuccess} />
      <Route path="/about" component={About} />
      <Route path="/contact" component={Contact} />
      <!-- <Route path="/promote-service" component={PromoteService} /> -->

      <!-- Testing Layout/Route/Component Currently Work On -->
      <Route path="/test" component={Dashboard} />
    </Router>
  </Main>
  <Footer />
</div>
