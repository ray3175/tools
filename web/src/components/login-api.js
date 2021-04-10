import { getHashAccount, registerAccount } from "@/api/auth";
import { AUTH } from "@/config/auth";

const loginApi = {
    name: "login-api",
    methods: {
        loginClick() {
            if (this.account && this.password) {
                getHashAccount(this.account, this.password, (rsp) => {
                    if (rsp.data.code === 200) {
                        localStorage.setItem(AUTH.key, rsp.data.data)
                        localStorage.setItem("xy-account", this.account);
                        if (this.rememberPasswordChecked) {
                            localStorage.setItem("xy-password", this.password);
                        }
                        this.$parent.navBarShow = true;
                    } else {
                        alert(rsp.data.msg);
                    }
                })
            } else {
                alert("请输入用户名和密码！");
            }
        },
        registAction() {
            if (this.account && this.password && this.idCard && this.name && this.phone && this.mail) {
                if (this.password === this.confirmPassword) {
                    registerAccount(this.account, this.password, this.idCard, this.name, this.phone, this.mail, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.loginClick();      // 注册成功后自动登录！
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                } else {
                    alert("两次输入的密码不一致！");
                }
            } else {
                alert("请将信息填写完整！");
            }
        },
        cursorGotoPassword() {
            $("#password").select();
        }
    }
};


export { loginApi };
