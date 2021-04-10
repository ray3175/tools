import {
    loginKeKe,
    getBalanceKeKe
} from "@/api/code-platform-keke";
import {
    loginJinDou,
    getBalanceJinDou
} from "@/api/code-platform-jindou";
import {
    loginMiYi,
    getBalanceMiYi
} from "@/api/code-platform-miyi";
import { CODE_PLATFORM_KEKE, CODE_PLATFORM_JINDOU, CODE_PLATFORM_MIYI } from "@/config/code-platform-info";
import { getPlatform } from "../common";


const rootApi = {
    name: "root-api",
    data() {
        return {
            item: CODE_PLATFORM_KEKE.item.qiaohu,
        }
    },
    methods: {
        getCodePlatformList() {
            return [
                CODE_PLATFORM_KEKE,
                CODE_PLATFORM_JINDOU,
                CODE_PLATFORM_MIYI
            ];
        },
        login(name, user, password, call=null) {
            if (name === "可可接码平台") {
                loginKeKe(user, password, (rsp) => {
                    if (rsp.data === "0") {
                        alert("账号处于禁止使用状态！");
                    } else if (rsp.data === "-1") {
                        alert("调用接口失败！");
                    } else if (rsp.data === "-2") {
                        alert("账户信息错误！");
                    } else if (rsp.data === "-3") {
                        alert("用户名或密码错误！");
                    } else if (rsp.data === "-4") {
                        alert("账号异常！");
                    } else if (rsp.data === "-30") {
                        alert("IP地址异常！");
                    } else {
                        this.token = rsp.data;
                        this.user = user;
                        this.password = password;
                        this.$self.verificationCode.token = this.token;
                        if (call) {
                            call();
                        }
                        if (this.loginShow) {
                            this.switchLoginShow();
                        }
                    }
                });
            } else if (name === "筋斗云接码平台") {
                loginJinDou(user, password, (rsp) => {
                    if (rsp.data.code === 200) {
                        let dataJinDou = rsp.data.data;
                        if (dataJinDou.slice(0, 1) === "0") {
                            this.token = dataJinDou.slice(7);
                            this.user = user;
                            this.password = password;
                            this.$self.verificationCode.token = this.token;
                            if (call) {
                                call(this.token);
                            }
                            if (this.loginShow) {
                                this.switchLoginShow();
                            }
                        } else {
                            alert(dataJinDou);
                        }
                    } else {
                        alert(rsp.data.msg);
                    }
                });
            } else if (name === "米宜接码平台") {
                loginMiYi(user, password, (rsp) => {
                    if (rsp.data.code === 200) {
                        let dataJinDou = rsp.data.data;
                        if (dataJinDou.slice(0, 1) === "0") {
                            this.token = dataJinDou.slice(7);
                            this.user = user;
                            this.password = password;
                            this.$self.verificationCode.token = this.token;
                            if (call) {
                                call(this.token);
                            }
                            if (this.loginShow) {
                                this.switchLoginShow();
                            }
                        } else {
                            alert(dataJinDou);
                        }
                    } else {
                        alert(rsp.data.msg);
                    }
                });
            }
        },
        autoLogin(name, user, password) {
            if (name === "可可接码平台") {
                this.login(name, user, password, () => {
                    getBalanceKeKe(user, password, (rsp) => {
                        this.user = user;
                        this.money = rsp.data;
                    });
                })
            } else if (name === "筋斗云接码平台") {
                this.login(name, user, password, (token) => {
                    getBalanceJinDou(token, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.money = rsp.data.data.slice(2);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                });
            } else if (name === "米宜接码平台") {
                this.login(name, user, password, (token) => {
                    getBalanceMiYi(token, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.money = rsp.data.data.slice(2);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                });
            }
        },
    }
};


export { rootApi };
