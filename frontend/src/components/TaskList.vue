<script setup>
import { onMounted } from 'vue'
import { useTasksStore } from '../stores/tasks'
const store = useTasksStore()

onMounted(() => store.fetchTasks())

function remove(t) {
  store.deleteTask(t.title)
}

function toggleCompleted(t) {
  const updatedTask = { ...t, done: !t.done }
  store.updateTask(updatedTask)
}

</script>

<template>
  <div>
    <p v-if="store.loading">Loading…</p>
    <p v-if="store.error">{{ store.error }}</p>
    <ul v-if="!store.loading">
      <li v-for="t in store.tasks" :key="t.title">
        <div class="task-content">
          <input type="checkbox" :checked="t.done" @change="toggleCompleted(t)" />
          <span :class="{ completed: t.done }">{{ t.title }}</span>
        </div>
        <button class="delete-btn" @click="remove(t)">Remove</button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
button { font-size: .9rem; }
</style>