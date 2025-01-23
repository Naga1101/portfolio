<template>
    <nav class="navbar">
        <div class="button-placeholder">
            <button class="return_button" v-if="showBackButton" @click="goToMainPage"> 
                <img src="/svgs/back_arrow.svg"/>
                <span>VOLTAR ATRÁS</span>
            </button>
        </div>
        <div class="right_data">
            <span> Arquiteta Paula Gonçalves Santos </span>
        </div>
    </nav>
</template>

<script>
    export default {
        data() {
            return {
                showBackButton: false,
            };
        },
        mounted() {
            this.showBackButton = this.$route.path !== '/';
        },
        methods: {
            goToMainPage() {
                this.$router.push({ path: '/' });
            },
        },
    };
</script>

<style scoped>
    html, body {
        margin: 0;
        padding: 0;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        padding: 7px 30px;
        background-color: rgb(233, 225, 209, 0.75);
        color: #000000;
        font-weight: 500;
        height: fit-content;
        border-bottom: 1.5px solid rgba(0, 0, 0, 0.8); /* Optional: Adds bottom border */
    }

    .button-placeholder {
        width: auto; /* Same width as the button */
        height: 2.5em; /* Same height as the button */
        display: flex;
        align-items: center;
    }

    .return_button {
        background-color: rgba(166, 193, 207, 0.9);
        color: #282828;
        padding: 8px 12px;
        cursor: pointer;
        font-size: 1.1em;
        padding: 12px 20px;
        /* width: 20vw;
        height: 50px; */
        width: auto;
        height: 2.5em;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        font-weight: semibold;
        align-items: center;
        justify-content: center;
        display: flex;
    }

    .return_button img {
        height: 25px;
        object-fit:contain;
        fill: #282828;
    }

    .return_button:hover{
        opacity: 85%;
    }

    .return_button span {
        padding-left: 0.35em;
    }

    .right_data {
        display: inline-flex;
        align-items: center;
        cursor: default;
    }
</style>