<script >
    import { RouterLink, RouterView } from 'vue-router';
    
    export default {
        data() {
            return {
                showMobile: false
            }
        },
        methods: {
            showMenu () {
                this.showMobile = !this.showMobile;
            }
        }
    }


</script>

<template>
    <div class="container">
        <nav class="navbar">
            <a href="/" class="logo">
                <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-code-slash" viewBox="0 0 16 16">
                    <path d="M10.478 1.647a.5.5 0 1 0-.956-.294l-4 13a.5.5 0 0 0 .956.294l4-13zM4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0zm6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0z"/>
                </svg>
                <span>Codewithmpia.fr</span>
            </a>
            <div class="navigation">
                <div class="menu" :class="this.showMobile ? 'open' : ''">
                    <RouterLink to="/">Blog</RouterLink>
                    <RouterLink to="/contact">Contact</RouterLink>
                </div>
                <div class="mobile" @click="showMenu()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
                    </svg>
                </div>
            </div>
        </nav>
    </div>
    <RouterView />
</template>

<style scoped>
    .navbar {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0;
        box-shadow: rgba(33, 35, 38, 0.1) 0px 10px 10px -10px;
        z-index: 3;
    }

    .navbar a {
        text-decoration: none;
        text-transform: uppercase;
        font-weight: 500;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .logo span {
        font-size: 22px;
        font-weight: 900;
    }

    .navigation {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .menu {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .mobile {
        display: none;
        align-items: center;
    }

    .mobile .bi {
        color: var(--color1);
        cursor: pointer;
    }

    .mobile .bi:hover {
        color: var(--color2);
    }

    @media screen and (max-width: 600px) {
        .navbar {
            position: relative;
            width: 100%;
        }
        .navigation {
            width: 100%;
            position: relative;
            justify-content: end;
            
        }
        .menu {
            width: 100%;
            display: none;
        }
        .menu.open {
            position: absolute;
            display: flex;
            flex-direction: column;
            gap: 0;
            top: 55px;
            width: 200px;
            background-color: #fff;
            box-shadow: rgba(17, 17, 26, 0.1) 0px 0px 16px;
            z-index: 2;
            padding: 10px;
            gap: 5px;
            border-radius: 5px;
        }
        .menu.open a {
            display: block;
            width: 100%;
            text-align: center;
            padding: 3px 0;
        }
        .menu.open a:hover {
            background-color: aliceblue;
        }
        .mobile {
            display: flex;
        }
    }
</style>