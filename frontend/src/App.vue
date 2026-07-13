<script setup>
import { ref, onMounted } from 'vue'

const posts = ref([])
const newTitle = ref('')
const newText = ref('')
const token = ref('')

onMounted(() => {
  fetch('http://localhost:8000/blog/posts/')
    .then(response => response.json())
    .then(data => posts.value = data.results)
})
</script>

<template>
  <h1>Блог</h1>

  <div v-for="post in posts" :key="post.id">
    <h2>{{ post.title }}</h2>
    <div>{{ post.text }}</div>
    <div>{{ new Date(post.created_at).toLocaleString('ru-RU') }}</div>

    <img v-if="post.image" :src="post.image" class="post-image">

    <hr>
  </div>
</template>

<style>
.post-image {
  width: 300px;
  height: 200px;
  object-fit: cover;
}
</style>
