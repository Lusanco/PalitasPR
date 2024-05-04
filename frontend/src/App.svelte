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
  import ContactUs from "./components/ContactUs.svelte";

  // Import Test Component
  import Pagination from "./components/Pagination.svelte";

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
      <Route path="/contact" component={ContactUs} />

      <!-- Route  Test Components -->
      <!-- <Route path="/components" component={Pagination} /> -->
    </Router>
  </Main>
  <Footer></Footer>
</div>
