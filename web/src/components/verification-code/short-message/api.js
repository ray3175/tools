import {
    getPhoneNumberKeKe,
    releaseAllPhoneNumberKeKe,
    getMessageKeKe,
    releasePhoneNumberKeKe,
    removePhoneNumberKeKe
} from "@/api/code-platform-keke";
import {
    getPhoneNumberJinDou,
    getSelfDefinePhoneNumberJinDou,
    releasePhoneNumberJinDou,
    removePhoneNumberJinDou,
    getMessageJinDou
} from "@/api/code-platform-jindou";
import {
    getPhoneNumberMiYi,
    getSelfDefinePhoneNumberMiYi,
    releasePhoneNumberMiYi,
    removePhoneNumberMiYi,
    getMessageMiYi
} from "@/api/code-platform-miyi";


const shortMessageApi = {
    name: "short-message-api",
    methods: {
        getPhoneNumber() {
            if (this.token) {
                if (this.name === "可可接码平台") {
                    getPhoneNumberKeKe(this.token, this.item, this.multi, this.type, (rsp) => {
                        if (rsp.data === "0") {
                            alert("Token已失效，请重新登录！");
                        } else if (rsp.data === "-1") {
                            alert("当前没有合条件号码！");
                        } else if (rsp.data === "-2") {
                            alert("提交取号任务超量，请稍后再试！");
                        } else if (rsp.data === "-3") {
                            alert("获取号码数量超量，请释放已经做完任务不使用的号码，以便获取新号码！");
                        } else if (rsp.data === "-4") {
                            alert("该项目已经被禁用，暂停取号做业务！");
                        } else if (rsp.data === "-8") {
                            alert("帐户余额不足！");
                        } else if (rsp.data === "-11") {
                            alert("端口繁忙被占用，请稍后再试！");
                        } else if (rsp.data === "-12") {
                            alert("该项目不能以获取号码方式工作！");
                        } else if (rsp.data === "-15") {
                            alert("该号码已被卡商删除！");
                        } else {
                            let phoneMatch = rsp.data.match("hm=([0-9,]+)");
                            if (phoneMatch) {
                                let phoneList = phoneMatch[1].split(",");
                                let tmpDict = {};
                                let tmpMessageDict = {};
                                for (let i in phoneList) {
                                    tmpDict[phoneList[i]] = {
                                        unreadInfoNumber: 0,
                                        timer: true
                                    };
                                    tmpMessageDict[phoneList[i]] = {
                                        code: "-",
                                        text: "-"
                                    };
                                }
                                Object.assign(tmpDict, this.phoneDict);
                                Object.assign(tmpMessageDict, this.messageDict);
                                this.phoneDict = tmpDict;
                                this.messageDict = tmpMessageDict;
                                this.checkPhoneNumber();
                            }
                        }
                    });
                } else if (this.name === "筋斗云接码平台") {
                    if (this.type.length === 11) {
                        getSelfDefinePhoneNumberJinDou(this.token, this.item, this.type, (rsp) => {
                            if (rsp.data.code === 200) {
                                let data = rsp.data.data;
                                if (data.slice(0, 1) === "0") {
                                    let phone = data.slice(2, 13);
                                    let tmpDict = {};
                                    let tmpMessageDict = {};
                                    tmpDict[phone] = {
                                        unreadInfoNumber: 0,
                                        timer: true
                                    };
                                    tmpMessageDict[phone] = {
                                        code: "-",
                                        text: "-"
                                    };
                                    Object.assign(tmpDict, this.phoneDict);
                                    Object.assign(tmpMessageDict, this.messageDict);
                                    this.phoneDict = tmpDict;
                                    this.messageDict = tmpMessageDict;
                                } else {
                                    alert(data);
                                }
                            } else {
                                alert(rsp.data.msg);
                            }
                        });
                    } else {
                        for (let i=0; i < Number(this.multi); i++) {
                            getPhoneNumberJinDou(this.token, this.item, this.type, (rsp) => {
                                if (rsp.data.code === 200) {
                                    let phone = rsp.data.data.slice(2, 13);
                                    let tmpDict = {};
                                    let tmpMessageDict = {};
                                    tmpDict[phone] = {
                                        unreadInfoNumber: 0,
                                        timer: true
                                    };
                                    tmpMessageDict[phone] = {
                                        code: "-",
                                        text: "-"
                                    };
                                    Object.assign(tmpDict, this.phoneDict);
                                    Object.assign(tmpMessageDict, this.messageDict);
                                    this.phoneDict = tmpDict;
                                    this.messageDict = tmpMessageDict;
                                    this.checkPhoneNumber();
                                } else {
                                    alert(rsp.data.msg);
                                }
                            });
                        }
                    }
                } else if (this.name === "米宜接码平台") {
                    if (this.type.length === 11) {
                        getSelfDefinePhoneNumberMiYi(this.token, this.item, this.type, (rsp) => {
                            if (rsp.data.code === 200) {
                                let data = rsp.data.data;
                                if (data.slice(0, 1) === "0") {
                                    let phone = data.slice(2, 13);
                                    let tmpDict = {};
                                    let tmpMessageDict = {};
                                    tmpDict[phone] = {
                                        unreadInfoNumber: 0,
                                        timer: true
                                    };
                                    tmpMessageDict[phone] = {
                                        code: "-",
                                        text: "-"
                                    };
                                    Object.assign(tmpDict, this.phoneDict);
                                    Object.assign(tmpMessageDict, this.messageDict);
                                    this.phoneDict = tmpDict;
                                    this.messageDict = tmpMessageDict;
                                } else {
                                    alert(data);
                                }
                            } else {
                                alert(rsp.data.msg);
                            }
                        });
                    } else {
                        for (let i=0; i < Number(this.multi); i++) {
                            getPhoneNumberMiYi(this.token, this.item, this.type, (rsp) => {
                                if (rsp.data.code === 200) {
                                    let phone = rsp.data.data.slice(2, 13);
                                    let tmpDict = {};
                                    let tmpMessageDict = {};
                                    tmpDict[phone] = {
                                        unreadInfoNumber: 0,
                                        timer: true
                                    };
                                    tmpMessageDict[phone] = {
                                        code: "-",
                                        text: "-"
                                    };
                                    Object.assign(tmpDict, this.phoneDict);
                                    Object.assign(tmpMessageDict, this.messageDict);
                                    this.phoneDict = tmpDict;
                                    this.messageDict = tmpMessageDict;
                                    this.checkPhoneNumber();
                                } else {
                                    alert(rsp.data.msg);
                                }
                            });
                        }
                    }
                }
            } else {
                alert("未检测到用户Token，请重新登录！");
            }
        },
        checkPhoneNumber() {
            let filterPhone = [];
            if (this.filterPhonePrefix) {
                filterPhone = this.filterPhonePrefix.split("||");
            }
            let needRepeatGetPhoneNumber = 0;
            let tmpDeletePhoneList = [];
            for (let phone in this.phoneDict) {
                if (filterPhone.filter((value) => { return phone.startsWith(value); }).length) {
                    needRepeatGetPhoneNumber++
                    tmpDeletePhoneList.push(phone);
                }
            }
            for (let phone in tmpDeletePhoneList) {
                delete this.phoneDict[tmpDeletePhoneList[phone]];
                delete this.messageDict[tmpDeletePhoneList[phone]];
                this.phoneAlertList.push(tmpDeletePhoneList[phone]);
            }
            if (needRepeatGetPhoneNumber) {
                this.multi = needRepeatGetPhoneNumber;
                this.getPhoneNumber();
            }
        },
        releaseAllPhoneNumber() {
            if (this.token) {
                if (this.name === "可可接码平台") {
                    releaseAllPhoneNumberKeKe(this.token, (rsp) => {
                        if (rsp.data === "0") {
                            alert("Token已失效，请重新登录！");
                        } else if (rsp.data === "-1") {
                            alert("全部释放失败！");
                        } else {
                            alert("全部释放成功！");
                            this.phoneDict = {};
                            this.phone = null;
                            this.messageDict = {};
                        }
                    });
                } else if (this.name === "筋斗云接码平台") {
                    releasePhoneNumberJinDou(this.token, this.item, null, (rsp) => {
                        if (rsp.data.code === 200) {
                            alert(rsp.data.data);
                            this.phoneDict = {};
                            this.phone = null;
                            this.messageDict = {};
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                } else if (this.name === "米宜接码平台") {
                    releasePhoneNumberMiYi(this.token, this.item, null, (rsp) => {
                        if (rsp.data.code === 200) {
                            alert(rsp.data.data);
                            this.phoneDict = {};
                            this.phone = null;
                            this.messageDict = {};
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                }
            } else {
                alert("未检测到用户Token，请重新登录！");
            }
        },
        getPhoneMessage() {
            let phone = this.phone;
            if (phone) {
                if (this.name === "可可接码平台") {
                    getMessageKeKe(this.token, phone, this.item, (rsp) => {
                        if (rsp.data === "0") {
                            alert("Token已失效，请重新登录！");
                        } else if (rsp.data === "1") {
                            alert("接码平台还未收到信息，请稍后再试！");
                        } else if (rsp.data === "-1") {
                            alert("该号码已被接码平台注销！");
                        } else if (rsp.data === "-2") {
                            alert("该业务已被注销！");
                        } else if (rsp.data === "-3") {
                            alert("该业务异常终止！");
                        } else if (rsp.data === "-8") {
                            alert("余额不足！");
                        } else if (rsp.data === "-9") {
                            alert("接码平台数据出错！");
                        } else {
                            this.messageDict[phone].text = rsp.data;
                            if (typeof (rsp.data) === "string") {
                                let codeRegex = rsp.data.match("激活码为([0-9]+)");
                                if (codeRegex && codeRegex.length) {
                                    this.messageDict[phone].code = codeRegex[1];
                                }
                            }
                        }
                    });
                } else if (this.name === "筋斗云接码平台") {
                    getMessageJinDou(this.token, this.item, phone, (rsp) => {
                        if (rsp.data.code === 200) {
                            let data = rsp.data.data;
                            this.messageDict[phone].text = data;
                            let codeRegex = data.match("激活码为([0-9]+)");
                            if (codeRegex && codeRegex.length) {
                                this.messageDict[phone].code = codeRegex[1];
                            }
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                } else if (this.name === "米宜接码平台") {
                    getMessageMiYi(this.token, this.item, phone, (rsp) => {
                        if (rsp.data.code === 200) {
                            let data = rsp.data.data;
                            this.messageDict[phone].text = data;
                            let codeRegex = data.match("激活码为([0-9]+)");
                            if (codeRegex && codeRegex.length) {
                                this.messageDict[phone].code = codeRegex[1];
                            }
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                }
            } else {
                alert("请先选择要操作的号码！");
            }
        },
        releasePhoneNumber() {
            if (this.phone) {
                if (this.name === "可可接码平台") {
                    releasePhoneNumberKeKe(this.token, this.phone, (rsp) => {
                        if (rsp.data === "0") {
                            alert("Token已失效，请重新登录！");
                        } else if (rsp.data === "-1") {
                            alert("释放号码失败！");
                        } else {
                            this.releasePhone(this.phone);
                            alert("释放成功！");
                        }
                    });
                } else if (this.name === "筋斗云接码平台") {
                    releasePhoneNumberJinDou(this.token, this.item, this.phone, (rsp) => {
                        if (rsp.data.code === 200) {
                            alert(rsp.data.data);
                            this.releasePhone(this.phone);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                } else if (this.name === "米宜接码平台") {
                    releasePhoneNumberMiYi(this.token, this.item, this.phone, (rsp) => {
                        if (rsp.data.code === 200) {
                            alert(rsp.data.data);
                            this.releasePhone(this.phone);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                }
            } else {
                alert("请先选择要操作的号码！");
            }
        },
        removePhoneNumber() {
            if (this.phone) {
                if (this.name === "可可接码平台") {
                    removePhoneNumberKeKe(this.token, this.phone, this.item, (rsp) => {
                        if (rsp.data === "0") {
                            alert("Token已失效，请重新登录！");
                        } else if (rsp.data === "-1") {
                            alert("拉黑失败！");
                        } else if (rsp.data === "-1") {
                            alert("该号码已被拉黑，请勿重复！");
                        } else {
                            this.releasePhone(this.phone);
                            alert("拉黑成功！");
                        }
                    });
                } else if (this.name === "筋斗云接码平台") {
                    removePhoneNumberJinDou(this.token, this.item, this.phone, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.releasePhone(this.phone);
                            alert(rsp.data.data);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                } else if (this.name === "米宜接码平台") {
                    removePhoneNumberMiYi(this.token, this.item, this.phone, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.releasePhone(this.phone);
                            alert(rsp.data.data);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                }
            } else {
                alert("请先选择要操作的号码！");
            }
        }
    }
};


export { shortMessageApi };
