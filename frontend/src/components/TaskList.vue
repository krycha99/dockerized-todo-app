<script setup>
import { onMounted } from 'vue'
import { useTasksStore } from '../stores/tasks'
const store = useTasksStore()

onMounted(() => store.fetchTasks())

function remove(t) {
  store.deleteTask(t.title)
}
</script>

<template>
  <div>
    <p v-if="store.loading">Ładowanie…</p>
    <p v-if="store.error">{{ store.error }}</p>
    <ul v-if="!store.loading">
      <li v-for="t in store.tasks" :key="t.title">
        <span>{{ t.title }}</span>
        <button @click="remove(t)">Usuń</button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
    li { display:flex; justify-content:space-between; padding:.25rem 0; }
    button { font-size:.9rem; }
</style>