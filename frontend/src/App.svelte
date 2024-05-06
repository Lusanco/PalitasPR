<script>
  import axios from "axios";
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

  // Import Test Component
  import Pagination from "./components/Pagination.svelte";
  import UploadImage from "./components/UploadImage.svelte";

  let searchInput = document.getElementById("search-input");
  let townInput = "All"; // No default town selected
  let services = []; // Array to store fetched services
  let errorMessage = ""; // Added to store error messages
  let switcher = false;

  async function handleSearch() {
    const data = {
      Service: {
        name: searchInput,
        town: townInput,
      },
    };

    axios
      .post("/api/filter", data)
      // .get("https://jsonplaceholder.typicode.com/users")
      .then((response) => {
        services = response.data;
        // console.log(services);

        // Loop through each service in the response
        for (const serviceId in services) {
          const service = services[serviceId];

          switcher = true;
        }
      })
      .catch((error) => {
        console.log(error);
        errorMessage = error;
      });
  }
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

      <!-- Route  Test Components -->
      <!-- <Route path="/components" component={Pagination} /> -->
      <!-- <Route path="/components" component={UploadImage} /> -->
    </Router>
  </Main>
  <Footer></Footer>
</div>
