import axios from 'axios';
import { AUTH } from "@/config/auth";
import { CODE_PLATFORM } from "@/config/code-platform";
import { CODE_PLATFORM_MIYI } from "@/config/code-platform-info";


const loginMiYi = function (user, password, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_MIYI.url + CODE_PLATFORM_MIYI.uri.login,
        params: {
            userName: user,
            password: password
        }
    }, {
        headers: headers
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

const getBalanceMiYi = function (_token, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_MIYI.url + CODE_PLATFORM_MIYI.uri.balance,
        params: {
            token: _token
        }
    }, {
        headers: headers
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

const getPhoneNumberMiYi = function (_token, item, type, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    if (type === "0") {
        type = "exclude4";
    } else if (type === "1") {
        type = "unlimit";
    } else if (type === "2") {
        type = "include2";
    } else if (type === "3") {
        type = "include3";
    } else if (type === "4") {
        type = "include1";
    } else if (type === "5") {
        type = "include4";
    }
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_MIYI.url + CODE_PLATFORM_MIYI.uri.phone,
        params: {
            token: _token,
            sid: item,
            operator: type
        }
    }, {
        headers: headers
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

const getSelfDefinePhoneNumberMiYi = function (_token, item, type, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_MIYI.url + CODE_PLATFORM_MIYI.uri.selfDefinePhone,
        params: {
            token: _token,
            sid: item,
            phone: type
        }
    }, {
        headers: headers
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

const releasePhoneNumberMiYi = function (_token, item, phone=null, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_MIYI.url + CODE_PLATFORM_MIYI.uri.releasePhone,
        params: {
            token: _token,
            sid: item,
            phone: phone
        }
    }, {
        headers: headers
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

const removePhoneNumberMiYi = function (_token, item, phone=null, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_MIYI.url + CODE_PLATFORM_MIYI.uri.removePhone,
        params: {
            token: _token,
            sid: item,
            phone: phone
        }
    }, {
        headers: headers
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

const getMessageMiYi = function (_token, item, phone=null, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_MIYI.url + CODE_PLATFORM_MIYI.uri.getMessage,
        params: {
            token: _token,
            sid: item,
            phone: phone
        }
    }, {
        headers: headers
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
    loginMiYi,
    getBalanceMiYi,
    getPhoneNumberMiYi,
    getSelfDefinePhoneNumberMiYi,
    releasePhoneNumberMiYi,
    removePhoneNumberMiYi,
    getMessageMiYi
};
