<script>
  import axios from "axios";
  import { onMount } from "svelte";

  onMount(() => {
    axios
      .get("/api/user/login?af1=jd123@gmail.com&af2=pwd1")
      .then((axiosResponse1) => {
        console.log(".then() Login Log: ", axiosResponse1.data);
        return axios.get("/api/user/status");
      });
  });
</script>
