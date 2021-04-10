import Vue from 'vue';
import Router from 'vue-router';
import index from '@/components';
import verificationCode from '@/components/verification-code';
import english from '@/components/english';
import { verificationCodeChildren } from "./verification-code";
import { englishChildren } from "./english";


Vue.use(Router);

export default new Router({
    routes: [
        {
            path: "/",
            redirect: "/index"
        },
        {
            path: "/index",
            name: "index",
            component: index
        },
        {
            path: "/verification-code",
            name: "verification-code",
            component: verificationCode,
            children: verificationCodeChildren
        },
        {
            path: "/english",
            name: "english",
            component: english,
            children: englishChildren
        }
    ]
});
