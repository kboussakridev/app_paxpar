<script setup lang="ts">
const user = useSupabaseUser()
const items = [
  [{
    slot: 'account',
    disabled: true
  }], [{
    label: 'checklist',
    icon: 'i-heroicons-document-check-20-solid',
    href: '/checklist'
  }], [{
    label: 'craftform',
    icon: 'i-heroicons-table-cells-solid',
    href: '/craftform'
  }, {
    label: 'bio',
    icon: 'i-heroicons-megaphone-16-solid',
    href: '/bio'
  }, {
    label: 'contact',
    icon: 'i-heroicons-chat-bubble-left-right-16-solid',
    href: '/contact'
  }], [{
    label: 'Sign out',
    icon: 'i-heroicons-arrow-right-start-on-rectangle-16-solid',
    href: '/profile'
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
          {{ user.email }}
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
