<!-- REVIEWS - JOB RATING: rename/move to it appropiate place -->
<script>
    /**
     * ? User data
     */
  
    let user = {
      name: "Jane Doe",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    };
  
    let service = {
      name: "Lawn Mowing",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    };
  
    let review = `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laudantium,
            magni nisi? Repellendus sequi perspiciatis delectus esse excepturi
            laborum, labore debitis quos sunt doloribus nesciunt quia quibusdam
            sed. Culpa, corrupti nisi. Quisquam, quod. Quisquam, quod. Quisquam,
            quod. Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro quis
            fuga totam quia hic, aperiam ratione voluptates necessitatibus error iure
            sint mollitia quaerat quae excepturi obcaecati praesentium facilis sapiente
            minus!`;
  
    /**
     * ! Test functions
     */
  </script>
  
  <!-- 
    ? Container
  -->
  <div
    class="flex flex-col items-center justify-center min-h-screen p-6 md:p-12 bg-base-200"
  >
    <!-- 
      * Card 
    -->
    <div class="w-full p-5 rounded shadow-md bg-base-100">
      <div class="flex justify-between mx-1">
        <!--
          * User and Service Details
        -->
        <div>
          <h2 class="mt-1 text-lg text-primary">{user.name}</h2>
          <h3 class="mb-1 -mt-1 text-sm text-neutral">ID: {user.id}</h3>
        </div>
        <div>
          <h2 class="mt-1 text-lg text-primary">{service.name}</h2>
          <h3 class="mb-1 -mt-1 text-sm text-end text-neutral">ID: {service.id}</h3>
        </div>
      </div>
      <!--
        * Review Box
      -->
      <div class="p-4 my-2 rounded bg-base-300">
        <p class="text-wrap">
          {review}
        </p>
      </div>
      <!--
        * User and Service Ratings
      -->
      <div class="flex justify-between mx-1">
        <div class="mt-2">
          <h2>
            User rating: <i class="text-sm text-warning fa-solid fa-star"></i>
            {user.rating}
          </h2>
          <h2 class="-mt-1 text-primary">
            Job Rating: <i class="text-sm text-warning fa-solid fa-star"></i>
            {service.rating}
          </h2>
        </div>
        <!--
          * Action Button
        -->
        <div>
          <button
            class="flex p-2 px-6 mt-4 text-white btn btn-primary"
            ><i class="block p-1 fa-solid fa-xmark md:hidden"></i>
            <span class="hidden md:block">Close</span></button
          >
        </div>
      </div>
    </div>
  </div>
  
  <style></style>
  