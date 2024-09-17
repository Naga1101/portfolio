<template>
    <Navbar/>
    <div class= "page">
        <div class= "info">
            <div class= "text">
                <div class= "upper-text">
                    <span>{{ info.name }}</span>
                </div>
                <div class= "lower-text">
                    <span>{{ info.bio }}</span>
                </div>
            </div>
            <div class= "foto">
                <img :src="info.profilePicture">
            </div>
        </div>
        <div class= "projetos">
            <div class= "title">
                <span>Projetos</span>
            </div>
            <div class= "buttons-cards">
                <div class= "buttons">
                    <div class= "unif-button" :class="{ active: activeButton === 1 }" @click="activeButton !== 1 ? setActiveButton(1) : null">
                        <span>Edificios Unifamiliares</span>
                    </div>
                    <div class= "multi-button" :class="{ active: activeButton === 2 }" @click="activeButton !== 2 ? setActiveButton(2) : null">
                        <span>Edificios Multifamiliares</span>
                    </div>
                    <div class= "escrt-button" :class="{ active: activeButton === 3 }" @click="activeButton !== 3 ? setActiveButton(3) : null">
                        <span>Escritorios e Comércio</span>
                    </div>
                    <div class= "reabl-button" :class="{ active: activeButton === 4 }" @click="activeButton !== 4 ? setActiveButton(4) : null">
                        <span>Reabilitação</span>
                    </div>
                </div>
                    <div class= "cards" v-if="filteredInfo.length">
                        <Card v-for="(item, index) in filteredInfo" :key="index" :item="item"/>
                    </div>
                    <div v-else>
                        <p>No cards to display</p>
                    </div>
            </div>
        </div>
    </div>
</template>

<script>
import Navbar from './main_navbar.vue';
import Card from './project_card.vue';
import infoArqDB from '../backend/paula.json';
import infoEdf from '../backend/projetos.json';

export default {
    components: {
        Navbar,
        Card
    },

    data() {
        return {
            info: infoArqDB.info,
            edfInfo: infoEdf.edfInfo || [],
            activeButton: 1,
        };
    },

    computed: {
        filteredInfo() {
            return this.edfInfo.filter(item => item.teste === this.activeButton);
        }
    },

    methods: {
        setActiveButton(buttonNumber) {
            this.activeButton = buttonNumber;
        },
    },
};
</script>

<style scoped>
.page {
    background-color: rgba(148, 140, 131, 0.75);
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
}

/* Styling for the info section (bio and image) */
.info {
    flex: 0 0 33%;
    display: flex;
    justify-content: space-between; /* Space between the text and the image */
    align-items: center; /* Vertically align the image and text */
    padding: 20px 0;
    padding-left: 1.5%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.15); /* Background for the bio section */
    box-sizing: border-box;
}

.text {
    max-width: 85%; /* Control the width of the text section */
}

.upper-text {
    font-size: 2.5em;
    font-weight: 500;
    color: #000;
    margin-bottom: 10px;
}

.lower-text {
    font-size: 1.4em; 
    line-height: 1.5em;
    font-weight: 400;
    color: #fff;
}

.foto img {
    border-radius: 5px;
    width: auto; 
    height: 100%;
    object-fit: cover;
}

/* Styling for the "Projetos" section */
.projetos {
    padding: 1% 1.5% 1% 1.5%; /*cima dir baixo esq */
    margin-top: 20px;
}

.title {
    font-size: 2em;
    font-weight: bold;
    color: #000;
    margin-bottom: 10px;
}

.buttons-cards {
    display: flex;
    flex-direction: column;
}

.buttons {
    padding-top: 0.5%;
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.buttons div {
    width: 18%;
    text-align: center;
    padding: 10px 20px;
    border: 1px solid #000;
    background-color: transparent;
    cursor: pointer;
    color: #403737;
    transition: background-color 0.3s;
}

.buttons div.active {
    color: #000000;
    background-color: rgba(111, 78, 55, 0.8);
    cursor: default;
}

.buttons div:hover {
    background-color: rgba(111, 78, 55, 0.4);
}

.buttons div.active:hover {
    background-color: rgba(111, 78, 55, 0.8);
}

.cards {
    padding: 0 2.5% 5% 2.5%;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: start;
    row-gap: 15px;
    column-gap: 15px;
    align-self: flex-start;
}

</style>