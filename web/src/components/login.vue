<template>
    <div>
        <div class="layout">
            <div class="form-login">
                <h1 class="form-login-title">用户登录</h1>
                <div class="form-login-input">
                    <input v-model="account" @keydown.enter="cursorGotoPassword" id="account" class="form-login-input-input" type="text" autocomplete="off" placeholder="用户名。。。">
                </div>
                <div class="form-login-input">
                    <input v-model="password" @keydown.enter="loginClick()" id="password" class="form-login-input-input" type="password" autocomplete="off" placeholder="密码。。。">
                </div>
                <div class="form-remember-password">
                    <input v-model="rememberPasswordChecked" id="self-login-remember-password" type="checkbox">
                    <label for="self-login-remember-password">&nbsp;&nbsp;记住密码</label>
                </div>
                <button @click="registSwitch()" class="form-regist-button self-form-button">注册</button>
                <button @click="loginClick()" class="form-login-button self-form-button">登录</button>
            </div>
        </div>
        <div v-show="registShow" class="regist-shield">
            <div class="regist-layout-main">
                <h1 class="form-login-title">用户注册</h1>
                <div class="form-login-input">
                    <input v-model="account" class="form-login-input-input" type="text" autocomplete="off" placeholder="用户名。。。">
                </div>
                <div class="form-login-input">
                    <input v-model="password" class="form-login-input-input" type="password" autocomplete="off" placeholder="密码。。。">
                </div>
                <div class="form-login-input">
                    <input v-model="confirmPassword" class="form-login-input-input" type="password" autocomplete="off" placeholder="确认密码。。。">
                </div>
                <div class="form-login-input">
                    <input v-model="idCard" class="form-login-input-input" type="text" autocomplete="off" placeholder="身份证号码。。。">
                </div>
                <div class="form-login-input">
                    <input v-model="name" class="form-login-input-input" type="text" autocomplete="off" placeholder="姓名。。。">
                </div>
                <div class="form-login-input">
                    <input v-model="phone" class="form-login-input-input" type="text" autocomplete="off" placeholder="手机号。。。">
                </div>
                <div class="form-login-input">
                    <input v-model="mail" class="form-login-input-input" type="text" autocomplete="off" placeholder="邮箱。。。">
                </div>
                <button @click="registAction()" class="form-regist-button self-form-button">注册</button>
                <button @click="registSwitch()" class="form-cancel-button self-form-button">取消</button>
            </div>
        </div>
    </div>
</template>

<script>
    import { loginApi } from "./login-api";

    export default {
        name: "login",
        mixins: [loginApi],
        data() {
            return {
                registShow: false,

                account: null,
                password: null,
                rememberPasswordChecked: true,

                confirmPassword: null,
                idCard: null,
                name: null,
                phone: null,
                mail: null
            };
        },
        mounted() {
            this.account = localStorage.getItem("xy-account");
            this.password = localStorage.getItem("xy-password");
        },
        methods: {
            registSwitch() {
                this.registShow = !this.registShow;
            }
        }
    }
</script>

<style scoped>
    .regist-shield {
        position: fixed;
        background: rgba(0,0,0,0.6);
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .layout {
        width: 400px;
        height: 560px;
        border: 1px solid blueviolet;
        border-radius: 10px;
        display: flex;
        position: relative;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        padding: 20px;
    }

    .form-login {
        width: 300px;
        position: relative;
    }

    .form-login-title {
        text-align: center;
        font-size: 40px;
        margin: 15px 0 20px 0;
        letter-spacing: 0.1em;
        font-weight: 700;
        line-height: 1.1;
    }

    .form-login-input-input {
        width: 100%;
        background: none;
        padding: 18px 15px;
        color: violet;
        border: none;
        font-weight: 600;
        letter-spacing: 0.035em;
    }

    .form-login-input {
        width: 100%;
        position: relative;
        margin-bottom: 25px;
        border: 1px solid orange;
        border-radius: 3px;
        transition: all 0.3s ease;
    }

    .form-remember-password {
        margin-bottom: 12px;
    }

    .self-form-button {
        cursor: pointer;
        font-size: 20px;
        width: 100%;
        padding: 20px;
        outline: none;
        position: relative;
        border: none;
        border-radius: 3px;
        margin-bottom: 25px;
        font-weight: 700;
        letter-spacing: 0.1em;
        transition: all 0.3s ease;
        overflow: hidden;
    }

    .form-regist-button {
        color: orange;
        background: yellowgreen;
    }

    .form-login-button {
        color: orange;
        background: dodgerblue;
    }

    .form-cancel-button {
        color: orange;
        background: darkgrey;
    }

    .form-regist-button:hover, .form-login-button:hover, .form-cancel-button:hover {
        color: yellow;
        background: black;
    }

    .regist-layout-main {
        width: 400px;
        height: 560px;
        background: white;
        border: 1px solid blueviolet;
        border-radius: 10px;
        position: relative;
        padding: 30px;
        overflow-y: scroll;
    }

    /* 滚动条消失 */
    .regist-layout-main::-webkit-scrollbar {
        width: 4px;
        height: 4px;
    }

    /* 滚动条颜色 */
    .regist-layout-main::-webkit-scrollbar-thumb {
        border-radius: 5px;
        -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
        background: rgba(0,0,0,0.2);
    }

    /* 滚动条轨道 */
    .regist-layout-main::-webkit-scrollbar-track {
        -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
        border-radius: 0;
        background: rgba(0,0,0,0.1);
    }
</style>
