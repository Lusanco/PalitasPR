<script>
    import { onMount } from "svelte";
    import { link } from "svelte-routing";
    import axios from "axios";
  
    let password, confirmPassword, errorMessage, email = "";
    let accEmail = "livanhernandez9@gmail.com";
  
    async function handleSignup() {
      if (password !== confirmPassword) {
        errorMessage = "Passwords do not match!";
        return; // Prevent unnecessary API call
      }
  
      const data = {
        first_name: "N/A",
        last_name: "N/A",
        email: email,
        password: password,
      };
  
      // let user = JSON.stringify(data);
      axios
        .post("/api/create_object", data)
        // .get("https://jsonplaceholder.typicode.com/users")
        .then((response) => {
          console.log(response);
          // Update the UI with success message
          errorMessage = `You have successfully created an account with the following email: ${email}`;
          // Add another line with a link to login
          errorMessage += "<br> To continue, login with your account, click below!";
        })
        .catch((error) => {
          console.log(error);
          errorMessage = error;
        });
    }
  
    onMount(() => {
      errorMessage = ""; // Clear any previous error messages on component mount
    });
  </script>
      <div class="flex flex-col items-center justify-center h-full max-w-lg p-6 m-auto text-teal-800 rounded-md sm:p-10">
        <div class="mb-8 text-center">
          <h1 class="my-3 text-3xl font-bold text-wrap">Account created succesfully</h1>
          <!-- <p class="px-6 mt-2 text-sm text-center text-teal-600">Account email address:</p> -->
          <div class="p-3 m-2 mt-4 rounded-lg bg-slate-300">
          <p class="text-lg text-teal-600">{accEmail}</p>
        </div>
        <p class="px-6 mt-3 text-sm text-center">
            To continue, login to your account
          </p>
          <p class="px-6 pt-4 text-sm text-center text-teal-600">
            <button type="button" class="px-8 py-3 font-semibold text-white bg-teal-600 rounded-md hover:bg-teal-800"><a use:link href="/login" rel="noopener noreferrer" role="button">Login</a></button>
          </p>
        </div>
  </div>
  