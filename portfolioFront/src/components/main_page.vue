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
                    <div class= "button" :class="{ active: activeButton === 1 }" @click="activeButton !== 1 ? setActiveButton(1) : null">
                        <span>Edificios Unifamiliares</span>
                    </div>
                    <div class= "button" :class="{ active: activeButton === 2 }" @click="activeButton !== 2 ? setActiveButton(2) : null">
                        <span>Edificios Multifamiliares</span>
                    </div>
                    <div class= "button" :class="{ active: activeButton === 3 }" @click="activeButton !== 3 ? setActiveButton(3) : null">
                        <span>Escritorios e Comércio</span>
                    </div>
                    <div class= "button" :class="{ active: activeButton === 4 }" @click="activeButton !== 4 ? setActiveButton(4) : null">
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
    box-sizing: border-box;
    padding: 20px;
}

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
    padding-right: 30px;
}

.upper-text {
    font-size: 2.1em;
    font-weight: 500;
    color: #000;
    margin-bottom: 10px;
}

.lower-text {
    font-size: 1em; 
    line-height: 1.5em;
    font-weight: 400;
    color: #fff;
}

@media (max-width: 1150px) {
    .upper-text {
        font-size: 1.7em;
        font-weight: 500;
    }
    
    .lower-text {
        font-size: .8em; 
        font-weight: 400;
    }
}

@media (max-width: 950px) {
    .upper-text {
        font-size: 1.4em;
        font-weight: 500;
    }
    
    .lower-text {
        font-size: .6em; 
        font-weight: 400;
    }
}

@media (max-width: 650px) {
    .upper-text {
        font-size: .8em;
        font-weight: 500;
    }
    
    .lower-text {
        font-size: .5em; 
        font-weight: 400;
    }
    .foto {
        display: none; 
    }

    .text {
        max-width: 100%; 
    }

    .info {
        justify-content: flex-start; 
    }
}

.foto {
    width: 100%; 
    height: auto;
    max-width: 100%; 
    overflow: hidden;
}

.foto img {
    width: 100%; 
    height: auto; 
    object-fit: cover; 
    border-radius: 5px;
}

.projetos {
    padding: 1% 1.5% 1% 1.5%; /*cima dir baixo esq */
    margin-top: 20px;
}

.title {
    font-size: 2em;
    font-weight: bold;
    color: #000;
    margin-bottom: 10px;
    z-index: 1;
}

.buttons-cards {
    display: flex;
    flex-direction: column;
}

.buttons {
    position: sticky;
    top: 0;
    background-color: #aea8a3;
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    padding: 30px 50px 20px 0;
    width: 100%;
    z-index: 1;
}

.buttons .button {
    font-size: 20px;
    font-weight: 400; 
}

@media (max-width: 650px) {
    .buttons .button {
        font-size: 14px; 
    }

    .buttons div {
        width: 8%;
        padding: 10px 10px;
    }
}

@media (max-width: 575px) {
    .buttons .button {
        font-size: 11px; 
        font-weight: 600; 
    }
}

.buttons div { /* dentro dos butões */
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
    z-index: 0;
    padding-left: 35px;
    padding-right: 10px;
    padding-top: 20px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: start;
    row-gap: 30px;
    column-gap: 8%;
    align-self: flex-start;
}

@media (max-width: 2200px) {
    .cards {
        padding-left: 10px;
        padding-right: 10px;
        column-gap: 10px;
        justify-self: start;
    }
}

@media (max-width: 950px) {
    .cards {
        padding-left: 10px;
        padding-right: 10px;
        column-gap: 10px;
    }
}

@media (max-width: 869px) {
    .cards {
        overflow: hidden;
        padding-left: 10px;
        padding-right: 20px;
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        justify-content: space-around;
        row-gap: 15px;
    }
}

</style>