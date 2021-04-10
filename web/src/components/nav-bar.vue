<template>
    <div class="self-root">
        <div v-for="(obj, index) in navList" class="self-div self-normal">
            <router-link class="nav-link self-a-normal" :to="obj.path">{{ obj.name }}</router-link>
        </div>
        <div class="self-div self-logout">
            <a @click="logoutClick()" class="nav-link" href="javascript:void(0)">注销</a>
        </div>
    </div>
</template>

<script>
    import { logoutClick } from "./logout-api";

    export default {
        name: "nav-bar",
        data() {
            return {
                navList: [
                    {
                        name: "验证码",
                        path: "/verification-code"
                    },
                    {
                        name: "英语",
                        path: "/english"
                    }
                ]
            };
        },
        methods: {
            logoutClick() {
                logoutClick();
                this.$parent.switchShow();
            }
        }
    }
</script>

<style scoped>
    .self-root {
        width: 100%;
    }

    .self-div {
        cursor: pointer;
        height:100px;
        margin: 20px 50px 20px 50px;
        text-align: center;
        padding-top: 20px;
        font-size: xx-large;
        font-weight: bolder;
        border-radius: 10px;
    }

    .self-normal {
        background: rgba(59, 29, 117, 0.64);
    }

    .self-normal:hover {
        background: green;
    }

    .self-logout {
        background: red;
    }

    .self-a-normal {
        color: white;
    }

    .self-a-normal:hover {
        color: yellow;
    }
</style>
