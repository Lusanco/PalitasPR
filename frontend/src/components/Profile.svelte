<!-- Profile component -->

<script>
  let name = "Alfredo Santiago Cosme de los Palotes";
  let provServ = "Landscaper";
  let userTown = "San Juan, PR";
  let userRating = 4.7;
  let clientsCount = "100 Clients";
  let jobsCount = 20;
  let reviewerName = "John Doe";
  let reviewStars = 4.5;
</script>

<!--* Profile Body -->
<body class="h-screen font-mono">
  <div class="profileContainer py-3 px-[5%] text-[#626262] bg-slate-100">
    <img
      src="../images/lawnMowing.jpg"
      alt="Banner"
      class="w-full mb-4 rounded-md h-96"
    />
    <!--* Profile Details -->
    <div
      class="flex items-start justify-between p-5 mb-4 bg-white rounded-md shadow-md profileDetails"
    >
      <div class="w-full">
        <div class="pd">
          <div class="flex items-start pdRow">
            <img
              src="../images/profile.png"
              alt="User Pic"
              class="w-24 mr-4 rounded-md pdImg"
            />
            <div class="flex justify-between w-full">
              <div>
                <h3 class="py-[7px] text-2xl font-semibold">{name}</h3>

                <p class="text-sm">{provServ}</p>
                <p class="text-sm">
                  <i class="fa-solid fa-star"></i> <span>{userRating}</span>
                </p>
              </div>
              <div class="relative flex justify-end bottom-8">
                <button type="button" class="pr-2 text-black">
                  <i class="fa-solid fa-ellipsis"></i>
                </button>
              </div>
              <!-- <p id="clientsCount" class="text-sm text-center"></p> -->
              <!-- <div class="flex justify-between pdClients">
                <img
                  src="images/images/member-1.png"
                  alt=""
                  class="w-6 mt-2 rounded-full"
                />
                <img
                  src="images/images/member-2.png"
                  alt=""
                  class="w-6 mt-2 rounded-full"
                />
                <img
                  src="images/images/member-3.png"
                  alt=""
                  class="w-6 mt-2 rounded-full"
                />
                <img
                  src="images/images/member-4.png"
                  alt=""
                  class="w-6 mt-2 rounded-full"
                />
              </div> -->
            </div>
          </div>
        </div>
        <div class="flex justify-center gap-2 mt-4">
          <button
            type="button"
            class="w-full p-2 text-black bg-gray-100 rounded-lg shadow-sm hover:bg-gray-300"
          >
            <i class="text-xs fa-solid fa-user-plus"></i>
          </button>
          <button
            type="button"
            class="w-full p-2 text-white bg-green-800 rounded-lg shadow-sm hover:bg-green-900"
          >
            <i class="text-xs fa-solid fa-message"></i>
          </button>
        </div>
      </div>
    </div>
    <!--* Profile Info -->
    <div class="profileInfo">
      <div class="grid grid-cols-3 gap-4">
        <div class="infoCol">
          <!--* User Info Containers -->
          <!--* User About Me -->
          <div
            class="w-full p-4 mx-0 my-5 bg-white rounded-md shadow-md userInfoContainer"
          >
            <div class="aboutHeader">
              <h3 class="text-xl font-bold border-b-2">About me</h3>
              <div class="pt-3">
                <i class="fa-solid fa-location-dot"></i>
                <span>{userTown}</span>
              </div>
              <div class="">
                <i class="pr-2 fa-solid fa-check"></i>Completed jobs:
                <span>{jobsCount}</span>
              </div>
            </div>
          </div>
          <!--* User Description -->
          <div
            class="w-full p-4 mx-0 my-5 bg-white rounded-md shadow-md userDescriptionContainer"
          >
            <div class="userDescriptionHeader">
              <h3 class="text-xl font-bold border-b-2">Description</h3>
              <div class="pt-3">
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab
                  repudiandae, nemo animi amet unde modi, consectetur voluptas
                  quae, iusto facilis dolor architecto! Sequi praesentium quidem
                  autem temporibus inventore iste eius.
                </p>
              </div>
            </div>
          </div>
          <!--* User Social Links -->
          <div
            class="w-full p-4 bg-white rounded-md shadow-md userSocialsContainer"
          >
            <h3 class="text-xl font-bold border-b-2">Socials</h3>
            <ul class="flex flex-col justify-start pt-3">
              <li>
                <button>
                  <a
                    href="https://www.facebook.com/"
                    class="hover:text-green-800"
                    ><i class="fa-brands fa-square-facebook"></i> Facebook</a
                  >
                </button>
              </li>
              <li>
                <button>
                  <a
                    href="https://www.instagram.com/"
                    class="hover:text-green-800"
                    ><i class="fa-brands fa-instagram"></i> Instagram</a
                  >
                </button>
              </li>
              <li>
                <button>
                  <a href="https://twitter.com/" class="hover:text-green-800"
                    ><i class="fa-brands fa-square-twitter"></i> Twitter</a
                  >
                </button>
              </li>
            </ul>
          </div>
          <!--* User Gallery -->
          <div
            class="w-full p-4 mx-0 my-5 bg-white rounded-md shadow-md userGalleryContainer"
          >
            <div class="aboutHeader">
              <h3 class="text-xl font-bold border-b-2">Gallery</h3>
              <div class="grid grid-cols-3 grid-rows-2 gap-2 pt-2 userGalley">
                <img
                  src="images/images/gallGrid_1.jpg"
                  alt=""
                  class="h-24 rounded-md w-28"
                />
                <img
                  src="images/images/gallGrid_2.jpg"
                  alt=""
                  class="h-24 rounded-md w-28"
                />
                <img
                  src="images/images/gallGrid_3.jpg"
                  alt=""
                  class="h-24 rounded-md w-28"
                />
                <img
                  src="images/images/gallGrid_4.jpg"
                  alt=""
                  class="h-24 rounded-md w-28"
                />
                <img
                  src="images/images/gallGrid_5.jpg"
                  alt=""
                  class="h-24 rounded-md w-28"
                />
                <img
                  src="images/images/gallGrid_6.jpg"
                  alt=""
                  class="h-24 rounded-md w-28"
                />
              </div>
              <button
                type="button"
                class="w-full p-2 mt-2 text-sm rounded-md shadow-sm hover:bg-slate-200 bg-slate-100"
              >
                See more
              </button>
            </div>
          </div>
          <!--* Reviews -->
          <div
            class="w-full p-4 mx-0 my-5 bg-white rounded-md shadow-md userInfoContainer"
          >
            <div class="reviewsHeader">
              <h3 class="text-xl font-bold border-b-2">Reviews</h3>
              <div class="pt-3">
                <div class="userReview">
                  <div
                    class="p-2 rounded-md shadow-md reviewHeader bg-slate-100"
                  >
                    <div
                      class="flex justify-between p-2 rounded-md bg-slate-200"
                    >
                      <h3 class="text-sm">{reviewerName}</h3>
                      <p class="text-xs">
                        <i class="fa-solid fa-star"></i>
                        <span>{reviewStars}</span>
                      </p>
                    </div>
                    <div class="flex justify-between">
                      <p class="p-2 text-xs">
                        Lorem ipsum dolor sit amet, consectetur adipisicing
                        elit.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-span-2 postCol">
          <!--* Post Container -->
          <div
            class="w-full p-3 mx-0 my-5 bg-white rounded-md shadow-md postContainer"
          >
            <div class="flex items-start w-full gap-3 mb-2 postHeader">
              <img
                src="images/images/profile.png"
                alt="User Pic"
                class="w-16 rounded-md pdImg"
              />
              <div class="flex justify-between w-full">
                <div>
                  <h3 class="text-lg font-semibold text-wrap">
                    {name}
                  </h3>

                  <p
                    class="inline-block p-1 text-xs font-thin text-center text-white bg-green-800 rounded-lg whitespace-nowrap min-w-12 max-w-40"
                  >
                    {provServ}
                  </p>
                </div>
                <div class="relative flex justify-end bottom-4">
                  <button type="button" class="pr-2 text-black">
                    <i class="fa-solid fa-ellipsis"></i>
                  </button>
                </div>
              </div>
            </div>
            <p class="mb-2 text-sm text-wrap">
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eveniet
              cumque ratione id voluptates quae. Iure expedita quaerat possimus
              optio adipisci laudantium? Vitae voluptas dignissimos iste rerum
              deleniti voluptatum voluptates a.
            </p>
            <div class="grid grid-cols-3 gap-2 mb-2">
              <img
                src="images/images/gallGrid_1.jpg"
                alt=""
                class="w-64 rounded-md h-52"
              />
              <img
                src="images/images/gallGrid_2.jpg"
                alt=""
                class="w-64 rounded-md h-52"
              />
              <img
                src="images/images/gallGrid_3.jpg"
                alt=""
                class="w-64 rounded-md h-52"
              />
            </div>
            <div class="flex justify-center gap-2">
              <button
                type="button"
                class="w-full p-2 text-black bg-gray-100 rounded-lg shadow-sm hover:bg-gray-300"
              >
                <i class="fa-regular fa-thumbs-up"></i>
              </button>
              <button
                type="button"
                class="w-full p-2 text-white bg-green-800 rounded-lg shadow-sm hover:bg-green-900"
              >
                <i class="text-xs fa-solid fa-message"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>

<style></style>
