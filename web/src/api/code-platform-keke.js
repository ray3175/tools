import axios from 'axios';
import { CODE_PLATFORM_KEKE } from "@/config/code-platform-info";


const loginKeKe = function (user, password, successCall=null, errorCall=null) {
    axios.get(CODE_PLATFORM_KEKE.url + CODE_PLATFORM_KEKE.uri.login, {
        params: {
            name: user,
            psw: password
        }
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const getBalanceKeKe = function (user, password, successCall=null, errorCall=null) {
    axios.get(CODE_PLATFORM_KEKE.url + CODE_PLATFORM_KEKE.uri.balance, {
        params: {
            name: user,
            psw: password
        }
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const getPhoneNumberKeKe = function (token, item, multi=1, type=0, successCall=null, errorCall=null) {
    axios.get(CODE_PLATFORM_KEKE.url + CODE_PLATFORM_KEKE.uri.phone, {
        params: {
            token: token,
            xmid: item,
            sl: multi,
            lx: type,
            a1: "",
            a2: "",
            pk: "",
            ks: 0,
            rj: 0
        }
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const releaseAllPhoneNumberKeKe = function (token, successCall=null, errorCall=null) {
    axios.get(CODE_PLATFORM_KEKE.url + CODE_PLATFORM_KEKE.uri.releasePhoneAll, {
        params: {
            token: token
        }
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const releasePhoneNumberKeKe = function (token, phone, successCall=null, errorCall=null) {
    axios.get(CODE_PLATFORM_KEKE.url + CODE_PLATFORM_KEKE.uri.releasePhone, {
        params: {
            token: token,
            hm: phone
        }
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const removePhoneNumberKeKe = function (token, phone, item, successCall=null, errorCall=null) {
    axios.get(CODE_PLATFORM_KEKE.url + CODE_PLATFORM_KEKE.uri.removePhone, {
        params: {
            token: token,
            hm: phone,
            xmid: item
        }
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const getMessageKeKe = function (token, phone, item, successCall=null, errorCall=null) {
    axios.get(CODE_PLATFORM_KEKE.url + CODE_PLATFORM_KEKE.uri.getMessage, {
        params: {
            token: token,
            hm: phone,
            xmid: item
        }
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};


export {
    loginKeKe,
    getBalanceKeKe,
    getPhoneNumberKeKe,
    releaseAllPhoneNumberKeKe,
    releasePhoneNumberKeKe,
    removePhoneNumberKeKe,
    getMessageKeKe
};
