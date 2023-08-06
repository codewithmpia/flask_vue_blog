<script>
    import axios from "axios";

    export default {
        data() {
            return {
                form: {
                    name: "",
                    email: "",
                    message: ""
                },
                showAlert: ""
            }
        },
        methods: {
            async sendMessage() {
                await axios.post("http://127.0.0.1:5000/api/contact", this.form)
                    .then(response => {
                        if (response.status == 200) {
                            this.showAlert = response.data.message
                            this.form.name = ""
                            this.form.email = ""
                            this.form.message = ""
                        }
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>

<template>
    <div class="container">
        <h1>Me contacter</h1>
        <p>
            Des questions ? des remarques ? ou des suggestions ?
            Vous êtes au bon endroit, contactez-moi via ce formulaire et 
            je reviendrai vers vous dans le plus bref delais.
        </p>
        <div class="alert" v-if="showAlert">
            <strong v-text="showAlert"></strong>
        </div>
        <form @submit.prevent="sendMessage" class="form">
            <div class="form-row">
                <div class="form-group">
                    <label for="name" class="form-label">Votre nom</label>
                    <input type="text" name="name" id="name" class="form-control" required v-model="form.name">
                </div>
                <div class="form-group">
                    <label for="email" class="form-label">Votre adresse mail</label>
                    <input type="email" name="email" id="email" class="form-control" required v-model="form.email">
                </div>
            </div>
            <div class="form-group">
                <label for="message" class="form-label">Votre message</label>
                <textarea name="message" id="message" cols="30" rows="10" class="form-control" required v-model="form.message"></textarea>
            </div>
            <div class="form-group">
                <button class="btn">Enoyer</button>
            </div>
        </form>
    </div>
</template>

<style scoped>
    .alert {
        padding: 10px 15px;
        border-radius: 5px;
        background-color: #D1E7DE;
        border: 1px solid #A3CFBB;
    }
    .form {
        margin: 30px 0;
    }
    .form-row {
        width: 100%;
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }
    .form-group {
        width: 100%;
        margin: 10px 0;
    }
    .form-label {
        display: block;
        text-transform: uppercase;
        margin-bottom: 6px;
        font-weight: 500;
    }
    .form-control {
        width: calc(100% - 30px);
        font-size: 16px;
        padding: 10px 15px;
        border-radius: 5px;
        outline: 0;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ced4da;
        appearance: none;
        transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;

    }
    .form-control:focus {
        color: #212529;
        background-color: #fff;
        border-color: #86b7fe;
        outline: 0;
        box-shadow: 0 0 0 0.25rem rgba(13,110,253,.25);
    }
    textarea {
        font-family: "Roboto", sans-serif;
        font-size: 15px;
    }
    .btn {
        background-color: var(--color2);
        color: #fff;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15),0 1px 1px rgba(0, 0, 0, 0.075);
        padding: 10px 15px;
        font-size: 16px;
        font-weight: 600;
        outline: none;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: .3s;
    }
    .btn:hover {
        box-shadow: 0 0 0 0.25rem rgba(13,110,253,.25);
        background-color: #2443c1;
    }

    @media screen and (max-width: 700px) {
        .form-row {
            grid-template-columns: repeat(1, 1fr);
            gap: 0;
        }
    }
</style>