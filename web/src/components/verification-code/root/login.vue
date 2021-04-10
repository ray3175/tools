<template>
    <div class="login shadow-lg rounded">
        <div class="row">
            <div class="col">
                <div class="header">
                    <b>{{ platformName }}</b>
                </div>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-3 col-form-label" for="login-self-user">用户名</label>
            <div class="col-9">
                <input v-model="user" id="login-self-user" class="form-control" type="text" placeholder="...">
            </div>
        </div>
        <div class="form-group row">
            <label class="col-3 col-form-label" for="login-self-password">密码</label>
            <div class="col-9">
                <input v-model="password" id="login-self-password" class="form-control" type="password" placeholder="...">
            </div>
        </div>
        <div class="form-group row">
            <div class="form-check self-is-auto-login">
                <input v-model="rememberPassword" id="auto-login" class="form-check-input" type="checkbox" >
                <label class="form-check-label" for="auto-login">记住密码</label>
            </div>
        </div>
        <div class="form-group row self-button">
            <button @click="loginAction()" class="btn btn-primary btn-lg shadow-lg rounded self-button-left" type="button">确认</button>
            <button @click="switchToUserInfo()" class="btn btn-dark btn-lg shadow-lg rounded self-button-right" type="button">取消</button>
        </div>
    </div>
</template>

<script>
    import { getPlatform, setPlatformUserPassword } from "../common";

    export default {
        name: "login",
        props: ["platformName"],
        data() {
            return {
                user: null,
                password: null,
                rememberPassword: true,
            };
        },
        watch: {
            platformName(value) {
                let platform = getPlatform(this.platformName);
                if (platform) {
                    this.user = platform.user;
                    this.password = platform.password;
                }
            }
        },
        methods: {
            switchToUserInfo() {
                this.$parent.switchLoginShow();
            },
            loginAction() {
                this.$parent.autoLogin(this.platformName, this.user, this.password);
                if (this.rememberPassword) {
                    setPlatformUserPassword(this.platformName, this.user, this.password);
                } else {
                    localStorage.clear();
                }
            }
        }
    }
</script>

<style scoped>
    .login {
        position: relative;
        width: 380px;
        margin: 0 auto;
        border: 1px solid blueviolet;
        border-radius: 10px;
        padding: 40px;
    }

    .login .header {
        font-size: 36px;
    }

    .login .row {
        margin-top: 20px;
    }

    .login .self-is-auto-login {
        margin-left: 17px;
    }

    .login .self-button {
        margin-top: 30px;
        margin-bottom: 25px;
    }

    .login .self-button-left {
        margin-left: 5%;
    }

    .login .self-button-right {
        margin-left: 45%;
    }
</style>
