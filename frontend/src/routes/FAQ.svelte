<script>
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";

  let openIndex = null;

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
      });
  });

  function toggleItem(index) {
    openIndex = openIndex === index ? null : index;
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
  class="flex flex-col items-center justify-center h-full min-h-screen py-20 m-auto"
>
  <div class="flex flex-col w-full max-w-5xl gap-4 px-2">
    <div class="flex flex-col gap-4 text-center">
      <h2 class="text-5xl text-[#cc2936]">FAQ</h2>
      <br />
      <p class="max-w-sm mx-auto">
        Here are some frequently asked questions. If you have any other
        questions, please feel free to contact us.
      </p>
    </div>
    <br />
    {#each questions as { question, answer }, index}
      <div
        class="max-w-3xl px-4 mx-auto bg-white border-b-2 rounded-lg border-[#cc2936] text-[#1f1f1f] transition-all duration-100 hover:bg-[#cc2936] hover:text-[#f1f1f1]"
      >
        <button
          class="w-full px-2 py-4 text-xl font-medium text-left rounded-lg focus:outline-none"
          on:click={() => toggleItem(index)}
        >
          {question}
        </button>
        <div
          class={`overflow-hidden transition-all duration-300 ${openIndex === index ? "max-h-screen" : "max-h-0"}`}
        >
          <div class="px-4 py-2">
            <p>{answer}</p>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
