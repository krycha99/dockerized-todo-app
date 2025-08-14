<script setup>
import { ref } from 'vue'
import { useTasksStore } from '../stores/tasks'
const store = useTasksStore()
const title = ref('')

function onSubmit() {
  store.addTask(title.value)
  title.value = ''
}
</script>

<template>
  <form @submit.prevent="onSubmit" class="form">
    <input type="text" v-model="title" placeholder="New tasks..." />
    <button type="submit" class="add-btn">Add task</button>
  </form>
</template>

<style scoped>
    .form { display:flex; gap:.5rem; }
    input { flex:1; padding:.5rem; }
    button { padding:.5rem 1rem; }
</style>