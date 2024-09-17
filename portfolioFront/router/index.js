import { createRouter, createWebHistory } from 'vue-router';
import mainPage from '../src/components/main_page.vue';
import edificioPage from '../src/components/project_page.vue';

export default createRouter({
    history: createWebHistory(), 
    routes: [
        { path: '/', component: mainPage },
        { path: '/edificio/:edificioID', component: edificioPage, props: true },
    ],
});

/*import NotFoundPage from '../components/NotFound.vue';

       // considerar também fazer isto com nested routing?
      { path: '/loading', component: LoadingPage},
      { path: '/:notFound(.*)', component: NotFoundPage} // rota para páginas não encontradas
*/