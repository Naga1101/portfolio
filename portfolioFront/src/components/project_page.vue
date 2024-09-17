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

        </div>
        <div class= "fotos">

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
    background-color: rgba(148, 140, 131, 0.75); /* Valid RGBA value */
    font-family: 'Inter', sans-serif;
}

.info-project{
    display: flex;
    flex-direction: row;
}

.info-text {
    display: flex;
    flex-direction: column;
}

.title {
    font-size: 3em;
    font-weight: 500;
    color: #000000; 
}

.info {
    font-size: 2em;
    font-weight: 400;
    color: #ffffff; 
}
</style>

