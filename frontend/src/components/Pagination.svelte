<nav aria-label="Page navigation example">
  <ul class="flex list-style-none">
    <li>
      <!-- svelte-ignore a11y-missing-attribute -->
      <a
        class="pointer-events-none relative block rounded-full bg-transparent px-3 py-1.5 text-sm text-surface/50 transition duration-300 dark:text-neutral-400"
        >Previous</a
      >
    </li>
    <li>
      <a
        class="relative block rounded-full bg-transparent px-3 py-1.5 text-sm text-surface transition duration-300 hover:bg-neutral-100 focus:bg-neutral-100 focus:text-primary-700 focus:outline-none active:bg-neutral-100 active:text-primary-700 dark:text-white dark:hover:bg-neutral-700 dark:focus:bg-neutral-700 dark:focus:text-primary-500 dark:active:bg-neutral-700 dark:active:text-primary-500"
        href="#!">1</a
      >
    </li>
    <li aria-current="page">
      <a
        class="relative block rounded-full bg-primary-100 px-3 py-1.5 text-sm font-medium text-primary-700 transition duration-300 focus:outline-none dark:bg-slate-900 dark:text-primary-500"
        href="#!"
        >2
        <span
          class="absolute -m-px h-px w-px overflow-hidden whitespace-nowrap border-0 p-0 [clip:rect(0,0,0,0)]"
          >(current)</span
        >
      </a>
    </li>
    <li>
      <a
        class="relative block rounded-full bg-transparent px-3 py-1.5 text-sm text-surface transition duration-300 hover:bg-neutral-100 focus:bg-neutral-100 focus:text-primary-700 focus:outline-none active:bg-neutral-100 active:text-primary-700 dark:text-white dark:hover:bg-neutral-700 dark:focus:bg-neutral-700 dark:focus:text-primary-500 dark:active:bg-neutral-700 dark:active:text-primary-500"
        href="#!">3</a
      >
    </li>
    <li>
      <a
        class="relative block rounded-full bg-transparent px-3 py-1.5 text-sm text-surface transition duration-300 hover:bg-neutral-100 focus:bg-neutral-100 focus:text-primary-700 focus:outline-none active:bg-neutral-100 active:text-primary-700 dark:text-white dark:hover:bg-neutral-700 dark:focus:bg-neutral-700 dark:focus:text-primary-500 dark:active:bg-neutral-700 dark:active:text-primary-500"
        href="#!">Next</a
      >
    </li>
  </ul>
</nav>
