<script>
  import axios from "axios";
  import { onMount } from "svelte";

  onMount(() => {
    axios
      .get("/api/user/logout")
      .then((loginRes) => {
        console.log("Logout Success!", loginRes.data);
      })
      .catch((loginError) => {
        console.log("Logout Error", loginError);
      });
  });
</script>
