<script setup>
import AddTaskForm from '../components/AddTaskForm.vue'
import TaskList from '../components/TaskList.vue'
</script>

<template>
  <main class="container">
    <h1 class="title">Todo App</h1>
    <AddTaskForm />
    <TaskList />
  </main>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
    .container { max-width: 680px; margin: 2rem auto; padding: 0 1rem; }
</style>