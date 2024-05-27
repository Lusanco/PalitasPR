<script>
  import { Router, Route } from "svelte-routing";
  import Index from "./routes/Index.svelte";
  import Login from "./routes/Login.svelte";
  import Signup from "./routes/Signup.svelte";
  import About from "./routes/About.svelte";
  import Contact from "./routes/Contact.svelte";
  import Header from "./components/Header.svelte";
  import Main from "./components/Main.svelte";
  import Footer from "./components/Footer.svelte";
  import SignupSuccess from "./routes/SignupSuccess.svelte";
  import Profile from "./components/Profile.svelte";
  import Faq from "./components/FAQ.svelte";
  import NotFound from "./components/NotFound.svelte";
  import LoadingSpinnerFull from "./components/LoadingSpinnerFull.svelte";
  import UploadImage from "./components/UploadImage.svelte";
  import PromotionsRequests from "./components/Promotions_Requests.svelte";
  import CreatePromotionRequest from "./components/CreatePromotion.svelte";
  import CreatePromotion from "./components/CreatePromotion.svelte";
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
      <Route path="/profile" component={Profile} />
      <Route path="/faq" component={Faq} />
      <Route path="/404" component={NotFound} />
      <Route path="/upload" component={UploadImage} />
      <Route path="/promotions-requests" component={PromotionsRequests} />
      <Route path="/create-promotion" component={CreatePromotion} />
    </Router>
  </Main>
  <Footer />
</div>
