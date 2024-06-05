<script setup lang="ts">
const items = [
  [{
    label: 'karim@example.com',
    slot: 'account',
    disabled: true
  }], [{
    label: 'Settings',
    icon: 'i-heroicons-cog-8-tooth',
    href: '/settings'
  }], [{
    label: 'Documentation',
    icon: 'i-heroicons-book-open',
    href: '/documentation'
  }, {
    label: 'Changelog',
    icon: 'i-heroicons-megaphone',
    href: '/changelog'
  }, {
    label: 'Status',
    icon: 'i-heroicons-signal',
    href: '/status'
  }], [{
    label: 'Sign out',
    icon: 'i-heroicons-arrow-left-on-rectangle',
    href: '/login'
  }, ]
]
</script>

<template>
  <UDropdown :items="items" :ui="{ item: { disabled: 'cursor-text select-text' } }" :popper="{ placement: 'bottom-start' }">
    <UAvatar src="https://avatars.githubusercontent.com/u/739984?v=4" />

    <template #account="{ item }">
      <div class="text-left">
        <p>
          Signed in as
        </p>
        <p class="truncate font-medium text-gray-900 dark:text-white">
          {{ item.label }}
        </p>
      </div>
    </template>

    <template #item="{ item }">
      <a v-if="item.href" :href="item.href" class="flex items-center space-x-2 truncate">
        <span>{{ item.label }}</span>
        <UIcon :name="item.icon" class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500 ms-auto" />
      </a>
      <span v-else class="flex items-center space-x-2 truncate">
        <span>{{ item.label }}</span>
        <UIcon :name="item.icon" class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500 ms-auto" />
      </span>
    </template>
  </UDropdown>
</template>
