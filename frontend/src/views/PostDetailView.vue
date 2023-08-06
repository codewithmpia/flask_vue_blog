<script setup>
    import axios from 'axios';
    import { ref, onMounted } from 'vue';
    import { useRoute } from 'vue-router';

    const route = useRoute();
    const post = ref({})

    onMounted(async () => {
        await axios.get(`http://127.0.0.1:5000/api/posts/${route.params.slug}`)
            .then(response => {
                if (response.status == 200) {
                    post.value = response.data
                }
            })
            .catch(error => {
                console.log(error)
            })
    })
</script>

<template>
    <div class="container">
        <h1>{{ post.title }}</h1>
        <div class="post-meta">
            <span>{{ post.date }}</span>
            <span>{{ post.author }}</span>
        </div>
        <div class="post-resume">
            {{ post.resume }}
        </div>

        <div class="post-image">
            <img :src="`/src/assets/images/`+post.image">
        </div>

        <div class="post-content">
            {{ post.content }}
        </div>
    </div>
</template>

<style scoped>
    .post-image {
        width: 100%;
    }

    .post-image img {
        width: 100%;
        border-radius: 5px;
    }
</style>