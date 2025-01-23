<template>
    <Navbar />
    <div class= "page">
        <div class= "info-project">
            <div class= "info-text">
                <div class= "title">
                    <span> {{ item.titulo }} </span>
                </div>
                <div class= "info">
                    <span> {{ item.descricao }} </span>
                </div>
            </div>
            <div class= "main_image">
                <img :src="item.main_image" alt="image"/>
            </div>
        </div><!-- 
        <div class= "plantas">
            <div class= "title-plantas">
                <span>Plantas</span>                
            </div>
            <div class="outer-rect">
                <div class="inner-rect"></div>
            </div>            
            <div class= "plantas">

            </div> 
        </div>-->
        <div class="fotos">
            <div class="title-fotos">
                <span>Imagens e 3Ds</span>                
            </div>
            <div class="fotos">
                <div v-for="(foto, index) in item.fotos" :key="index" class="foto-item">
                    <img :src="foto" :alt="'image' + index"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Navbar from './main_navbar.vue';
    import infoEdf from '../backend/projetos.json';
    export default {
        components: {
            Navbar,
        },

        props: {
            edificioID: {
                type: String,
                required: true
            }
        },

        data() {
            return {
                item: null,
            };
        },

        created() {
            this.fetchItem();
        },

        methods: {
            fetchItem() {
                this.item = infoEdf.edfInfo.find(projeto => String(projeto.id) === this.edificioID);
            }
        }
    }
</script>

<style>
.page {
    box-sizing: border-box;
    padding: 0px;
}

.info-project{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0;
    width: 100%;
    max-height: 500px;
    background-color: #CABBA9;
    box-sizing: border-box;
}

.info-text {
    display: flex;
    flex-direction: column;
    padding-left: 1.5%;
    max-width: 85%; /* Control the width of the text section */
    padding-right: 30px;
}

.main_image{
    width: 60%; 
    height: auto;
    max-height: 500px;
    overflow: hidden;
}

.foto img {
    width: 100%; 
    height: auto; 
    border-radius: 5px;
}

.title, .title-plantas, .title-fotos {
    font-size: 2.8em;
    font-weight: 500;
    color: #282828; 
}

.info {
    font-size: 1.8em;
    font-weight: 400;
    color: #282828; 
}

.outer-rect {
    width: 100%;
    max-width: 500px; /* Adjust the max-width as needed */
    height: 20px;
    border: 2px solid #000; /* Black border */
    border-radius: 10px; /* Rounded corners */
    background-color: #D3CFCB; /* Background color similar to the one in the image */
    padding: 2px;
    box-sizing: border-box;
}

.inner-rect {
    width: 30%; /* Adjust the percentage based on progress */
    height: 100%;
    background-color: #2E2825; /* Darker fill color */
    border-radius: 10px;
}
</style>

