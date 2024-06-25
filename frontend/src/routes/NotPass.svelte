<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";

  onMount(() => {
    axios
    .get("/api/user/status")
    .then((userStatusRes) => {
      userSession.set(true);
      console.log(userStatusRes.data);
    })
    .catch((userStatusErr) => {
      userSession.set(false);
      console.log(userStatusErr);
      console.log($userSession);
    })
  })
  

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
