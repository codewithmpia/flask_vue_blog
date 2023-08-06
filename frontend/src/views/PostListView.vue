<script setup>
    import axios from "axios";
    import { ref, onMounted } from "vue";
    import { RouterLink } from "vue-router";

    const posts = ref([])

    onMounted(async () => {
        await axios.get("http://127.0.0.1:5000/api/posts")
            .then(response => {
                if (response.status == 200) {
                    posts.value = response.data
                }
            })
            .catch(error => {
                console.log(error)
            })
    })
</script>

<template>
    <div class="container">
        <div class="posts">
            <div class="post" v-for="post in posts" :key="post.id">
                <RouterLink :to="`blog/${post.slug}`">
                    <h2>{{ post.title }}</h2>
                </RouterLink>
                <div class="post-meta">
                    <span>{{ post.date }}</span>
                    <span>{{ post.author }}</span>
                </div>
                <div class="post-resume">{{ post.resume }}</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .post {
        margin: 30px 0;
    }
    .post a {
        text-decoration: none;
    }
</style>