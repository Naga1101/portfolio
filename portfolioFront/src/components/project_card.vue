<template>
    
    <div class= "card" @click="goToPage(item.id)">
        <div class= "imagem">
            <img src="/images/casa.png" alt="image"/>
        </div>
        <div class= "card-info">
            <div class= "esq">
                <div class= "upper-text">
                    <span>Vila Moleza</span>
                </div>
                <div class= "lower-text">
                    <span>Espaço de harmonia entre roby reles e natureza</span>
                </div>
            </div>
            <div class= "dir">
                <div class= "top">
                    <span>200m<sup>2</sup></span>
                    <img src="/svgs/icon_casa.svg"/>
                </div>
                <div class= "mid">
                    <span>{{ item.id }}</span>
                    <img src="/svgs/icon_quarto.svg"/>
                </div>
                <div class= "bottom">
                    <p>{{ item.teste }}</p>
                    <img src="/svgs/icon_casabanho.svg"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        item: Object
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
    width: 450px;
    height: 350px;
    background-color: rgba(111, 78, 55, 0.8);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease;
    font-family: 'Inter', sans-serif;
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
    color: #000000;
    font-weight: 500;
    font-size: 1.5em;
}

.lower-text{
    color: #FFFFFF;
    font-weight: 400;
    font-size: 1em;
}

.dir {
    display: flex;
    flex-direction: column;
    align-items: flex-end; 
    color: #FFFFFF;
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

.top span {
    padding-right: 0.14em; 
}
.mid span {
    padding-right: 0.18em; 
}

.bottom span {
    padding-right: 0.53em; 
}
</style>