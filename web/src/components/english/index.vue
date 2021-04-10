<template>
    <div>
        <div class="header">
            <nav-bar></nav-bar>
        </div>
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<script>
    import { authVerify } from "@/api/english";

    import navBar from './nav-bar';

    export default {
        name: "english",
        components: {
            "nav-bar": navBar
        },
        mounted () {
            authVerify(this.gotoLogin, (rsp) => {
                if (rsp.data.code !== 200) {
                    alert(rsp.data.msg);
                    this.gotoLogin();
                }
            });
        },
        methods: {
            gotoLogin() {
                this.$router.push({
                    path: "/"
                });
            }
        }
    }
</script>

<style scoped>
</style>
