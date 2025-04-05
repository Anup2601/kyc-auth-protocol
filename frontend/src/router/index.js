import { createRouter, createWebHistory } from 'vue-router';
import LoginRegister from "../components/Login.vue";
import RegisterCompany from '../components/RegisterCompany.vue';
import RegisterUser from '../components/RegisterUser.vue';
import Main from '../components/mainpage.vue';

const routes = [
  {
    path: '/',
    name: 'LoginRegister',
    component: LoginRegister,
  },
  {
    path: '/registeruser',
    name: 'Register', 
    component: RegisterUser,
  },
  {
    path: '/registercompany',
    name: 'RegisterCompany',
    component: RegisterCompany
  },
  {
    path: '/main',
    name: 'Main',
    component: Main
},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;