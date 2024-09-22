<template>
    <Navbar />
    <div class= "page">
        <div class= "info-project">
            <div class= "info-text">
                <div class= "title">
                    <span>Título do projeto {{ item.id }}</span>
                </div>
                <div class= "info">
                    <span>Informação prolongada acerca do projeto realizado por paula do tipo {{ item.teste }}</span>
                </div>
            </div>
            <div class= "main image">

            </div>
        </div>
        <div class= "plantas">
            <div class= "title-plantas">
                <span>Plantas</span>                
            </div>
            <div class="outer-rect">
                <div class="inner-rect"></div>
            </div>            
            <div class= "plantas">

            </div>
        </div>
        <div class= "fotos">
            <div class= "title-fotos">
                <span>Fotos</span>                
            </div>
            <div class= "fotos">
                
            </div>
        </div>
    </div>
</template>

<script>
    import Navbar from './main_navbar.vue';
    import infoEdf from '../backend/projetos.json'; // Import your JSON data

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
    padding: 20px;
}

.info-project{
    display: flex;
    flex-direction: row;
}

.info-text {
    display: flex;
    flex-direction: column;
}

.title, .title-plantas, .title-fotos {
    font-size: 2.8em;
    font-weight: 500;
    color: #000000; 
}

.info {
    font-size: 1.8em;
    font-weight: 400;
    color: #ffffff; 
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

