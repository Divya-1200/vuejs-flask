import Vue from 'vue';
import VueRouter from 'vue-router';
import Frontview from './src/views/Frontview.vue';


Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes:[
        {
            path:'/',
            name:'frontview',
            component: Frontview,
        },

            
    ],
})