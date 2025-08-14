import { defineStore } from 'pinia'
import api from '../services/api'
import { ref } from 'vue'

export const useTasksStore = defineStore('tasks', () => {
  const tasks = ref([])
  const loading = ref(false)
  const error = ref(null)

  async function fetchTasks() {
    loading.value = true; error.value = null
    try {
      const { data } = await api.get('/tasks')
      tasks.value = data
    } catch (e) {
      error.value = 'Failed to download tasks'
    } finally {
      loading.value = false
    }
  }

  async function addTask(title) {
    if (!title?.trim()) return
    const newTask = { title: title.trim(), done: false }
    tasks.value = [newTask, ...tasks.value]
    try {
      await api.post('/tasks', { title: newTask.title })
      await fetchTasks()
    } catch (e) {
      error.value = 'Failed to add task'
      await fetchTasks()
    }
  }

  async function deleteTask(title) {
    try {
      await api.delete(`/tasks/${encodeURIComponent(title)}`)
      tasks.value = tasks.value.filter(t => t.title !== title)
    } catch (e) {
      error.value = 'Failed to delete task'
    }
  }

  return { tasks, loading, error, fetchTasks, addTask, deleteTask }
})