<template>
    <div class="card" @click="goToPage(item.id)">
        <div class="imagem">
            <img :src="item.main_image" alt="image"/>
        </div>
        <div class="card-info">
            <div class="esq">
                <div class="upper-text">
                    <span>{{ item.titulo }}</span>
                </div>
                <div class="lower-text">
                    <span>{{ item.resumo }}</span>
                </div>
            </div>
            <div class="dir">
                <div class="mid">
                    <span>{{ item.id }}</span>
                    <img src="/svgs/icon_quarto.svg" />
                </div>
                <div class="bottom">
                    <p>{{ item.type }}</p>
                    <img src="/svgs/icon_casabanho.svg" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        item: {
            type: Object, 
            required: true 
        }
    },

    methods: {
        goToPage(itemId) {
            this.$router.push(`/edificio/${itemId}`);
        }
    },
}
</script>

<style scoped>  

.card {
    width: 560px;
    height: 350px;
    background-color: rgba(166, 193, 207, 0.9);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease;
    font-family: 'Inter', sans-serif;
    box-shadow: 10px 10px 10px rgba(50, 50, 50, 0.7),
                -10px -10px 10px rgba(100, 100, 100, 0.6);
    overflow: hidden;
}

@media (max-width: 1250px) {
    .card {
        width: 45%;
        height: auto;
    }
}

@media (max-width: 900px) {
    .card {
        width: 600px;
        height: 400px;
    }
}

@media (max-width: 650px) {
    .card {
        width: 90%;
        height: auto;
    }
}


.card:hover {
    transform: scale(.98);
    cursor: pointer;
    z-index: 2;
    opacity: 85%;
}

.imagem {
    flex: 0 0 60%;
}

.imagem img {
    width: 100%;
    height: 100%;
    object-fit: cover; 
}

.card-info {
    flex: 1; 
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px; 
}

.esq {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.upper-text{
    color: #282828;
    font-weight: 500;
    font-size: 1.5em;
}

.lower-text{
    color: #3F3F3F;
    font-weight: 400;
    font-size: 1em;
}

@media (max-width: 450px) {
    .upper-text{
        font-size: 1.2em;
    }
    
    .lower-text{
        font-size: .8em;
    }
}

.dir {
    display: flex;
    flex-direction: column;
    align-items: flex-end; 
    color: #3F3F3F;
    font-size: 0.75em;
    font-weight: 400;
    text-align: right;
}

.top, .mid, .bottom {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.top img, .mid img, .bottom img {
    margin-left: 5px; 
}

.mid span {
    padding-right: 0.18em; 
}

.bottom span {
    padding-right: 0.53em; 
}
</style>