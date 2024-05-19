<script>
  import { Router, Route } from "svelte-routing";
  import Header from "./components/Header.svelte";
  import Main from "./components/Main.svelte";
  import PageSearchBar from "./components/PageSearchBar.svelte";
  import Login from "./components/Login.svelte";
  import Footer from "./components/Footer.svelte";
  import Signup from "./components/Signup.svelte";
  import SignSuccess from "./components/SignSuccess.svelte";
  import Profile from "./components/Profile.svelte";
  import ContactUs from "./components/ContactUs.svelte";
  import AboutUs from "./components/AboutUs.svelte";
  import Faq from "./components/FAQ.svelte";
  import NotFound from "./components/NotFound.svelte";
  import LoadingSpinnerFull from "./components/LoadingSpinnerFull.svelte";
  import UploadImage from "./components/UploadImage.svelte";
  import PromotionsRequests from "./components/Promotions_Requests.svelte";
</script>

<div class="flex flex-col">
  <Header></Header>
  <Main>
    <Router>
      <Route path="/" component={PageSearchBar} />
      <Route path="/login" component={Login} />
      <Route path="/signup" component={Signup} />
      <Route path="/success" component={SignSuccess} />
      <Route path="/profile" component={Profile} />
      <Route path="/contact" component={ContactUs} />
      <Route path="/about" component={AboutUs} />
      <Route path="/faq" component={Faq} />
      <Route path="/404" component={NotFound} />
      <Route path="/upload" component={UploadImage} />
      <Route path="/promotions-requests" component={PromotionsRequests} />
    </Router>
  </Main>
  <Footer></Footer>
</div>
