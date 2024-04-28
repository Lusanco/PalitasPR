<script>
  import Navbar from "./Navbar.svelte";
  import Footer from "./Footer.svelte";
</script>

<div class="Template">
  <Navbar />
  <div class="h-full div">
    <slot />
  </div>
  <Footer />
</div>

<style>
  .Template {
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
  }
  .div {
    display: flex-column;
    justify-content: center;
    /* background-image: url("https://img.freepik.com/free-vector/hand-drawn-olive-green-background_23-2149724855.jpg?w=1380&t=st=1713812035~exp=1713812635~hmac=c58823e622ef816b6cd03ac1e976814e1c657f46ea05ad1cc40ab555d8ba23ab");
    background-repeat: no-repeat;
    background-size: cover; */
  }
</style>
