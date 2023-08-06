import { createRouter, createWebHistory } from "vue-router";
import PostListView from "../views/PostListView.vue";
import PostDetailView from "../views/PostDetailView.vue";
import ContactView from "../views/ContactView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.BASE_URL),
    routes: [
        {
            path: "/",
            name: "blog",
            component: PostListView
        },
        {
            path: "/blog/:slug",
            name: "blog-detail",
            component: PostDetailView
        },
        {
            path: "/contact",
            name: "contact",
            component: ContactView
        }
    ]
})

export default router