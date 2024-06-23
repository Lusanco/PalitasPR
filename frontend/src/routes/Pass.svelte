<script>
  import axios from "axios";
  import { onMount } from "svelte";

  onMount(() => {
    axios
      .get("/api/user/login?af1=jd123@gmail.com&af2=pwd1")
      .then((loginRes) => {
        console.log("Login Success!", loginRes.data);
      })
      .catch((loginError) => {
        console.log("Login Error", loginError);
      });
  });
</script>
