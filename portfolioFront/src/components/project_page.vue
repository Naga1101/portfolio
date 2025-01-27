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
        </div> 
        <div v-if="item.plantas && item.plantas.length" class="plantas">
            <div class="title-plantas">
                <span>Plantas</span>                
            </div>
            <section class="container">
                <div class="slider-wrapper">
                    <div class="slider" ref="slider">
                        <div v-for="(foto, index) in item.plantas" :key="index" class="foto-item" :id="'slide-' + index" :ref="'slide-' + index">
                            <img class="project-image" :src="foto" :alt="'image' + index" @click="openMedia(index, 'plantas')"/>
                            <img class="overlay-svg" src="/svgs/expand_image.svg" alt="Icon"/>
                        </div>
                    </div>
                    <div class="slider-nav">
                        <a v-for="(foto, index) in item.plantas" :key="'nav-' + index" :href="'#slide-' + index"></a>
                    </div>
                </div>
            </section>
            <div v-if="currentMediaType == 'plantas'" class="overlay" @click="closeMedia">
                <div class="navigation" @click.stop>
                    <button 
                        class="next_prev_button" 
                        @click="prevMedia" 
                        :disabled="currentIndex === 0">
                        <img class="rotate-180" src="/svgs/next_back_arrow.svg"/>
                    </button>
                    <img :src="item.plantas[currentIndex]" class="enlarged-projectImage"/>
                    <button 
                        class="next_prev_button" 
                        @click="nextMedia" 
                        :disabled="currentIndex === item.plantas.length - 1">
                        <img src="/svgs/next_back_arrow.svg"/>
                    </button>
                </div>
            </div>
        </div>
        <div class="fotos">
            <div class="title-fotos">
                <span>Imagens e 3Ds</span>                
            </div>
            <div class="img-grid">
                <div v-for="(foto, index) in item.fotos" :key="index" class="foto-item">
                    <img class="project-image" :src="foto" :alt="'image' + index" @click="openMedia(index, 'fotos')"/>
                    <img class="overlay-svg" src="/svgs/expand_image.svg" alt="Icon"/>
                </div>
            </div>
            <div v-if="currentMediaType == 'fotos'" class="overlay" @click="closeMedia">
                <div class="navigation" @click.stop>
                    <button 
                        class="next_prev_button" 
                        @click="prevMedia" 
                        :disabled="currentIndex === 0">
                        <img class="rotate-180" src="/svgs/next_back_arrow.svg"/>
                    </button>
                    <img :src="item.fotos[currentIndex]" class="enlarged-projectImage"/>
                    <button 
                        class="next_prev_button" 
                        @click="nextMedia" 
                        :disabled="currentIndex === item.fotos.length - 1">
                        <img src="/svgs/next_back_arrow.svg"/>
                    </button>
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
                currentIndex: null,
                currentMediaType: null,
            };
        },

        created() {
            this.fetchItem();
        },

        methods: {
            fetchItem() {
                this.item = infoEdf.edfInfo.find(projeto => String(projeto.id) === this.edificioID);
            },

            openMedia(index, type) {
                this.currentIndex = index;
                this.currentMediaType = type;
            },

            closeMedia() {
                this.scrollToCurrentImage();
                this.currentIndex = null;
                this.currentMediaType = null;
            },

            prevMedia() {
                if (this.currentIndex > 0) {
                    this.currentIndex--;
                }
            },

            nextMedia() {
                if (this.currentMediaType === 'fotos' && this.currentIndex < this.item.fotos.length - 1) {
                    this.currentIndex++;
                } else if (this.currentMediaType === 'plantas' && this.currentIndex < this.item.plantas.length - 1) {
                    this.currentIndex++;
                }
            },

            scrollToCurrentImage() {
                if (this.currentIndex === null || this.currentIndex === undefined) {
                    console.warn("Current index is not set.");
                    return;
                }

                this.$nextTick(() => {
                    const slider = this.$refs.slider;

                    if (!slider) {
                    console.error("Slider element not found.");
                    return;
                    }

                    // Attempt to locate the current slide by its ID directly
                    const currentSlide = document.getElementById(`slide-${this.currentIndex}`);

                    if (!currentSlide) {
                    console.error(`Slide with ID "slide-${this.currentIndex}" not found.`);
                    return;
                    }

                    // Smooth scroll the slider to align with the current slide
                    slider.scrollTo({
                    left: currentSlide.offsetLeft,
                    behavior: "smooth",
                    });

                    console.log(`Scrolled to slide ${this.currentIndex}.`);
                });
            }
        }
    }
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
    font-family: 'Inter', sans-serif;
    border-bottom: 1.5px solid rgba(0, 0, 0, 0.8);
}

.button-placeholder {
    width: auto;
    height: 2.5em;
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
    border-radius: 10px;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
}

.return_button img {
    height: 25px;
    object-fit: contain;
    fill: #282828;
}

.return_button span {
    padding-left: 0.35em;
}

.right_data {
    display: inline-flex;
    align-items: center;
}

.page {
    box-sizing: border-box;
    padding: 0px;
}

.info-project {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0;
    width: 100%;
    max-height: 500px;
    background-color: #CABBA9;
    box-sizing: border-box;
    cursor: default;
}

.info-text {
    display: flex;
    flex-direction: column;
    padding-left: 1.5%;
    max-width: 85%; 
    padding-right: 30px;
}

.main_image {
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
    cursor: default;
}

.info {
    font-size: 1.8em;
    font-weight: 400;
    color: #282828; 
}

/** Parte das plantas das casas */

.plantas {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    padding-left: 1.5%;
}

.container {
    padding: 1.5rem;
}

.slider-wrapper {
    position: relative;
    max-width: 100rem;
    height: auto;
    margin: 0 auto;
}

.slider {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;    
}

.slider div {
    flex: 1 0 45%;
    scroll-snap-align: start;
    object-fit: cover;
}

.slider nav {
    display: flex;
    column-gap: 1rem;
    position: absolute;
    bottom: 1.25rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
}

.slider-nav a {
    width: 20rem;
    height: 20rem;
    border-radius: 20rem;
    background-color: rgb(233, 225, 209);
    opacity: 0.75;
    transition: ease 250ms;
}

.slider-nav a:hover {
    opacity: 1;
}

/** Parte das fotos das casas */

.fotos {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    padding-left: 1.5%;
}

.img-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr); 
    align-items: center;
    gap: 10px
}

.foto-item {
    margin: 10px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    position: relative;
    max-width: 750px;
    max-height: 350px;
}

.project-image {
    width: 100%; 
    height: auto; 
    border-radius: 5px;
    z-index: 1;
    transition: opacity 0.3s ease; 
}

.foto-item:hover .project-image {
    opacity: 0.85;
    pointer-events: auto;
}

.overlay-svg {
    width: 50px;
    opacity: 0;
    z-index: 2;
    position: absolute;
    bottom: 1rem;
    right: 1rem;
    pointer-events: none;
}

.foto-item:hover .overlay-svg{
    opacity: 1;
    pointer-events: none;
}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    cursor: pointer;
}

.navigation {
    display: flex;
    align-items: center;
}

.enlarged-projectImage {
    max-width: 80%;
    max-height: 80%;
    cursor: default;
}

.next_prev_button {
    background: none;
    border: none;
    cursor: pointer;
    margin: 0 20px;
    opacity: 0.85;
}

.next_prev_button:hover:not(:disabled) {
    opacity: 1;
}

.next_prev_button:active:not(:disabled) {
    opacity: 0.85;
}

button:disabled {
    opacity: 0.4;
    cursor: default;
}

.rotate-180 {
    transform: rotate(180deg);
}
</style>
