<script>
  import { slide } from "svelte/transition";
  let openItems = [];

  function toggleItem(index) {
    if (openItems.includes(index)) {
      openItems = openItems.filter((i) => i !== index);
    } else {
      openItems = [];
      openItems = [...openItems, index];
    }
  }

  let questions = [
    {
      question: "What services are offered on your platform?",
      answer:
        "Our platform offers a wide range of services across various categories such as home services, professional services, beauty and wellness, and more. You can browse through our service listings to find what you're looking for.",
    },
    {
      question: "How do I book or schedule a service?",
      answer:
        "To book or schedule a service, simply navigate to the service you're interested in, select the date and time that works best for you, and follow the prompts to complete the booking process. You'll receive confirmation once your booking is successful.",
    },
    {
      question: "How can I pay for services on your platform?",
      answer:
        "For the time being, the only payment method we are working with is ATH Movil. Make sure to look up in the setting for the option to upload your QR code. Don't worry if you dont know how to upload it, we have a step by step guide to help you set it up. We are working on adding more payment options in the future. Stay tuned!",
    },
    {
      question: "What are your cancellation and refund policies?",
      answer:
        "Our cancellation and refund policies vary depending on the service and provider. Generally, you can cancel or reschedule appointments with reasonable notice without any penalties. Refunds may be applicable in certain situations, such as provider cancellations or dissatisfaction with the service rendered.",
    },
    {
      question: "How are service providers vetted and rated on your platform?",
      answer:
        "We have a rigorous vetting process in place to ensure that our service providers meet certain quality standards and are properly licensed and insured, where applicable. Additionally, our platform features a rating system where customers can leave reviews and feedback about their experiences, helping others make informed decisions.",
    },
    {
      question:
        "Can I leave reviews or feedback for service providers I've used?",
      answer:
        "Yes, we highly encourage customers to leave honest reviews and feedback for service providers they've used on our platform. This helps maintain transparency and quality control, and aids other users in making informed choices based on real experiences.",
    },
  ];
</script>

<div
  class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
>
  <div class="max-w-xl sm:mx-auto lg:max-w-2xl">
    <div class="flex flex-col mb-6 sm:text-center">
      <a href="/" class="mb-6 sm:mx-auto"> </a>
      <div class="max-w-xl md:mx-auto sm:text-center lg:max-w-2xl">
        <h2
          class="max-w-lg mb-8 ml-auto mr-auto text-5xl font-semibold text-center text-primary sm:text-5xl md:mx-auto sm:ml-10"
        >
          FAQ
        </h2>
        <p class="text-center text-neutral md:text-lg text-balance">
          Here are some frequently asked questions. If you have any other
          questions, please feel free to contact us.
        </p>
      </div>
    </div>
    <div class="p-5 rounded-lg bg-base-150">
      <div class="space-y-2">
        {#each [0, 1, 2, 3, 4, 5] as index}
          <div class="border rounded shadow-md">
            <button
              type="button"
              aria-label="Open item"
              title="Open item"
              class="flex flex-col items-center justify-between w-full p-4 bg-base-100 focus:outline-none"
              on:click={() => toggleItem(index)}
            >
              <div class="mt-2">
                <p class="text-lg font-medium text-center">
                  {#if index === 0}{questions[0].question}{/if}
                  {#if index === 1}{questions[1].question}{/if}
                  {#if index === 2}{questions[2].question}{/if}
                  {#if index === 3}{questions[3].question}{/if}
                  {#if index === 4}{questions[4].question}{/if}
                  {#if index === 5}{questions[5].question}{/if}
                </p>
                <span><i class="fa-solid fa-angle-down"></i></span>
              </div>
            </button>
            {#if openItems.includes(index)}
              <div
                transition:slide={{ duration: 300 }}
                class="p-4 pt-0 bg-base-100"
              >
                <p class="text-center text-neutral">
                  {#if index === 0}{questions[0].answer}{/if}
                  {#if index === 1}{questions[1].answer}{/if}
                  {#if index === 2}{questions[2].answer}{/if}
                  {#if index === 3}{questions[3].answer}{/if}
                  {#if index === 4}{questions[4].answer}{/if}
                  {#if index === 5}{questions[5].answer}{/if}
                </p>
              </div>
            {/if}
          </div>
        {/each}
      </div>
    </div>
  </div>
</div>
