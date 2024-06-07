<script>
    import List from "../DaisyComponents/DaisyList.svelte";
  
    let classUL1 = "menu menu-horizontal space-x-4 sm:space-x-8";
    let classUL2 = "menu menu-horizontal pl-3 space-x-4 sm:space-x-8";
    let linksARRAY1 = { "Terms of Use": "/terms-of-use", Privacy: "/privacy" };
    let classLINKS1 = { "Terms of Use": "menu-item", Privacy: "menu-item" };
    let linksARRAY2 = { About: "/about", Contact: "/contact", FAQ: "/faq" };
    let classLINKS2 = { About: "menu-item", Contact: "menu-item", FAQ: "menu-item" };
    let svgPath =
      "M18.266 26.068l7.839-7.854 4.469 4.479c1.859 1.859 1.859 4.875 0 6.734l-1.104 1.104c-1.859 1.865-4.875 1.865-6.734 0zM30.563 2.531l-1.109-1.104c-1.859-1.859-4.875-1.859-6.734 0l-6.719 6.734-6.734-6.734c-1.859-1.859-4.875-1.859-6.734 0l-1.104 1.104c-1.859 1.859-1.859 4.875 0 6.734l6.734 6.734-6.734 6.734c-1.859 1.859-1.859 4.875 0 6.734l1.104 1.104c1.859 1.859 4.875 1.859 6.734 0l21.307-21.307c1.859-1.859 1.859-4.875 0-6.734z";
  </script>
  
  <!-- Footer Start -->
  <footer class="hidden px-4 py-4 mt-auto text-teal-100 bg-primary md:flex">
    <div
      class="container flex flex-wrap items-center justify-center mx-auto space-y-4 sm:justify-between sm:space-y-0"
    >
      <div class="flex flex-row pr-3 space-x-4 sm:space-x-8">
        <div class="avatar placeholder">
          <div class="w-12 rounded-full bg-neutral-focus text-neutral-content">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 32 32"
              fill="currentColor"
              class="w-5 h-5 rounded-full text-neutral-content"
            >
              <path d={svgPath}></path>
            </svg>
          </div>
        </div>
        <List
          linksARRAY={linksARRAY1}
          classLINKS={classLINKS1}
          classUL={classUL1}
        />
      </div>
      <List
        linksARRAY={linksARRAY2}
        classLINKS={classLINKS2}
        classUL={classUL2}
      />
    </div>
  </footer>
  <!-- Footer End -->