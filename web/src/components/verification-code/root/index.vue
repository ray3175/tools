<template>
    <div>
        <div v-show="!platformSelect" class="root">
            <platform-select></platform-select>
        </div>
        <div v-show="platformSelect" class="root login">
            <login v-show="loginShow" :platformName="platformName"></login>
            <user-info ref="user" v-show="!loginShow" :platformName="platformName" :userName="user" :userMoney="money" :userToken="token"></user-info>
        </div>
    </div>
</template>

<script>
    import { rootApi } from "./api";
    import { getPlatform } from "../common";

    import platformSelect from "./platform-select";
    import userInfo from "./user-info";
    import login from "./login";

    export default {
        name: "root",
        mixins: [rootApi],
        components: {
            login,
            "user-info": userInfo,
            "platform-select": platformSelect
        },
        data() {
            return {
                platformSelect: false,
                loginShow: false,
                token: null,
                user: null,
                money: null,

                platformName: ""
            };
        },
        methods: {
            init() {
                let platform = getPlatform(this.platformName);
                if (platform.user && platform.password) {
                    this.autoLogin(this.platformName, platform.user, platform.password);
                }
            },
            selectPlatform(name) {
                this.$self.verificationCode.name = this.platformName = name;
                this.platformSelect = true;
                this.init();
            },
            switchLoginShow() {
                this.loginShow = !this.loginShow;
            }
        }
    }
</script>

<style scoped>
    .root {
        margin-top: 50px;
    }

    .login {
        position: relative;
        text-align: center;
        vertical-align: middle;
    }
</style>
