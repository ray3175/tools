<template>
    <div class="root">
        <nav-bar v-show="navBarShow"></nav-bar>
        <login v-show="!navBarShow"></login>
    </div>
</template>

<script>
    import { AUTH } from "@/config/auth";
    import { getAccountInfo } from "@/api/auth";

    import navBar from "./nav-bar";
    import login from "./login";

    export default {
        name: "index",
        components: {
            "nav-bar": navBar,
            "login": login
        },
        data() {
            return {
                navBarShow: false
            };
        },
        mounted() {
            let authKey = localStorage.getItem(AUTH.key);
            if (authKey) {
                getAccountInfo(authKey, (rsp) => {
                    if (rsp.data.code === 200) {
                        this.navBarShow = true;
                    }
                })
            }
        },
        methods: {
            switchShow() {
                this.navBarShow = !this.navBarShow;
            }
        }
    }
</script>

<style scoped>
    .root {
        position: fixed;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>